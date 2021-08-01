import time
import logging
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='192.168.1.110', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    # app.logger.debug("I'm a DEBUG message")
    # app.logger.error("I'm a ERROR message")
    # app.logger.info("I'm an INFO message")
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
