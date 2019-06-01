import sqlalchemy as sa
from marshmallow import ValidationError

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
        return self.__schema__().dump(self).data

    @classmethod
    def json_collection(cls, queryset, paginated=False, **kwargs):
        if paginated:
            paginator = Paginator(queryset=queryset, **kwargs)
            return paginator.response(schema=cls.__schema__(many=True))
        return dict(data=cls.__schema__(many=True).dump(data).data)

    @classmethod
    def create(cls, session, data):
        try:
            clean_data = cls.__schema__().load(data).data
            user = cls(**clean_data)
            session.add(user)
            session.flush()
            return user
        except ValidationError as exc:
            raise ValidationError(str(exc))
        except sa.exc.IntegrityError as exc:
            raise ValidationError(str(exc))
