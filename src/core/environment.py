import os

from dotenv import load_dotenv

load_dotenv()


class Environment:
    base_url = os.getenv("BASE_URL")
