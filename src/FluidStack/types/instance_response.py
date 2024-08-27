# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .configuration_instance_response import ConfigurationInstanceResponse
from .instance_status import InstanceStatus


class InstanceResponse(pydantic_v1.BaseModel):
    id: str = pydantic_v1.Field()
    """
    The unique identifier of the instance.
    """

    status: typing.Optional[InstanceStatus] = pydantic_v1.Field(default=None)
    """
    The current status of the instance.
    """

    username: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    The username used to connect to the instance. For example, to connect to the instance via SSH, use: "ssh -i <path/to/private/key> <username>@<ip_address>".
    """

    ssh_port: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    The SSH port used to connect to the instance.
    """

    ssh_keys: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    The names of the SSH keys used to login to the instance.
    """

    ip_address: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    The IP address of the instance.
    """

    name: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    The name provided when the instance was created.
    """

    current_rate: typing.Optional[float] = pydantic_v1.Field(default=None)
    """
    The current hourly price of the instance per processor based on its current status.
    """

    configuration: typing.Optional[ConfigurationInstanceResponse] = pydantic_v1.Field(default=None)
    """
    The configuration used to create the instance.
    """

    created_at: typing.Optional[dt.datetime] = pydantic_v1.Field(default=None)
    """
    The creation date and time of the instance.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
