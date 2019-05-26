import sqlalchemy as sa

from app.models import RootModel

 
class User(RootModel):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(100))
