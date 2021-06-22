#--------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
#--------------------------------------------------------------------------
import sys
from unittest.mock import Mock
from azure.core.pipeline import AsyncPipeline
from azure.core.pipeline.transport._base import SupportedFormat
from azure.core.pipeline.policies import (
    SansIOHTTPPolicy,
    UserAgentPolicy,
    DistributedTracingPolicy,
    AsyncRetryPolicy,
    AsyncRedirectPolicy,
    AsyncHTTPPolicy,
    AsyncRetryPolicy,
    HttpLoggingPolicy,
)
from azure.core.pipeline.transport import (
    AsyncHttpTransport,
    HttpRequest as PipelineTransportHttpRequest,
    AsyncioRequestsTransport,
    TrioRequestsTransport,
    AioHttpTransport
)
from azure.core.rest import HttpRequest as RestHttpRequest

from azure.core.polling.async_base_polling import AsyncLROBasePolling
from azure.core.polling.base_polling import LocationPolling

from azure.core.configuration import Configuration
from azure.core import AsyncPipelineClient
from azure.core.exceptions import AzureError

import aiohttp
import trio

import pytest


@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [PipelineTransportHttpRequest, RestHttpRequest])
async def test_sans_io_exception(request_type):
    class BrokenSender(AsyncHttpTransport):
        async def send(self, request, **config):
            raise ValueError("Broken")

        async def open(self):
            self.session = requests.Session()

        async def close(self):
            self.session.close()

        @property
        def supported_formats(self):
            return [SupportedFormat.REST] if hasattr(request_type, "content") else [SupportedFormat.PIPELINE_TRANSPORT]

        async def __aexit__(self, exc_type, exc_value, traceback):
            """Raise any exception triggered within the runtime context."""
            return self.close()

    pipeline = AsyncPipeline(BrokenSender(), [SansIOHTTPPolicy()])

    req = request_type('GET', '/')
    with pytest.raises(ValueError):
        await pipeline.run(req)

    class SwapExec(SansIOHTTPPolicy):
        def on_exception(self, requests, **kwargs):
            exc_type, exc_value, exc_traceback = sys.exc_info()
            raise NotImplementedError(exc_value)

    pipeline = AsyncPipeline(BrokenSender(), [SwapExec()])
    with pytest.raises(NotImplementedError):
        await pipeline.run(req)


@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [PipelineTransportHttpRequest, RestHttpRequest])
async def test_basic_aiohttp(request_type):

    request = request_type("GET", "https://bing.com")
    policies = [
        UserAgentPolicy("myusergant"),
        AsyncRedirectPolicy()
    ]
    async with AsyncPipeline(AioHttpTransport(), policies=policies) as pipeline:
        response = await pipeline.run(request)

    assert pipeline._transport.session is None
    # all we need to check is if we are able to make the call
    assert isinstance(response.http_response.status_code, int)

@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [PipelineTransportHttpRequest, RestHttpRequest])
async def test_basic_aiohttp_separate_session(request_type):

    session = aiohttp.ClientSession()
    request = request_type("GET", "https://bing.com")
    policies = [
        UserAgentPolicy("myusergant"),
        AsyncRedirectPolicy()
    ]
    transport = AioHttpTransport(session=session, session_owner=False)
    async with AsyncPipeline(transport, policies=policies) as pipeline:
        response = await pipeline.run(request)

    assert transport.session
    assert isinstance(response.http_response.status_code, int)
    await transport.close()
    assert transport.session
    await transport.session.close()

@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [PipelineTransportHttpRequest, RestHttpRequest])
async def test_basic_async_requests(request_type):

    request = request_type("GET", "https://bing.com")
    policies = [
        UserAgentPolicy("myusergant"),
        AsyncRedirectPolicy()
    ]
    async with AsyncPipeline(AsyncioRequestsTransport(), policies=policies) as pipeline:
        response = await pipeline.run(request)

    assert isinstance(response.http_response.status_code, int)

