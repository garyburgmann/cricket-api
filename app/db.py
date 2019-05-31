"""
Module for initiating DB connection
"""
from sqlalchemy import create_engine, orm

from app import settings


def get_session(uri=settings.DB_URI):
    engine = create_engine(uri, pool_pre_ping=True)
    session_factory = orm.sessionmaker(bind=engine)
    Session = orm.scoped_session(session_factory)
    return Session
