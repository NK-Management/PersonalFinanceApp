from flask_caching import Cache
from user_service.config import Config

cache = Cache()

def init_cache(app):
    """
    Initializes the caching system using Redis or the default type.
    """
    app.config["CACHE_TYPE"] = Config.CACHE_TYPE
    app.config["CACHE_REDIS_URL"] = Config.get_redis_url()  # Assuming this method exists in your config.
    app.config["CACHE_DEFAULT_TIMEOUT"] = Config.CACHE_DEFAULT_TIMEOUT
    cache.init_app(app)

def cache_token(user_id, token):
    """
    Caches the JWT token for a specific user.
    """
    cache.set(f"user_token_{user_id}", token)

def invalidate_token(user_id):
    """
    Invalidates the cached token by removing it from the cache.
    """
    cache.delete(f"user_token_{user_id}")
    