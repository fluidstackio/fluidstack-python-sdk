# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.query_encoder import encode_query
from ..core.remove_none_from_dict import remove_none_from_dict
from ..core.request_options import RequestOptions
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.create_instance_response import CreateInstanceResponse
from ..types.gpu_type import GpuType
from ..types.http_validation_error import HttpValidationError
from ..types.list_instance_response import ListInstanceResponse
from ..types.message import Message
from ..types.region import Region
from ..types.supported_operating_system import SupportedOperatingSystem

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class InstancesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[ListInstanceResponse]:
        """
        This endpoint is used to retrieve a list of all instances associated with the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ListInstanceResponse]
            Successful Response

        Examples
        --------
        from FluidStack.client import FluidStack

        client = FluidStack(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.instances.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "instances"),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[ListInstanceResponse], _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(Message, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        gpu_type: GpuType,
        ssh_keys: typing.Sequence[str],
        name: typing.Optional[str] = OMIT,
        gpu_count: typing.Optional[int] = OMIT,
        operating_system_label: typing.Optional[SupportedOperatingSystem] = OMIT,
        region: typing.Optional[Region] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateInstanceResponse:
        """
        This endpoint is used to create a new instance. You must provide a name for the instance, the gpu_type, and a list of SSH key names.

        If you do not provide values for gpu_count and operating_system_label when calling this endpoint, the default values of 1 and 'ubuntu_20_04_lts' are used respectively.

        Parameters
        ----------
        gpu_type : GpuType

        ssh_keys : typing.Sequence[str]
            The list of SSH key names to add to the instance

            These SSH keys are used to connect to the instance.

        name : typing.Optional[str]
            The name of the instance.

        gpu_count : typing.Optional[int]
            The number of GPUs to attach to the instance.

        operating_system_label : typing.Optional[SupportedOperatingSystem]
            The operating system label to be used to create the instance.

        region : typing.Optional[Region]
            The region to create the instance in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateInstanceResponse
            Successful Response

        Examples
        --------
        from FluidStack.client import FluidStack

        client = FluidStack(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.instances.create(
            gpu_type="RTX_A4000_16GB",
            ssh_keys=["ssh_keys"],
        )
        """
        _request: typing.Dict[str, typing.Any] = {"gpu_type": gpu_type, "ssh_keys": ssh_keys}
        if name is not OMIT:
            _request["name"] = name
        if gpu_count is not OMIT:
            _request["gpu_count"] = gpu_count
        if operating_system_label is not OMIT:
            _request["operating_system_label"] = operating_system_label
        if region is not OMIT:
            _request["region"] = region
        _response = self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "instances"),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(CreateInstanceResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(Message, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def stop(
        self, instance_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListInstanceResponse:
        """
        This endpoint can be used to stop an existing instance by its ID.

        Parameters
        ----------
        instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListInstanceResponse
            Successful Response

        Examples
        --------
        from FluidStack.client import FluidStack

        client = FluidStack(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.instances.stop(
            instance_id="instance_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="PUT",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"instances/{jsonable_encoder(instance_id)}/stop"
            ),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))
            if request_options is not None
            else None,
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ListInstanceResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(Message, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def start(
        self, instance_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListInstanceResponse:
        """
        This endpoint can be used to start an existing instance by its ID.

        Parameters
        ----------
        instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListInstanceResponse
            Successful Response

        Examples
        --------
        from FluidStack.client import FluidStack

        client = FluidStack(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.instances.start(
            instance_id="instance_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="PUT",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"instances/{jsonable_encoder(instance_id)}/start"
            ),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))
            if request_options is not None
            else None,
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ListInstanceResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(Message, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, instance_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        This endpoint can be used to terminate an existing instance by its ID.

        Parameters
        ----------
        instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from FluidStack.client import FluidStack

        client = FluidStack(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.instances.delete(
            instance_id="instance_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="DELETE",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"instances/{jsonable_encoder(instance_id)}"
            ),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))
            if request_options is not None
            else None,
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(Message, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncInstancesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ListInstanceResponse]:
        """
        This endpoint is used to retrieve a list of all instances associated with the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ListInstanceResponse]
            Successful Response

        Examples
        --------
        from FluidStack.client import AsyncFluidStack

        client = AsyncFluidStack(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.instances.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "instances"),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[ListInstanceResponse], _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(Message, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        gpu_type: GpuType,
        ssh_keys: typing.Sequence[str],
        name: typing.Optional[str] = OMIT,
        gpu_count: typing.Optional[int] = OMIT,
        operating_system_label: typing.Optional[SupportedOperatingSystem] = OMIT,
        region: typing.Optional[Region] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateInstanceResponse:
        """
        This endpoint is used to create a new instance. You must provide a name for the instance, the gpu_type, and a list of SSH key names.

        If you do not provide values for gpu_count and operating_system_label when calling this endpoint, the default values of 1 and 'ubuntu_20_04_lts' are used respectively.

        Parameters
        ----------
        gpu_type : GpuType

        ssh_keys : typing.Sequence[str]
            The list of SSH key names to add to the instance

            These SSH keys are used to connect to the instance.

        name : typing.Optional[str]
            The name of the instance.

        gpu_count : typing.Optional[int]
            The number of GPUs to attach to the instance.

        operating_system_label : typing.Optional[SupportedOperatingSystem]
            The operating system label to be used to create the instance.

        region : typing.Optional[Region]
            The region to create the instance in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateInstanceResponse
            Successful Response

        Examples
        --------
        from FluidStack.client import AsyncFluidStack

        client = AsyncFluidStack(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.instances.create(
            gpu_type="RTX_A4000_16GB",
            ssh_keys=["ssh_keys"],
        )
        """
        _request: typing.Dict[str, typing.Any] = {"gpu_type": gpu_type, "ssh_keys": ssh_keys}
        if name is not OMIT:
            _request["name"] = name
        if gpu_count is not OMIT:
            _request["gpu_count"] = gpu_count
        if operating_system_label is not OMIT:
            _request["operating_system_label"] = operating_system_label
        if region is not OMIT:
            _request["region"] = region
        _response = await self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "instances"),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(CreateInstanceResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(Message, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def stop(
        self, instance_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListInstanceResponse:
        """
        This endpoint can be used to stop an existing instance by its ID.

        Parameters
        ----------
        instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListInstanceResponse
            Successful Response

        Examples
        --------
        from FluidStack.client import AsyncFluidStack

        client = AsyncFluidStack(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.instances.stop(
            instance_id="instance_id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="PUT",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"instances/{jsonable_encoder(instance_id)}/stop"
            ),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))
            if request_options is not None
            else None,
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ListInstanceResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(Message, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def start(
        self, instance_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListInstanceResponse:
        """
        This endpoint can be used to start an existing instance by its ID.

        Parameters
        ----------
        instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListInstanceResponse
            Successful Response

        Examples
        --------
        from FluidStack.client import AsyncFluidStack

        client = AsyncFluidStack(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.instances.start(
            instance_id="instance_id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="PUT",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"instances/{jsonable_encoder(instance_id)}/start"
            ),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))
            if request_options is not None
            else None,
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ListInstanceResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(Message, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, instance_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        This endpoint can be used to terminate an existing instance by its ID.

        Parameters
        ----------
        instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from FluidStack.client import AsyncFluidStack

        client = AsyncFluidStack(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.instances.delete(
            instance_id="instance_id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="DELETE",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"instances/{jsonable_encoder(instance_id)}"
            ),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))
            if request_options is not None
            else None,
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(Message, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
