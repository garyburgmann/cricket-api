import logging

from app import settings, db
from .users_seeder import UsersSeeder

log = logging.getLogger(__name__)

Session = db.get_session(settings.DB_URI)


def database_seeder(table=None):
    """Run migrations for all tables, or specified table"""
    if table == 'users':
        log.info('Seeding users table')
        UsersSeeder(Session).run()
