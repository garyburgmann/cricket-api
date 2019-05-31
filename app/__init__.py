"""
Root module for the application containing WSGI instance
"""
import falcon

from app import (
    settings,
    db,
    middleware
)

Session = db.get_session(settings.DB_URI)

api = falcon.API(middleware=[
    middleware.SQLAlchemySessionManager(Session)
])

# avoid circular imports
from app import routes
