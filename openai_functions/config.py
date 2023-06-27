import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

AUTHORIZATION = f"Bearer {os.getenv('OPENAI_API_KEY')}"
BASE_URL = 'https://api.openai.com/v1'
