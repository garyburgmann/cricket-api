"""
Module for initiating DB connection
"""
from sqlalchemy import create_engine, orm

from app import settings

engine = create_engine(settings.DB_URI, pool_pre_ping=True)

session_factory = orm.sessionmaker(bind=engine)
Session = orm.scoped_session(session_factory)
