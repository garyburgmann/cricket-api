import sqlalchemy as sa

from app.models import RootModel
from app.serializers import UserSchema

 
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
        return self.__schema__().dump(self).data

    @classmethod
    def json_collection(cls, data):
        return cls.__schema__(many=True).dump(data).data
