"""
Module housing resource handlers for match collection and detail endpoints
"""
import falcon
from bson.json_util import dumps


class MatchResource:

    def on_get(self, req, resp):
        collection = self.db.matches
        resp.body = dumps(collection.find())
    
    def on_post(self, req, resp):
        collection = self.db.matches
        match = {
            'team': req.media.get('team'),
            'opponent': req.media.get('opponent')
        }
        match_id = collection.insert_one(match).inserted_id
        match = collection.find_one(match_id)
        resp.status = falcon.HTTP_CREATED
        resp.body = dumps(match)


class MatchDetailResource:

    def on_get(self, req, resp, oid):
        collection = self.db.matches
        match = collection.find_one({'_id': self.object_id})
        if not match:
            raise falcon.HTTPNotFound(
                description='Item not found'
            )
        resp.body = dumps(match)
    
    def on_put(self, req, resp, oid):
        collection = self.db.matches
        # collection.update_one(
        #     {'_id': self.object_id},
        #     {'$set': req.media},
        #     upsert=True
        # )
        collection.replace_one(
            {'_id': self.object_id},
            req.media,
            # upsert=True
        )
        match = collection.find_one(self.object_id)
        if not match:
            raise falcon.HTTPNotFound(
                description='Item not found'
            )
        resp.body = dumps(match)

    def on_delete(self, req, resp, oid):
        collection = self.db.matches
        collection.delete_one(
            {'_id': self.object_id},
        )
        resp.status = falcon.HTTP_NO_CONTENT
