from app.models import Base, TimestampMixin, UUIDMixin

class RootModel(Base, UUIDMixin, TimestampMixin):
    __abstract__ = True
