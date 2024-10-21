from unittest.mock import patch,Mock
from fastapi.testclient import TestClient
import pytest
from utils import classes
import requests
from test import test


# test for methods of class

@pytest.fixture
def random_generator_obj():
    return classes.RandomNameGenerator('nepali','nepal','male')

@pytest.fixture
def mock_get():
    with patch('requests.get') as mock_get:
        yield mock_get

mock_response=test.mock_response
def test_make_api_call(random_generator_obj,mock_response):
    assert random_generator_obj.make_api_call()=="random_nepali"

def test_make_appropriate_url(random_generator_obj):
    assert random_generator_obj.make_appropriate_url()=="https://api.namefake.com/nepali-nepal/male/"


def test_request_timeoutError(random_generator_obj, mock_get):
    mock_get.side_effect = requests.exceptions.Timeout
    with pytest.raises(classes.APIException):
        random_generator_obj.make_api_call()


def test_request_connectionError(random_generator_obj, mock_get):
    mock_get.side_effect = requests.exceptions.ConnectionError
    with pytest.raises(classes.APIException):
        random_generator_obj.make_api_call()