"""
Module housing resource handlers for User collection and detail endpoints
"""
import falcon
from bson.json_util import dumps

from app.resources import BaseDetailResource, BaseResource


class UserResource(BaseResource):
    __collection__ = 'users'


class UserDetailResource(BaseDetailResource):
    __collection__ = 'users'


class UserRelationResource(BaseDetailResource):
    __collection__ = 'users'
    __relations__ = ['teams', 'matches']

    def on_get(self, req, resp, oid, relation):
        item = self.collection.find_one({'_id': self.object_id})
        if not item:
            raise falcon.HTTPNotFound(
                description='Item not found'
            )

        if relation not in self.__relations__:
            raise falcon.HTTPNotFound(
                description='Item relationship not found'
            )

        teams = self.db['teams'].find({'user': oid})
        if relation == 'teams':
            resp.body = dumps(teams)

        team_ids = [str(x['_id']) for x in teams]
        matches = self.db['matches'].find(
            {
                'team': {
                    '$in': team_ids
                }
            }
        )
        if relation == 'matches':
            resp.body = dumps(matches)