@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [PipelineTransportHttpRequest, RestHttpRequest])
async def test_async_transport_sleep(request_type):

    async with AsyncioRequestsTransport() as transport:
        await transport.sleep(1)

    async with AioHttpTransport() as transport:
        await transport.sleep(1)

def test_polling_with_path_format_arguments():
    method = AsyncLROBasePolling(
        timeout=0,
        path_format_arguments={"host": "host:3000", "accountName": "local"}
    )
    client = AsyncPipelineClient(base_url="http://{accountName}{host}")

    method._operation = LocationPolling()
    method._operation._location_url = "/results/1"
    method._client = client
    assert "http://localhost:3000/results/1" == method._client.format_url(method._operation.get_polling_url(), **method._path_format_arguments)

def test_async_trio_transport_sleep():

    async def do():
        async with TrioRequestsTransport() as transport:
            await transport.sleep(1)

    response = trio.run(do)

def test_default_http_logging_policy():
    config = Configuration()
    pipeline_client = AsyncPipelineClient(base_url="test")
    pipeline = pipeline_client._build_pipeline(config)
    http_logging_policy = pipeline._impl_policies[-1]._policy
    assert http_logging_policy.allowed_header_names == HttpLoggingPolicy.DEFAULT_HEADERS_WHITELIST

def test_pass_in_http_logging_policy():
    config = Configuration()
    http_logging_policy = HttpLoggingPolicy()
    http_logging_policy.allowed_header_names.update(
        {"x-ms-added-header"}
    )
    config.http_logging_policy = http_logging_policy

    pipeline_client = AsyncPipelineClient(base_url="test")
    pipeline = pipeline_client._build_pipeline(config)
    http_logging_policy = pipeline._impl_policies[-1]._policy
    assert http_logging_policy.allowed_header_names == HttpLoggingPolicy.DEFAULT_HEADERS_WHITELIST.union({"x-ms-added-header"})

@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [PipelineTransportHttpRequest, RestHttpRequest])
async def test_conf_async_requests(request_type):

    request = request_type("GET", "https://bing.com/")
    policies = [
        UserAgentPolicy("myusergant"),
        AsyncRedirectPolicy()
    ]
    async with AsyncPipeline(AsyncioRequestsTransport(), policies=policies) as pipeline:
        response = await pipeline.run(request)

    assert isinstance(response.http_response.status_code, int)

@pytest.mark.parametrize("request_type", [PipelineTransportHttpRequest, RestHttpRequest])
def test_conf_async_trio_requests(request_type):

    async def do():
        request = request_type("GET", "https://bing.com/")
        policies = [
            UserAgentPolicy("myusergant"),
            AsyncRedirectPolicy()
        ]
        async with AsyncPipeline(TrioRequestsTransport(), policies=policies) as pipeline:
            return await pipeline.run(request)

    response = trio.run(do)
    assert isinstance(response.http_response.status_code, int)

@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [PipelineTransportHttpRequest, RestHttpRequest])
async def test_retry_without_http_response(request_type, add_properties_to_transport):
    class NaughtyPolicy(AsyncHTTPPolicy):
        def send(*args):
            raise AzureError('boo')

    policies = [AsyncRetryPolicy(), NaughtyPolicy()]
    transport = Mock()
    add_properties_to_transport(transport)
    pipeline = AsyncPipeline(policies=policies, transport=transport)
    with pytest.raises(AzureError):
        await pipeline.run(request_type('GET', url='https://foo.bar'))

