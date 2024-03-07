import pytest
import requests
from data.test_data import User
from data.urls import TestCreatedUserAPI


@pytest.fixture
def user_token():
    payload = User.generate_new_user_for_register
    response = requests.post(TestCreatedUserAPI.CREATE_LOGIN_URL, data=payload)
    token = response.json()['accessToken']

    yield token
    requests.delete(TestCreatedUserAPI.DELETE_USER_URL, headers={'Authorization': token})