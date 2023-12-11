from flask_sqlalchemy import SQLAlchemy

class Config:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DatabaseConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:my_password@127.0.0.1:3306/hostaldb'

db = SQLAlchemy()