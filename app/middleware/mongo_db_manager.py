"""
Module to attach a Mongo client and db instance to each resource as middleware
"""
import falcon
from bson.objectid import ObjectId
from bson.errors import InvalidId


class MongoDBManager:
    """
    Attach a db instance to every request
    """
    def __init__(self, client):
        self._client = client
        self._db = client.cricket

    def process_resource(self, req, resp, resource, params):
        resource.client = self._client
        resource.db = self._db
        if hasattr(resource, '__collection__'):
            resource.collection = resource.db[resource.__collection__]
        if params.get('oid'):
           resource.object_id = self.get_object_id(params['oid'])

    def get_object_id(self, oid):
        try:
            return ObjectId(oid)
        except InvalidId as exc:
            raise falcon.HTTPBadRequest(
                description=f'Invalid ObjectId: {str(exc)}'
            )
    # def process_response(self, req, resp, resource, req_succeeded):
    #     if hasattr(resource, 'session'):
    #         Session.remove()