# This file was auto-generated by Fern from our API Definition.

import os
import typing

import httpx

from .configurations.client import AsyncConfigurationsClient, ConfigurationsClient
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .instances.client import AsyncInstancesClient, InstancesClient
from .ssh_keys.client import AsyncSshKeysClient, SshKeysClient
from .templates.client import AsyncTemplatesClient, TemplatesClient


class FluidStack:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    api_key : typing.Optional[str]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests by default the timeout is 60 seconds, unless a custom httpx client is used, in which case a default is not set.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from FluidStack.client import FluidStack

    client = FluidStack(
        api_key="YOUR_API_KEY",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        api_key: typing.Optional[str] = os.getenv("FLUIDSTACK_API_KEY"),
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        self._client_wrapper = SyncClientWrapper(
            base_url=base_url,
            api_key=api_key,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.instances = InstancesClient(client_wrapper=self._client_wrapper)
        self.ssh_keys = SshKeysClient(client_wrapper=self._client_wrapper)
        self.configurations = ConfigurationsClient(client_wrapper=self._client_wrapper)
        self.templates = TemplatesClient(client_wrapper=self._client_wrapper)


class AsyncFluidStack:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    api_key : typing.Optional[str]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests by default the timeout is 60 seconds, unless a custom httpx client is used, in which case a default is not set.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from FluidStack.client import AsyncFluidStack

    client = AsyncFluidStack(
        api_key="YOUR_API_KEY",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        api_key: typing.Optional[str] = os.getenv("FLUIDSTACK_API_KEY"),
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        self._client_wrapper = AsyncClientWrapper(
            base_url=base_url,
            api_key=api_key,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.instances = AsyncInstancesClient(client_wrapper=self._client_wrapper)
        self.ssh_keys = AsyncSshKeysClient(client_wrapper=self._client_wrapper)
        self.configurations = AsyncConfigurationsClient(client_wrapper=self._client_wrapper)
        self.templates = AsyncTemplatesClient(client_wrapper=self._client_wrapper)