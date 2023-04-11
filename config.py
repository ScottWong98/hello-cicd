import os

from dotenv import load_dotenv

load_dotenv()

FLASK_HOST = os.getenv('FLASK_HOST')
FLASK_PORT = os.getenv('FLASK_PORT')
