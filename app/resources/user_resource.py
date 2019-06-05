"""
Module housing resource handlers for User collection and detail endpoints
"""
# import logging

import falcon
import sqlalchemy as sa

from app.resources import BaseDetailResource, BaseResource
from app.models import User

# log = logging.getLogger(__name__)


class UserResource(BaseResource):

    def on_get(self, req, resp):
        queryset = self.session.query(User)

        resp.media = User.json_collection(
            queryset,
            paginated=True,
            **req.params
        )

    def on_post(self, req, resp):
        existing_email = self.session.query(User) \
            .filter(User.email == f"{req.media.get('email')}") \
            .one_or_none()
        if existing_email:
            raise falcon.HTTPBadRequest(
                description='Email already exists'
            )
        user = User.create(req.media)
        try:
            self.session.add(user)
            self.session.commit()
        except Exception as exc:
            raise falcon.HTTPBadRequest(
                description=str(exc)
            )

        resp.status = falcon.HTTP_CREATED
        resp.media = user.json()


class UserDetailResource:

    def on_get(self, req, resp, pk):
        try:
            user = self.session.query(User).filter(User.uuid == pk).one()
        except sa.orm.exc.NoResultFound:
            raise falcon.HTTPNotFound(
                description='Item not found'
            )
        resp.media = user.json()

    def on_put(self, req, resp, pk):
        try:
            user = self.session.query(User).filter(User.uuid == pk).one()
        except sa.orm.exc.NoResultFound:
            raise falcon.HTTPNotFound(
                description='Item not found'
            )
        existing_email = self.session.query(User) \
            .filter(
                User.email == f"{req.media.get('email')}",
                User.uuid != user.uuid
            ) \
            .one_or_none()
        if existing_email:
            raise falcon.HTTPBadRequest(
                description='Email already exists'
            )
        user.update(req.media)
        try:
            self.session.add(user)
            self.session.commit()
        except Exception as exc:
            raise falcon.HTTPBadRequest(
                description=str(exc)
            )
        resp.media = user.json()

    def on_delete(self, req, resp, pk):
        try:
            user = self.session.query(User).filter(User.uuid == pk).one()
        except sa.orm.exc.NoResultFound:
            raise falcon.HTTPNotFound(
                description='Item not found'
            )
        self.session.query(User).filter(User.uuid == pk) \
            .delete()
        self.session.commit()
        resp.status = falcon.HTTP_NO_CONTENT

# class UserRelationResource(BaseDetailResource):
#     __collection__ = 'users'
#     __relations__ = ['teams', 'matches']

#     def on_get(self, req, resp, oid, relation):
#         item = self.collection.find_one({'_id': self.object_id})
#         if not item:
#             raise falcon.HTTPNotFound(
#                 description='Item not found'
#             )

#         if relation not in self.__relations__:
#             raise falcon.HTTPNotFound(
#                 description='Item relationship not found'
#             )

#         teams = self.db['teams'].find({'user': oid})
#         if relation == 'teams':
#             resp.body = dumps(teams)

#         team_ids = [str(x['_id']) for x in teams]
#         matches = self.db['matches'].find(
#             {
#                 'team': {
#                     '$in': team_ids
#                 }
#             }
#         )
#         if relation == 'matches':
#             resp.body = dumps(matches)
