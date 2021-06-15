# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.pipeline.transport._base import _format_url_section
from azure.synapse.artifacts.core.rest import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Dict, IO, Optional

_SERIALIZER = Serializer()


def build_rerun_trigger_instance_request(
    trigger_name,  # type: str
    run_id,  # type: str
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Rerun single trigger instance by runId.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param trigger_name: The trigger name.
    :type trigger_name: str
    :param run_id: The pipeline run identifier.
    :type run_id: str
    :return: Returns an :class:`~azure.synapse.artifacts.core.rest .HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.synapse.artifacts.core.rest .HttpRequest
    """

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/triggers/{triggerName}/triggerRuns/{runId}/rerun")
    path_format_arguments = {
        "triggerName": _SERIALIZER.url(
            "trigger_name",
            trigger_name,
            "str",
            max_length=260,
            min_length=1,
            pattern=r"^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$",
        ),
        "runId": _SERIALIZER.url("run_id", run_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_cancel_trigger_instance_request(
    trigger_name,  # type: str
    run_id,  # type: str
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Cancel single trigger instance by runId.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param trigger_name: The trigger name.
    :type trigger_name: str
    :param run_id: The pipeline run identifier.
    :type run_id: str
    :return: Returns an :class:`~azure.synapse.artifacts.core.rest .HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.synapse.artifacts.core.rest .HttpRequest
    """

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/triggers/{triggerName}/triggerRuns/{runId}/cancel")
    path_format_arguments = {
        "triggerName": _SERIALIZER.url(
            "trigger_name",
            trigger_name,
            "str",
            max_length=260,
            min_length=1,
            pattern=r"^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$",
        ),
        "runId": _SERIALIZER.url("run_id", run_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_query_trigger_runs_by_workspace_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Query trigger runs.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Parameters to filter the pipeline run.
    :paramtype json: Any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Parameters to filter the pipeline run.
    :paramtype content: Any
    :return: Returns an :class:`~azure.synapse.artifacts.core.rest .HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.synapse.artifacts.core.rest .HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "continuationToken": "str (optional)",
                "filters": [
                    {
                        "operand": "str",
                        "operator": "str",
                        "values": [
                            "str"
                        ]
                    }
                ],
                "lastUpdatedAfter": "datetime",
                "lastUpdatedBefore": "datetime",
                "orderBy": [
                    {
                        "order": "str",
                        "orderBy": "str"
                    }
                ]
            }

            # response body for status code(s): 200
            response.json() == {
                "continuationToken": "str (optional)",
                "value": [
                    {
                        "": {
                            "str": "object (optional)"
                        },
                        "message": "str (optional)",
                        "properties": {
                            "str": "str (optional)"
                        },
                        "status": "str (optional)",
                        "triggerName": "str (optional)",
                        "triggerRunId": "str (optional)",
                        "triggerRunTimestamp": "datetime (optional)",
                        "triggerType": "str (optional)",
                        "triggeredPipelines": {
                            "str": "str (optional)"
                        }
                    }
                ]
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]
    json = kwargs.pop("json", None)  # type: Any

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/queryTriggerRuns")

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, params=query_parameters, headers=header_parameters, **kwargs)
