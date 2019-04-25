"""
Module housing resource handlers for Base collection and detail endpoints
"""
import falcon
from bson.json_util import dumps


class CollectionMixin:
    """
    Mixin class to enforce the presence of the __collection__ property on
    declared resource classes
    """
    @property
    def __collection__(self):
        raise falcon.HTTPNotImplemented(
            description='__collection__ property missing on Class: '
                        f'{self.__class__.__name__}'
        )


class BaseResource(CollectionMixin):
    """
    Base resource handler for list and create endpoints
    """
    def on_get(self, req, resp):
        resp.body = dumps(self.collection.find())
    
    def on_post(self, req, resp):
        item = req.media
        item_id = self.collection.insert_one(item).inserted_id
        item = self.collection.find_one(item_id)
        resp.status = falcon.HTTP_CREATED
        resp.body = dumps(item)


class BaseDetailResource(CollectionMixin):
    """
    Base resource handler for retrieve, update and destroy endpoints
    """
    def on_get(self, req, resp, oid):
        item = self.collection.find_one({'_id': self.object_id})
        if not item:
            raise falcon.HTTPNotFound(
                description='Item not found'
            )
        resp.body = dumps(item)
    
    def on_put(self, req, resp, oid):
        # collection.update_one(
        #     {'_id': self.object_id},
        #     {'$set': req.media},
        #     upsert=True
        # )
        self.collection.replace_one(
            {'_id': self.object_id},
            req.media,
            # upsert=True
        )
        item = self.collection.find_one(self.object_id)
        if not item:
            raise falcon.HTTPNotFound(
                description='Item not found'
            )
        resp.body = dumps(item)

    def on_delete(self, req, resp, oid):
        self.collection.delete_one(
            {'_id': self.object_id},
        )
        resp.status = falcon.HTTP_NO_CONTENT
