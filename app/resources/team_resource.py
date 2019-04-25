"""
Module housing resource handlers for Team collection and detail endpoints
"""
import falcon
from bson.json_util import dumps

from app.resources import BaseResource, BaseDetailResource


class TeamResource(BaseResource):
    __collection__ = 'teams'


class TeamDetailResource(BaseDetailResource):
    __collection__ = 'teams'
