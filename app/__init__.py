"""
Root module for the application containing WSGI instance
"""
import falcon

from app import (
    settings,
    mongo,
    middleware
)

api = falcon.API(middleware=[
    middleware.MongoDBManager(mongo.client),
])

# avoid circular imports
from app import routes
