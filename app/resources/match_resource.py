"""
Module housing resource handlers for Match collection and detail endpoints
"""
import falcon
from bson.json_util import dumps

from app.resources import BaseResource, BaseDetailResource


class MatchResource(BaseResource):
    __collection__ = 'matches'


class MatchDetailResource(BaseDetailResource):
    __collection__ = 'matches'
