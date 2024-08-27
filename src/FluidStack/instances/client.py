# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.create_instance_response import CreateInstanceResponse
from ..types.gpu_type import GpuType
from ..types.http_validation_error import HttpValidationError
from ..types.instance_response import InstanceResponse
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
        )
        client.instances.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "instances", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(typing.List[ListInstanceResponse], _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(Message, _response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        gpu_type: GpuType,
        ssh_key: str,
        name: typing.Optional[str] = OMIT,
        gpu_count: typing.Optional[int] = OMIT,
        operating_system_label: typing.Optional[SupportedOperatingSystem] = OMIT,
        region: typing.Optional[Region] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateInstanceResponse:
        """
        This endpoint is used to create a new instance. You must provide a custom `name` for the instance, its `gpu_type`, and the name of its `ssh_key`.

        If no values are provided for the `gpu_count` and `operating_system_label`, the default values of `1` and `ubuntu_20_04_lts_nvidia` are used respectively.

        Parameters
        ----------
        gpu_type : GpuType
            The GPU type of the instance.

        ssh_key : str
            The SSH key name to add to the instance. This SSH key is used to connect to the instance.

        name : typing.Optional[str]
            The custom name of the instance.

        gpu_count : typing.Optional[int]
            The number of GPUs to attach to the instance.

        operating_system_label : typing.Optional[SupportedOperatingSystem]
            The operating system label used to create the instance.

        region : typing.Optional[Region]
            The region in which to create the instance.

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
        )
        client.instances.create(
            name="my_instance_name",
            gpu_type="RTX_A5000_24GB",
            ssh_key="my_ssh_key",
            operating_system_label="ubuntu_20_04_lts_nvidia",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "instances",
            method="POST",
            json={
                "name": name,
                "gpu_type": gpu_type,
                "gpu_count": gpu_count,
                "ssh_key": ssh_key,
                "operating_system_label": operating_system_label,
                "region": region,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(CreateInstanceResponse, _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(Message, _response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, instance_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> InstanceResponse:
        """
        This endpoint is used to retrieve a single instance associated with the authenticated user by its ID.

        Parameters
        ----------
        instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InstanceResponse
            Successful Response

        Examples
        --------
        from FluidStack.client import FluidStack

        client = FluidStack(
            api_key="YOUR_API_KEY",
        )
        client.instances.get(
            instance_id="{instance_id}",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"instances/{jsonable_encoder(instance_id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(InstanceResponse, _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(Message, _response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, instance_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        This endpoint is used to terminate an existing instance by its ID.

        Parameters
        ----------
        instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from FluidStack.client import FluidStack

        client = FluidStack(
            api_key="YOUR_API_KEY",
        )
        client.instances.delete(
            instance_id="{instance_id}",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"instances/{jsonable_encoder(instance_id)}", method="DELETE", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(typing.Any, _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(Message, _response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def stop(
        self, instance_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListInstanceResponse:
        """
        This endpoint is used to stop an existing instance by its ID.

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
        )
        client.instances.stop(
            instance_id="{instance_id}",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"instances/{jsonable_encoder(instance_id)}/stop", method="PUT", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ListInstanceResponse, _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(Message, _response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def start(
        self, instance_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListInstanceResponse:
        """
        This endpoint is used to start an existing instance by its ID.

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
        )
        client.instances.start(
            instance_id="{instance_id}",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"instances/{jsonable_encoder(instance_id)}/start", method="PUT", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ListInstanceResponse, _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(Message, _response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
                )
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
        )
        await client.instances.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "instances", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(typing.List[ListInstanceResponse], _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(Message, _response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        gpu_type: GpuType,
        ssh_key: str,
        name: typing.Optional[str] = OMIT,
        gpu_count: typing.Optional[int] = OMIT,
        operating_system_label: typing.Optional[SupportedOperatingSystem] = OMIT,
        region: typing.Optional[Region] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateInstanceResponse:
        """
        This endpoint is used to create a new instance. You must provide a custom `name` for the instance, its `gpu_type`, and the name of its `ssh_key`.

        If no values are provided for the `gpu_count` and `operating_system_label`, the default values of `1` and `ubuntu_20_04_lts_nvidia` are used respectively.

        Parameters
        ----------
        gpu_type : GpuType
            The GPU type of the instance.

        ssh_key : str
            The SSH key name to add to the instance. This SSH key is used to connect to the instance.

        name : typing.Optional[str]
            The custom name of the instance.

        gpu_count : typing.Optional[int]
            The number of GPUs to attach to the instance.

        operating_system_label : typing.Optional[SupportedOperatingSystem]
            The operating system label used to create the instance.

        region : typing.Optional[Region]
            The region in which to create the instance.

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
        )
        await client.instances.create(
            name="my_instance_name",
            gpu_type="RTX_A5000_24GB",
            ssh_key="my_ssh_key",
            operating_system_label="ubuntu_20_04_lts_nvidia",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "instances",
            method="POST",
            json={
                "name": name,
                "gpu_type": gpu_type,
                "gpu_count": gpu_count,
                "ssh_key": ssh_key,
                "operating_system_label": operating_system_label,
                "region": region,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(CreateInstanceResponse, _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(Message, _response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, instance_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InstanceResponse:
        """
        This endpoint is used to retrieve a single instance associated with the authenticated user by its ID.

        Parameters
        ----------
        instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InstanceResponse
            Successful Response

        Examples
        --------
        from FluidStack.client import AsyncFluidStack

        client = AsyncFluidStack(
            api_key="YOUR_API_KEY",
        )
        await client.instances.get(
            instance_id="{instance_id}",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"instances/{jsonable_encoder(instance_id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(InstanceResponse, _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(Message, _response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, instance_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        This endpoint is used to terminate an existing instance by its ID.

        Parameters
        ----------
        instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from FluidStack.client import AsyncFluidStack

        client = AsyncFluidStack(
            api_key="YOUR_API_KEY",
        )
        await client.instances.delete(
            instance_id="{instance_id}",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"instances/{jsonable_encoder(instance_id)}", method="DELETE", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(typing.Any, _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(Message, _response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def stop(
        self, instance_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListInstanceResponse:
        """
        This endpoint is used to stop an existing instance by its ID.

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
        )
        await client.instances.stop(
            instance_id="{instance_id}",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"instances/{jsonable_encoder(instance_id)}/stop", method="PUT", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ListInstanceResponse, _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(Message, _response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def start(
        self, instance_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListInstanceResponse:
        """
        This endpoint is used to start an existing instance by its ID.

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
        )
        await client.instances.start(
            instance_id="{instance_id}",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"instances/{jsonable_encoder(instance_id)}/start", method="PUT", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ListInstanceResponse, _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(Message, _response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
