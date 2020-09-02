from datetime import datetime
from functools import wraps

import simplejson
from flask import jsonify, request
from schematics.exceptions import DataError

from src.utils.redis import redis
from src.utils.settings import CACHE_BASE_UID

CACHE_EXPIRE_TIMEOUT = 60 * 60  # 1 hour


def validate_schema(schema_in):
    def validate(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                schema_obj = schema_in(request.json)
                schema_obj.validate()

                return fn(*args, **kwargs)
            except DataError as e:
                response = jsonify(e.to_primitive())
                response.status_code = 422
                return response

        return wrapper

    return validate


def cache(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        cache_name = f"{CACHE_BASE_UID}-OER"
        cache = redis.get(cache_name)
        if cache:
            parsed_cache = simplejson.loads(cache, use_decimal=True)
            if not should_update_forex(parsed_cache):
                return parsed_cache

        response = fn(*args, **kwargs)
        redis.setex(cache_name, CACHE_EXPIRE_TIMEOUT, simplejson.dumps(response, use_decimal=True))
        return response

    return wrapper


def should_update_forex(parsed_cache):
    last_forex = datetime.utcfromtimestamp(parsed_cache['timestamp'])
    if last_forex.hour != datetime.utcnow().hour:
        return True

    return False
