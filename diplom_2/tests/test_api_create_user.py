import allure
import requests
import pytest
from data.urls import TestCreatedUserAPI
from data.test_data import User,UserErrors


class TestCreateUserAPI:
    @allure.description('Регистрация уже существующего пользователя| POST | CREATE_LOGIN_URL')
    @allure.title('Сообщение- "пользователь уже существует", регистрация не пройдена.')
    def test_create_user_already_registered(self):
        payload= User.login_user
        response = requests.post(TestCreatedUserAPI.CREATE_LOGIN_URL, data=payload)
        assert response.status_code == 403
        assert response.json()['message'] == UserErrors.user_already_exist



    @allure.description('Регистрация пользователя:не заполнить одно из обязательных полей| POST | CREATE_LOGIN_URL')
    @allure.title('Получение сообщения "Email, password and name are required fields"')
    @pytest.mark.parametrize('user_data', (User.empty_password, User.only_password, User.empty_name,User.empty_email))
    def test_create_new_user_with_empty_data(self,user_data):
        response = requests.post(TestCreatedUserAPI.CREATE_LOGIN_URL, data=user_data)
        assert response.status_code == 403
        assert response.json()['message'] == UserErrors.required_fields




    @allure.description('Регистрация нового пользователя| POST | CREATE_LOGIN_URL')
    @allure.title('Регистрация прошла успешно')
    def test_create_new_user_success(self):
        payload = User.generate_new_user_for_register
        response = requests.post(TestCreatedUserAPI.CREATE_LOGIN_URL, data=payload)
        token = response.json()['accessToken']
        requests.delete(TestCreatedUserAPI.DELETE_USER_URL, headers={'Authorization': token})
        assert response.status_code == 200
        assert response.json()['success'] == True



    @allure.description('Авторизация существующего пользователя в системе| POST |AUTH_LOGIN_URL')
    @allure.title('Авторизация прошла успешно')
    def test_authorization_user_success(self):
        user_data = User.user_auth
        response = requests.post(TestCreatedUserAPI.AUTH_LOGIN_URL, data=user_data)
        assert response.status_code == 200


    @allure.description('Авторизация пользователя с неверным логином и паролем| POST |AUTH_LOGIN_URL')
    @allure.title('Сообщение об ошибке "email or password are incorrect"')
    def test_authorization_user_error_data(self):
        user_data = User.user_auth_incorrect_data
        response = requests.post(TestCreatedUserAPI.AUTH_LOGIN_URL, data=user_data)
        assert response.status_code == 401
        assert response.json()['message'] == UserErrors.incorrect_data


    @allure.description('Изменение данных пользователя без авторизации| PATCH |CHANGE_DATA_USER_URL')
    @allure.title('Сообщение об ошибке "You should be authorised"')
    @pytest.mark.parametrize('user_data', (User.create_email_user,User.create_password_user))
    def test_create_user_data_without_auth(self,user_data):
        response = requests.patch(TestCreatedUserAPI.CHANGE_DATA_USER_URL, data=user_data)
        assert response.status_code == 401
        assert response.json()['message'] == UserErrors.change_data_without_auth



    @allure.description('Изменение данных пользователя c авторизацией: изменить емеил| PATCH |CHANGE_DATA_USER_URL')
    @allure.title('Успешное обновление емеил, пароля')
    @pytest.mark.parametrize('user_data', (User.create_password_user,User.create_email_user))
    def test_create_user_data_with_auth_update_data(self,user_token,user_data):
        token = user_token
        payload = user_data
        response_create_data = requests.patch(TestCreatedUserAPI.CHANGE_DATA_USER_URL, headers={'Authorization': token},
                                              data = payload)
        assert response_create_data.status_code == 200
        assert response_create_data.json().get("success") is True




