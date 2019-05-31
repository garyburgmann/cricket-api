import uuid

import sqlalchemy as sa
from sqlalchemy_utils import UUIDType


def get_uuid():
    return str(uuid.uuid4().hex)


class UUIDMixin:
    """
    sqlalchemy UUIDMixin model adding
    UUID column
    """
    uuid = sa.Column(
        UUIDType(binary=False),
        unique=True,
        default=get_uuid
    )
