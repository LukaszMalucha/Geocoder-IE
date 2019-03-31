from werkzeug.security import safe_str_cmp
from user import User


users = [
    User(1, 'bob', 'asd')

]

# Set comprehension
username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    """"User Authentication"""
    user = username_mapping.get(username, None)
    # for Python 2.7
    if user and safe_str_cmp(user.password , password):
        return user


def identity(payload):
    """Get user identity after receiving JWT Token"""
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
