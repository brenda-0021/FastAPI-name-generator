from unittest.mock import patch,Mock
from fastapi.testclient import TestClient
from main import app
import pytest


# generate mock
@pytest.fixture
def mock_response():
    with patch('requests.get') as mock_get:
        mock_response=Mock()
        mock_response.status_code = 200
        mock_response.json.return_value={"name": "random_nepali"}
        mock_get.return_value = mock_response
        yield mock_get


# test for main.py
@pytest.fixture
def client():
    return TestClient(app)


payload={
    "nationality":"nepali",
    "country": "nepal",
    "gender":"male"
}

def test_generate_random_name(client,mock_response):
    response=client.get('/generate',params=payload)
    assert response.status_code == 200
    assert response.json()['random_name']=="random_nepali"







    

