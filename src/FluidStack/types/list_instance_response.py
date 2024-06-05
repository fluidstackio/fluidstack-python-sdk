# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .configuration_response import ConfigurationResponse
from .instance_status import InstanceStatus
from .instance_term import InstanceTerm
from .operating_system_response import OperatingSystemResponse
from .region_response import RegionResponse
from .ssh_key_response import SshKeyResponse


class ListInstanceResponse(pydantic_v1.BaseModel):
    id: str = pydantic_v1.Field()
    """
    The unique identifier of the instance.
    """

    status: typing.Optional[InstanceStatus] = pydantic_v1.Field(default=None)
    """
    The current status of the instance.
    """

    username: typing.Optional[str] = None
    ssh_port: typing.Optional[str] = None
    ssh_keys: typing.Optional[typing.List[SshKeyResponse]] = None
    ip_address: typing.Optional[str] = None
    name: typing.Optional[str] = None
    term: typing.Optional[InstanceTerm] = pydantic_v1.Field(default=None)
    """
    The commitment term of the instance.
    """

    current_rate: typing.Optional[float] = None
    configuration: typing.Optional[ConfigurationResponse] = None
    region: typing.Optional[RegionResponse] = None
    operating_system: typing.Optional[OperatingSystemResponse] = None
    created_at: typing.Optional[dt.datetime] = None

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