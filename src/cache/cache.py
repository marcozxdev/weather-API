

from src.cache.client_redis import client, config
from redis import Redis
import json





class Cache:
    def __init__(self, client: Redis):
        self.client = client


    
    def set(self, key, value, expire=config.CACHE_SECONDS):
        return self.client.set(key=key, value=json.dumps(value), ex=expire)


    def get(self, key):
       
       cached = self.client.get(key)

       if cached is None:
          return None
       
       return json.loads(cached)
    

    def delete(self, key):
        return self.client.delete(key=key)
    

    def exists(self, key):
        return self.client.exists(key=key)
    

    def  ttl(self, key):
        return self.client.ttl(key=key)
    

    





redis_cache = Cache(client=client)












