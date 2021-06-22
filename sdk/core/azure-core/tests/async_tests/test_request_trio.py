# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE.txt in the project root for
# license information.
# -------------------------------------------------------------------------
import json
from azure.core import rest

from azure.core.pipeline.transport import TrioRequestsTransport, HttpRequest as PipelineTransportHttpRequest
from azure.core.rest import HttpRequest as RestHttpRequest

import pytest


@pytest.mark.trio
@pytest.mark.parametrize("request_type", [PipelineTransportHttpRequest, RestHttpRequest])
async def test_async_gen_data(request_type):
    class AsyncGen:
        def __init__(self):
            self._range = iter([b"azerty"])

        def __aiter__(self):
            return self

        async def __anext__(self):
            try:
                return next(self._range)
            except StopIteration:
                raise StopAsyncIteration

    async with TrioRequestsTransport() as transport:
        if hasattr(request_type, "content"):
            # only pipeline transport requests actually go into the transport code
            rest_request = request_type('GET', 'http://httpbin.org/anything', content=AsyncGen())
            req = PipelineTransportHttpRequest._from_rest_request(rest_request)
        else:
            req = request_type('GET', 'http://httpbin.org/anything', data=AsyncGen())
        response = await transport.send(req)
        assert json.loads(response.text())['data'] == "azerty"

@pytest.mark.trio
@pytest.mark.parametrize("request_type", [PipelineTransportHttpRequest, RestHttpRequest])
async def test_send_data(request_type):
    async with TrioRequestsTransport() as transport:
        if hasattr(request_type, "content"):
            # only pipeline transport requests actually go into the transport code
            rest_request = request_type('PUT', 'http://httpbin.org/anything', content=b"azerty")
            req = PipelineTransportHttpRequest._from_rest_request(rest_request)
        else:
            req = request_type('PUT', 'http://httpbin.org/anything', data=b"azerty")
        response = await transport.send(req)

        assert json.loads(response.text())['data'] == "azerty"