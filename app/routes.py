"""
Module for route declarations
"""
from app import api, resources

api.add_route('/teams', resources.TeamResource())
api.add_route('/teams/{oid}', resources.TeamDetailResource())
api.add_route('/matches', resources.MatchResource())
api.add_route('/matches/{oid}', resources.MatchDetailResource())
