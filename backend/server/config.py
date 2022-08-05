import os

from dotenv import load_dotenv

load_dotenv()

def get_api_port():
    return '3001'


def get_website_port():
    return '3000'


def get_website_domain():
    return 'http://localhost:' + get_website_port()

def get_postgres_uri():
    host = os.environ.get("DB_HOST", "localhost")
    port = 5433 if host == "localhost" else 5432
    password = os.environ.get("DB_PASSWORD", "abc123")
    user, db_name = "aqualog", "aqualog"
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"