"""
Root module for the application containing WSGI instance
"""
import falcon

from app import (
    settings,
    mongo,
    db,
    middleware
)

api = falcon.API(middleware=[
    middleware.MongoDBManager(mongo.client),
    middleware.SQLAlchemySessionManager(db.Session)
])

# avoid circular imports
from app import routes
