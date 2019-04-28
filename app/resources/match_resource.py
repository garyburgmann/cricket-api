"""
Module housing resource handlers for Match collection and detail endpoints
"""
import falcon
from bson.json_util import dumps

from app.resources import BaseResource, BaseDetailResource


class MatchResource(BaseResource):
    __collection__ = 'matches'

    def on_get(self, req, resp):
        if 'team' in req.params:
            data = dumps(self.collection.find({'team': req.params['team']}))
        else:
            data = dumps(self.collection.find())
        resp.body = data


class MatchDetailResource(BaseDetailResource):
    __collection__ = 'matches'
