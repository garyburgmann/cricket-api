"""
Module for handling the users table seeder
"""
from app import models


class UsersSeeder:
    """
    Class for seeding users
    """
    def __init__(self, Session):
        self.Session = Session
    def run(self):
        session = self.Session()
        session.query(models.User).delete()
        user = models.User(
            name='Gary Burgmann',
            email="garyburgmann@gmail.com"
        )
        session.add(user)
        session.commit()
        self.Session.remove()
