# """
# Module housing resource handlers for Team collection and detail endpoints
# """
# import falcon
# from bson.json_util import dumps

# from app.resources import BaseResource, BaseDetailResource


# class TeamResource(BaseResource):
#     __collection__ = 'teams'

#     def on_get(self, req, resp):
#         if 'user' in req.params:
#             data = dumps(self.collection.find({'user': req.params['user']}))
#         else:
#             data = dumps(self.collection.find())
#         resp.body = data


# class TeamDetailResource(BaseDetailResource):
#     __collection__ = 'teams'
