"""
Root resources module
"""
from .base_resource import BaseResource, BaseDetailResource
# from .match_resource import MatchResource, MatchDetailResource
# from .team_resource import TeamResource, TeamDetailResource
from .user_resource import (
    UserResource,
    UserDetailResource,
    # UserRelationResource
)