@pytest.mark.asyncio
async def test_add_custom_policy():
    class BooPolicy(AsyncHTTPPolicy):
        def send(*args):
            raise AzureError('boo')

    class FooPolicy(AsyncHTTPPolicy):
        def send(*args):
            raise AzureError('boo')

    config = Configuration()
    retry_policy = AsyncRetryPolicy()
    config.retry_policy = retry_policy
    boo_policy = BooPolicy()
    foo_policy = FooPolicy()
    client = AsyncPipelineClient(base_url="test", config=config, per_call_policies=boo_policy)
    policies = client._pipeline._impl_policies
    assert boo_policy in policies
    pos_boo = policies.index(boo_policy)
    pos_retry = policies.index(retry_policy)
    assert pos_boo < pos_retry

    client = AsyncPipelineClient(base_url="test", config=config, per_call_policies=[boo_policy])
    policies = client._pipeline._impl_policies
    assert boo_policy in policies
    pos_boo = policies.index(boo_policy)
    pos_retry = policies.index(retry_policy)
    assert pos_boo < pos_retry

    client = AsyncPipelineClient(base_url="test", config=config, per_retry_policies=boo_policy)
    policies = client._pipeline._impl_policies
    assert boo_policy in policies
    pos_boo = policies.index(boo_policy)
    pos_retry = policies.index(retry_policy)
    assert pos_boo > pos_retry

    client = AsyncPipelineClient(base_url="test", config=config, per_retry_policies=[boo_policy])
    policies = client._pipeline._impl_policies
    assert boo_policy in policies
    pos_boo = policies.index(boo_policy)
    pos_retry = policies.index(retry_policy)
    assert pos_boo > pos_retry

    client = AsyncPipelineClient(base_url="test", config=config, per_call_policies=boo_policy,
                                 per_retry_policies=foo_policy)
    policies = client._pipeline._impl_policies
    assert boo_policy in policies
    assert foo_policy in policies
    pos_boo = policies.index(boo_policy)
    pos_foo = policies.index(foo_policy)
    pos_retry = policies.index(retry_policy)
    assert pos_boo < pos_retry
    assert pos_foo > pos_retry

    client = AsyncPipelineClient(base_url="test", config=config, per_call_policies=[boo_policy],
                                 per_retry_policies=[foo_policy])
    policies = client._pipeline._impl_policies
    assert boo_policy in policies
    assert foo_policy in policies
    pos_boo = policies.index(boo_policy)
    pos_foo = policies.index(foo_policy)
    pos_retry = policies.index(retry_policy)
    assert pos_boo < pos_retry
    assert pos_foo > pos_retry

    policies = [UserAgentPolicy(),
                AsyncRetryPolicy(),
                DistributedTracingPolicy()]
    client = AsyncPipelineClient(base_url="test", policies=policies, per_call_policies=boo_policy)
    actual_policies = client._pipeline._impl_policies
    assert boo_policy == actual_policies[0]
    client = AsyncPipelineClient(base_url="test", policies=policies, per_call_policies=[boo_policy])
    actual_policies = client._pipeline._impl_policies
    assert boo_policy == actual_policies[0]

    client = AsyncPipelineClient(base_url="test", policies=policies, per_retry_policies=foo_policy)
    actual_policies = client._pipeline._impl_policies
    assert foo_policy == actual_policies[2]
    client = AsyncPipelineClient(base_url="test", policies=policies, per_retry_policies=[foo_policy])
    actual_policies = client._pipeline._impl_policies
    assert foo_policy == actual_policies[2]

    client = AsyncPipelineClient(base_url="test", policies=policies, per_call_policies=boo_policy,
                                 per_retry_policies=[foo_policy])
    actual_policies = client._pipeline._impl_policies
    assert boo_policy == actual_policies[0]
    assert foo_policy == actual_policies[3]
    client = AsyncPipelineClient(base_url="test", policies=policies, per_call_policies=[boo_policy],
                            per_retry_policies=[foo_policy])
    actual_policies = client._pipeline._impl_policies
    assert boo_policy == actual_policies[0]
    assert foo_policy == actual_policies[3]

    policies = [UserAgentPolicy(),
                DistributedTracingPolicy()]
    with pytest.raises(ValueError):
        client = AsyncPipelineClient(base_url="test", policies=policies, per_retry_policies=foo_policy)
    with pytest.raises(ValueError):
        client = AsyncPipelineClient(base_url="test", policies=policies, per_retry_policies=[foo_policy])
