import sqlalchemy as sa
from sqlalchemy_utils import UUIDType


class UUIDMixin:
    """
    sqlalchemy UUIDMixin model adding
    UUID column
    """
    uuid = sa.Column(UUIDType(binary=False), primary_key=True)
