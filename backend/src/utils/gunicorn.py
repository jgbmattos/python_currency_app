from src.utils.settings import HOST, PORT

bind = f'{HOST}:{PORT}'
workers = 2
worker_class = 'gevent'
keepalive = 10
