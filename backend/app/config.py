from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

class Config:
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
    FIREBASE_API_KEY = os.getenv('FIREBASE_API_KEY')
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')
    HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')
    REPLICATE_API_KEY = os.getenv('REPLICATE_API_KEY')