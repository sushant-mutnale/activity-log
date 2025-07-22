import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:pass@localhost:5432/db')
SECRET_KEY = os.getenv('SECRET_KEY', 'supersecret')
