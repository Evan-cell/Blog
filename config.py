import os

class Config:

    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:malcomiz0582@localhost/blog'


class ProdConfig(Config):
    uri = os.getenv("DATABASE_URL")  # or other relevant config var
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:malcomiz0582@localhost/blog'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}