from app.models import Base, TimestampMixin, UUIDMixin

class RootModel(Base, TimestampMixin, UUIDMixin):
    __abstract__ = True
