import datetime

import sqlalchemy as sa


class TimestampMixin:
    """
    sqlalchemy TimestampMixin model adding
    created_at and updated_at columns
    """
    # timestamps
    created_at = sa.Column(
        sa.DateTime,
        default=datetime.datetime.utcnow
    )
    updated_at = sa.Column(
        sa.DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow
    )
