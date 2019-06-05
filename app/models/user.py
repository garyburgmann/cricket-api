import falcon
import sqlalchemy as sa
# from marshmallow import ValidationError

from app.models import RootModel
from app.serializers import UserSchema
from app.core import Paginator

 
class User(RootModel):
    __tablename__ = 'users'
    __schema__ = UserSchema

    id = sa.Column(
        sa.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = sa.Column(
        sa.String(100)
    )
    email = sa.Column(
        sa.String(100),
        unique=True
    )

    def json(self):
        return self.__schema__().dump(self)

    @classmethod
    def json_collection(cls, queryset, paginated=False, **kwargs):
        if paginated:
            paginator = Paginator(queryset=queryset, **kwargs)
            return paginator.response(schema=cls.__schema__(many=True))
        return dict(data=cls.__schema__(many=True).dump(data))

    @classmethod
    def create(cls, data):
        try:
            clean_data = cls.__schema__().load(data)
            user = cls(**clean_data)
            return user
        except Exception as exc:
            raise falcon.HTTPBadRequest(
                description=str(exc)
            )

    def update(self, data):
        try:
            clean_data = self.__schema__().load(data)
            for key, val in clean_data.items():
                setattr(self, key, val)
        except Exception as exc:
            raise falcon.HTTPBadRequest(
                description=str(exc)
            )
