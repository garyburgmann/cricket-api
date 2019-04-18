"""
Module for instantation of MongoDB connection
"""
from pymongo import MongoClient

from app import settings

client = MongoClient(settings.MONGO_URI)
