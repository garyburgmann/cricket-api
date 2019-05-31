"""
Module housing resource handlers for User collection and detail endpoints
"""
# import logging
import json

import falcon
from sqlalchemy import orm

from app.resources import BaseDetailResource, BaseResource
from app.models import User

# log = logging.getLogger(__name__)


class UserResource(BaseResource):
    __collection__ = 'users'

    def on_get(self, req, resp):
        users = self.session.query(User).all()
        # log.info('Users list')
        resp.media = {
            'data': User.json_collection(users)
        }

class UserDetailResource:
    __collection__ = 'users'

    def on_get(self, req, resp, oid):
        # log.info('Users retrieve')
        try:
            user = self.session.query(User).filter(User.uuid == oid).one()
        except orm.exc.NoResultFound:
            raise falcon.HTTPNotFound(
                description='Item not found'
            )
        resp.media = user.json()

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
