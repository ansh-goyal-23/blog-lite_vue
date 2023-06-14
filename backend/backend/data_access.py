from .models import User, Post
# from flask import Flask
from . import cache

@cache.cached(timeout=20, key_prefix='get_all_users')
def get_all_users():
    users = User.query.all()
    return users

@cache.memoize(50)
def get_posts_by_user(userid):
    # users = User.query.all()
    # return users
    pass