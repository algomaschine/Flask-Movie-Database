import base64
import hashlib
import hmac
import datetime
import calendar
import jwt

from flask import abort, request
from project.config import BaseConfig

config = BaseConfig()


def _get_password_hash(password):
    """
    Hashes the password.
    """
    password = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        config.PWD_HASH_SALT,
        config.PWD_HASH_ITERATIONS
    )

    return base64.b64encode(password).decode("utf-8", "ignore")


def _compare_passwords(password_hash, entered_password):
    """
    Compares the sent password with a user's password in a database.
    """
    password = base64.b64decode(password_hash)

    new_hash = hashlib.pbkdf2_hmac(
        'sha256',
        entered_password.encode('utf-8'),
        config.PWD_HASH_SALT,
        config.PWD_HASH_ITERATIONS
    )

    return hmac.compare_digest(password, new_hash)


def _generate_tokens(id, password):
    """
    Generates a pair of access + refresh tokens for a user.
    """
    data = {
        "id": id,
            "password": password,
    }

    min30 = datetime.datetime.utcnow(
    ) + datetime.timedelta(minutes=config.TOKEN_EXPIRE_MINUTES)
    data["exp"] = calendar.timegm(min30.timetuple())
    data["type"] = "access_token"
    access_token = jwt.encode(
        data, config.SECRET_KEY, algorithm=config.JWT_ALGORITHM)

    days130 = datetime.datetime.utcnow() + datetime.timedelta(days=config.TOKEN_EXPIRE_DAYS)
    data["exp"] = calendar.timegm(days130.timetuple())
    data["type"] = "refresh_token"
    refresh_token = jwt.encode(
        data, config.SECRET_KEY, algorithm=config.JWT_ALGORITHM)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }


def _approve_refresh_token(refresh_token):
    """
    Checks the user's refresh token, in case of success
    returns a new pair of tokens.
    """
    data = jwt.decode(jwt=refresh_token, key=config.SECRET_KEY,
                        algorithms=[config.JWT_ALGORITHM])
    uid = data.get("id")
    password = data.get("password")

    tokens = _generate_tokens(uid, password)
    return tokens


def auth_required(func):
    """
    A wrapper for the endpoint that allows only
    authenticated users to access the endpoint.
    """
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401, description='Unauthorized')

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            jwt.decode(token, key=config.SECRET_KEY,
                        algorithms=[config.JWT_ALGORITHM])
        except Exception as e:
            print('JWT Decode Exception', e)
            abort(401, description='Unauthorized')

        return func(*args, **kwargs)

    return wrapper
