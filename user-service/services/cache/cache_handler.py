from flask_caching import Cache
from config import Config

cache = Cache()

def init_cache(app):
    """
    Initializes the caching system using Redis or the default type.
    """
    app.config["CACHE_TYPE"] = Config.CACHE_TYPE
    app.config["CACHE_REDIS_URL"] = Config.get_redis_url()
    app.config["CACHE_DEFAULT_TIMEOUT"] = Config.CACHE_DEFAULT_TIMEOUT
    cache.init_app(app)
