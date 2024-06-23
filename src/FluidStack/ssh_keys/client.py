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
from ..types.http_validation_error import HttpValidationError
from ..types.message import Message
from ..types.ssh_key_response import SshKeyResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SshKeysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[SshKeyResponse]:
        """
        Fetch a list of SSH key names associated with the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SshKeyResponse]
            Successful Response

        Examples
        --------
        from FluidStack.client import FluidStack

        client = FluidStack(
            api_key="YOUR_API_KEY",
        )
        client.ssh_keys.list()
        """
        _response = self._client_wrapper.httpx_client.request("ssh_keys", method="GET", request_options=request_options)
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(typing.List[SshKeyResponse], _response.json())  # type: ignore
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
        self, *, name: str, public_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SshKeyResponse:
        """
        Create a new SSH key for the authenticated user.

        A unique name must be provided for the SSH key, along with a public key. The public key you provide is stored on your FluidStack account for use in SSH authentication.

        Supported public key formats: ssh-rsa, ssh-dss (DSA), ssh-ed25519, and ecdsa keys with NIST curves.

        Parameters
        ----------
        name : str
            The name of the SSH key.

        public_key : str
            The public key of the SSH key.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SshKeyResponse
            Successful Response

        Examples
        --------
        from FluidStack.client import FluidStack

        client = FluidStack(
            api_key="YOUR_API_KEY",
        )
        client.ssh_keys.create(
            name="my_ssh_key",
            public_key="<my_public_key>",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "ssh_keys",
            method="POST",
            json={"name": name, "public_key": public_key},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(SshKeyResponse, _response.json())  # type: ignore
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

    def delete(self, ssh_key_name: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete an existing SSH key by its name.

        Parameters
        ----------
        ssh_key_name : str

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
        )
        client.ssh_keys.delete(
            ssh_key_name="{ssh_key_name}",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ssh_keys/{jsonable_encoder(ssh_key_name)}", method="DELETE", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return
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


class AsyncSshKeysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[SshKeyResponse]:
        """
        Fetch a list of SSH key names associated with the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SshKeyResponse]
            Successful Response

        Examples
        --------
        from FluidStack.client import AsyncFluidStack

        client = AsyncFluidStack(
            api_key="YOUR_API_KEY",
        )
        await client.ssh_keys.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ssh_keys", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(typing.List[SshKeyResponse], _response.json())  # type: ignore
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
        self, *, name: str, public_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SshKeyResponse:
        """
        Create a new SSH key for the authenticated user.

        A unique name must be provided for the SSH key, along with a public key. The public key you provide is stored on your FluidStack account for use in SSH authentication.

        Supported public key formats: ssh-rsa, ssh-dss (DSA), ssh-ed25519, and ecdsa keys with NIST curves.

        Parameters
        ----------
        name : str
            The name of the SSH key.

        public_key : str
            The public key of the SSH key.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SshKeyResponse
            Successful Response

        Examples
        --------
        from FluidStack.client import AsyncFluidStack

        client = AsyncFluidStack(
            api_key="YOUR_API_KEY",
        )
        await client.ssh_keys.create(
            name="my_ssh_key",
            public_key="<my_public_key>",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ssh_keys",
            method="POST",
            json={"name": name, "public_key": public_key},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(SshKeyResponse, _response.json())  # type: ignore
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

    async def delete(self, ssh_key_name: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete an existing SSH key by its name.

        Parameters
        ----------
        ssh_key_name : str

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
        )
        await client.ssh_keys.delete(
            ssh_key_name="{ssh_key_name}",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ssh_keys/{jsonable_encoder(ssh_key_name)}", method="DELETE", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return
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
