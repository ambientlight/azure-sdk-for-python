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


def build_get_notebooks_by_workspace_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Lists Notebooks.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :return: Returns an :class:`~azure.synapse.artifacts.core.rest .HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.synapse.artifacts.core.rest .HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "nextLink": "str (optional)",
                "value": [
                    {
                        "etag": "str (optional)",
                        "id": "str (optional)",
                        "name": "str",
                        "properties": {
                            "": {
                                "str": "object (optional)"
                            },
                            "bigDataPool": {
                                "referenceName": "str",
                                "type": "str"
                            },
                            "cells": [
                                {
                                    "": {
                                        "str": "object (optional)"
                                    },
                                    "attachments": "object (optional)",
                                    "cell_type": "str",
                                    "metadata": "object",
                                    "outputs": [
                                        {
                                            "data": "object (optional)",
                                            "execution_count": "int (optional)",
                                            "metadata": "object (optional)",
                                            "name": "str (optional)",
                                            "output_type": "str",
                                            "text": "object (optional)"
                                        }
                                    ],
                                    "source": [
                                        "str"
                                    ]
                                }
                            ],
                            "description": "str (optional)",
                            "metadata": {
                                "": {
                                    "str": "object (optional)"
                                },
                                "kernelspec": {
                                    "": {
                                        "str": "object (optional)"
                                    },
                                    "display_name": "str",
                                    "name": "str"
                                },
                                "language_info": {
                                    "": {
                                        "str": "object (optional)"
                                    },
                                    "codemirror_mode": "str (optional)",
                                    "name": "str"
                                }
                            },
                            "nbformat": "int",
                            "nbformat_minor": "int",
                            "sessionProperties": {
                                "driverCores": "int",
                                "driverMemory": "str",
                                "executorCores": "int",
                                "executorMemory": "str",
                                "numExecutors": "int"
                            }
                        },
                        "type": "str (optional)"
                    }
                ]
            }
    """

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/notebooks")

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_get_notebook_summary_by_work_space_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Lists a summary of Notebooks.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :return: Returns an :class:`~azure.synapse.artifacts.core.rest .HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.synapse.artifacts.core.rest .HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "nextLink": "str (optional)",
                "value": [
                    {
                        "etag": "str (optional)",
                        "id": "str (optional)",
                        "name": "str",
                        "properties": {
                            "": {
                                "str": "object (optional)"
                            },
                            "bigDataPool": {
                                "referenceName": "str",
                                "type": "str"
                            },
                            "cells": [
                                {
                                    "": {
                                        "str": "object (optional)"
                                    },
                                    "attachments": "object (optional)",
                                    "cell_type": "str",
                                    "metadata": "object",
                                    "outputs": [
                                        {
                                            "data": "object (optional)",
                                            "execution_count": "int (optional)",
                                            "metadata": "object (optional)",
                                            "name": "str (optional)",
                                            "output_type": "str",
                                            "text": "object (optional)"
                                        }
                                    ],
                                    "source": [
                                        "str"
                                    ]
                                }
                            ],
                            "description": "str (optional)",
                            "metadata": {
                                "": {
                                    "str": "object (optional)"
                                },
                                "kernelspec": {
                                    "": {
                                        "str": "object (optional)"
                                    },
                                    "display_name": "str",
                                    "name": "str"
                                },
                                "language_info": {
                                    "": {
                                        "str": "object (optional)"
                                    },
                                    "codemirror_mode": "str (optional)",
                                    "name": "str"
                                }
                            },
                            "nbformat": "int",
                            "nbformat_minor": "int",
                            "sessionProperties": {
                                "driverCores": "int",
                                "driverMemory": "str",
                                "executorCores": "int",
                                "executorMemory": "str",
                                "numExecutors": "int"
                            }
                        },
                        "type": "str (optional)"
                    }
                ]
            }
    """

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/notebooksSummary")

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_create_or_update_notebook_request_initial(
    notebook_name,  # type: str
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Creates or updates a Note Book.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param notebook_name: The notebook name.
    :type notebook_name: str
    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Note book resource definition.
    :paramtype json: Any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Note book resource definition.
    :paramtype content: Any
    :keyword if_match: ETag of the Note book entity.  Should only be specified for update, for
     which it should match existing entity or can be * for unconditional update.
    :paramtype if_match: str
    :return: Returns an :class:`~azure.synapse.artifacts.core.rest .HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.synapse.artifacts.core.rest .HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "etag": "str (optional)",
                "id": "str (optional)",
                "name": "str",
                "properties": {
                    "": {
                        "str": "object (optional)"
                    },
                    "bigDataPool": {
                        "referenceName": "str",
                        "type": "str"
                    },
                    "cells": [
                        {
                            "": {
                                "str": "object (optional)"
                            },
                            "attachments": "object (optional)",
                            "cell_type": "str",
                            "metadata": "object",
                            "outputs": [
                                {
                                    "data": "object (optional)",
                                    "execution_count": "int (optional)",
                                    "metadata": "object (optional)",
                                    "name": "str (optional)",
                                    "output_type": "str",
                                    "text": "object (optional)"
                                }
                            ],
                            "source": [
                                "str"
                            ]
                        }
                    ],
                    "description": "str (optional)",
                    "metadata": {
                        "": {
                            "str": "object (optional)"
                        },
                        "kernelspec": {
                            "": {
                                "str": "object (optional)"
                            },
                            "display_name": "str",
                            "name": "str"
                        },
                        "language_info": {
                            "": {
                                "str": "object (optional)"
                            },
                            "codemirror_mode": "str (optional)",
                            "name": "str"
                        }
                    },
                    "nbformat": "int",
                    "nbformat_minor": "int",
                    "sessionProperties": {
                        "driverCores": "int",
                        "driverMemory": "str",
                        "executorCores": "int",
                        "executorMemory": "str",
                        "numExecutors": "int"
                    }
                },
                "type": "str (optional)"
            }

            # response body for status code(s): 200
            response.json() == {
                "etag": "str (optional)",
                "id": "str (optional)",
                "name": "str",
                "properties": {
                    "": {
                        "str": "object (optional)"
                    },
                    "bigDataPool": {
                        "referenceName": "str",
                        "type": "str"
                    },
                    "cells": [
                        {
                            "": {
                                "str": "object (optional)"
                            },
                            "attachments": "object (optional)",
                            "cell_type": "str",
                            "metadata": "object",
                            "outputs": [
                                {
                                    "data": "object (optional)",
                                    "execution_count": "int (optional)",
                                    "metadata": "object (optional)",
                                    "name": "str (optional)",
                                    "output_type": "str",
                                    "text": "object (optional)"
                                }
                            ],
                            "source": [
                                "str"
                            ]
                        }
                    ],
                    "description": "str (optional)",
                    "metadata": {
                        "": {
                            "str": "object (optional)"
                        },
                        "kernelspec": {
                            "": {
                                "str": "object (optional)"
                            },
                            "display_name": "str",
                            "name": "str"
                        },
                        "language_info": {
                            "": {
                                "str": "object (optional)"
                            },
                            "codemirror_mode": "str (optional)",
                            "name": "str"
                        }
                    },
                    "nbformat": "int",
                    "nbformat_minor": "int",
                    "sessionProperties": {
                        "driverCores": "int",
                        "driverMemory": "str",
                        "executorCores": "int",
                        "executorMemory": "str",
                        "numExecutors": "int"
                    }
                },
                "type": "str (optional)"
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]
    json = kwargs.pop("json", None)  # type: Any
    if_match = kwargs.pop("if_match", None)  # type: Optional[str]
    if_match = kwargs.pop("if_match", None)  # type: Optional[str]

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/notebooks/{notebookName}")
    path_format_arguments = {
        "notebookName": _SERIALIZER.url("notebook_name", notebook_name, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if if_match is not None:
        header_parameters["If-Match"] = _SERIALIZER.header("if_match", if_match, "str")
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_get_notebook_request(
    notebook_name,  # type: str
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Gets a Note Book.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param notebook_name: The notebook name.
    :type notebook_name: str
    :keyword if_none_match: ETag of the Notebook entity. Should only be specified for get. If the
     ETag matches the existing entity tag, or if * was provided, then no content will be returned.
    :paramtype if_none_match: str
    :return: Returns an :class:`~azure.synapse.artifacts.core.rest .HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.synapse.artifacts.core.rest .HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "etag": "str (optional)",
                "id": "str (optional)",
                "name": "str",
                "properties": {
                    "": {
                        "str": "object (optional)"
                    },
                    "bigDataPool": {
                        "referenceName": "str",
                        "type": "str"
                    },
                    "cells": [
                        {
                            "": {
                                "str": "object (optional)"
                            },
                            "attachments": "object (optional)",
                            "cell_type": "str",
                            "metadata": "object",
                            "outputs": [
                                {
                                    "data": "object (optional)",
                                    "execution_count": "int (optional)",
                                    "metadata": "object (optional)",
                                    "name": "str (optional)",
                                    "output_type": "str",
                                    "text": "object (optional)"
                                }
                            ],
                            "source": [
                                "str"
                            ]
                        }
                    ],
                    "description": "str (optional)",
                    "metadata": {
                        "": {
                            "str": "object (optional)"
                        },
                        "kernelspec": {
                            "": {
                                "str": "object (optional)"
                            },
                            "display_name": "str",
                            "name": "str"
                        },
                        "language_info": {
                            "": {
                                "str": "object (optional)"
                            },
                            "codemirror_mode": "str (optional)",
                            "name": "str"
                        }
                    },
                    "nbformat": "int",
                    "nbformat_minor": "int",
                    "sessionProperties": {
                        "driverCores": "int",
                        "driverMemory": "str",
                        "executorCores": "int",
                        "executorMemory": "str",
                        "numExecutors": "int"
                    }
                },
                "type": "str (optional)"
            }
    """

    if_none_match = kwargs.pop("if_none_match", None)  # type: Optional[str]
    if_none_match = kwargs.pop("if_none_match", None)  # type: Optional[str]

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/notebooks/{notebookName}")
    path_format_arguments = {
        "notebookName": _SERIALIZER.url("notebook_name", notebook_name, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if if_none_match is not None:
        header_parameters["If-None-Match"] = _SERIALIZER.header("if_none_match", if_none_match, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_delete_notebook_request_initial(
    notebook_name,  # type: str
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Deletes a Note book.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param notebook_name: The notebook name.
    :type notebook_name: str
    :return: Returns an :class:`~azure.synapse.artifacts.core.rest .HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.synapse.artifacts.core.rest .HttpRequest
    """

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/notebooks/{notebookName}")
    path_format_arguments = {
        "notebookName": _SERIALIZER.url("notebook_name", notebook_name, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_rename_notebook_request_initial(
    notebook_name,  # type: str
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Renames a notebook.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param notebook_name: The notebook name.
    :type notebook_name: str
    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. proposed new name.
    :paramtype json: Any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). proposed new name.
    :paramtype content: Any
    :return: Returns an :class:`~azure.synapse.artifacts.core.rest .HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.synapse.artifacts.core.rest .HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "newName": "str (optional)"
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]
    json = kwargs.pop("json", None)  # type: Any

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/notebooks/{notebookName}/rename")
    path_format_arguments = {
        "notebookName": _SERIALIZER.url("notebook_name", notebook_name, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, params=query_parameters, headers=header_parameters, **kwargs)
