from logging import DEBUG
import os
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

PORT = int(os.getenv('PORT'))
HOST = os.getenv('HOST')
DEBUG_MODE = os.getenv("DEBUG_MODE")
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")


