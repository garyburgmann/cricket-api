from manager import Manager

from app.database.seeds import database_seeder

manager = Manager()


@manager.command
def dbseed(table=None):
    """Run database seeders"""
    database_seeder(table)


if __name__ == '__main__':
    manager.main()
