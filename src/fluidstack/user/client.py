# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .ssh_keys.client import AsyncSshKeysClient, SshKeysClient


class UserClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.ssh_keys = SshKeysClient(client_wrapper=self._client_wrapper)


class AsyncUserClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.ssh_keys = AsyncSshKeysClient(client_wrapper=self._client_wrapper)
