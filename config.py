import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")

load_dotenv(ENV_PATH)

def get_database_uri():
    username = os.environ["MYSQL_USERNAME"]
    password = os.environ["MYSQL_PASSWORD"]
    host = os.environ["MYSQL_HOST"]
    database = os.environ["MYSQL_DATABASE"]
    # mysql://flask:fc592aOQNImA8ynL@127.0.0.1/flask
    return f"mysql://{username}:{password}@{host}/{database}"

class Config(object):
    SQLALCHEMY_DATABASE_URI = get_database_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
