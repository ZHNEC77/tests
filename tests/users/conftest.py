import os
import requests
import pytest
from configuration import SERVICE_URL
from dotenv import load_dotenv


load_dotenv()
SERVICE_URL = os.getenv("SERVICE_URL")


@pytest.fixture
def get_users():
    response = requests.get(SERVICE_URL)
    return response
