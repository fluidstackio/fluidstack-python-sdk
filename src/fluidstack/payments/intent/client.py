# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.query_encoder import encode_query
from ...core.remove_none_from_dict import remove_none_from_dict
from ...core.request_options import RequestOptions
from ...errors.unauthorized_error import UnauthorizedError
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.create_payment_response import CreatePaymentResponse
from ...types.currency_type import CurrencyType
from ...types.http_validation_error import HttpValidationError
from ...types.message import Message

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class IntentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self,
        *,
        amount: int,
        currency: typing.Optional[CurrencyType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatePaymentResponse:
        """
        Create a new payment intent.

        Parameters
        ----------
        amount : int

        currency : typing.Optional[CurrencyType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatePaymentResponse
            Successful Response

        Examples
        --------
        from fluidstack.client import FluidStack

        client = FluidStack(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.payments.intent.create(
            amount=1,
        )
        """
        _request: typing.Dict[str, typing.Any] = {"amount": amount}
        if currency is not OMIT:
            _request["currency"] = currency
        _response = self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "payments/create-intent"),
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
            return pydantic_v1.parse_obj_as(CreatePaymentResponse, _response.json())  # type: ignore
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


class AsyncIntentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self,
        *,
        amount: int,
        currency: typing.Optional[CurrencyType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatePaymentResponse:
        """
        Create a new payment intent.

        Parameters
        ----------
        amount : int

        currency : typing.Optional[CurrencyType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatePaymentResponse
            Successful Response

        Examples
        --------
        from fluidstack.client import AsyncFluidStack

        client = AsyncFluidStack(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.payments.intent.create(
            amount=1,
        )
        """
        _request: typing.Dict[str, typing.Any] = {"amount": amount}
        if currency is not OMIT:
            _request["currency"] = currency
        _response = await self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "payments/create-intent"),
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
            return pydantic_v1.parse_obj_as(CreatePaymentResponse, _response.json())  # type: ignore
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
