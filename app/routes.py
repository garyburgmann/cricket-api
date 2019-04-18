"""
Module for route declarations
"""
from app import api, resources

api.add_route('/matches', resources.MatchResource())
api.add_route('/matches/{oid}', resources.MatchDetailResource())
