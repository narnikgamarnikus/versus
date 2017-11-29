from functools import wraps
from annoying.functions import get_object_or_None
from versus.users.models import User
from django.core.cache import cache


def path_token(func):

    @wraps(func)
    def inner(message, *args, **kwargs):

        last_path_item = args[0].content['path'].split("/")[-1]
        split_last_item = last_path_item.split('=')
        
        if split_last_item.count('token') == 1:
            token = split_last_item[1]
            if token:
                args[0].token = token
            else:
                raise ValueError('Token was not set')
        elif split_last_item.count('token') > 1:
            raise ValueError('More than one token specified')
        else:
            raise ValueError('Token was not set in the path')
        
        return func(message, *args, **kwargs)

    return inner


def path_token_user(func):

    @path_token
    @wraps(func)
    def inner(message, *args, **kwargs):
        if hasattr(args[0], 'token'):
            token = args[0].token
            user = cache.get(token)
            if not user:
                user = get_object_or_None(User, token=token)
                cache.set(user.token, user)
            if not args[0].user is user:
                args[0].user = user
        return func(message, *args, **kwargs)

    return inner    