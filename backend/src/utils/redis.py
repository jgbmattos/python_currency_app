from redis import Redis, ConnectionPool
from src.utils.settings import REDIS_HOST, REDIS_PORT

redis = Redis(
    connection_pool=ConnectionPool(
            host=REDIS_HOST,
            port=REDIS_PORT,
            db=0,
    )
)