from dotenv import load_dotenv
import os


load_dotenv()


class Config:
    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT = int(os.getenv("REDIS_PORT"))
    CACHE_SECONDS = int(os.getenv("CACHE_SECONDS"))



config = Config()