import os

class Config:
    """Configuration settings for the Flask application."""
    SECRET_KEY = os.environ.get("SECRET_KEY", "a-super-secret-key")
    SQLALCHEMY_DATABASE_URI = "sqlite:///smartclassroom.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False