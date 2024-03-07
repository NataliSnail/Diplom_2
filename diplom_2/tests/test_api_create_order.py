import allure
import requests
import pytest
import random
from data.urls import TestCreatedUserAPI,TestCreatedOrderAPI
from data.test_data import User,Ingredient
from data.test_data import UserErrors,OrdersErrors
from data.test_data import *


class TestCreateOrderAPI:
    @allure.description('Тест создания заказа для авторизованного юзера + добавить ингредиенты| POST| CREATE_ORDER_URL')
    @allure.title('Успешное создание заказа')
    def test_create_new_order_with_auth(self,user_token):
        token = user_token
        payload = Ingredient.INGREDIENTS
        response_create_order = requests.post(TestCreatedOrderAPI.CREATE_ORDER_URL, headers={'Authorization': token}, data=payload)
        assert response_create_order.json()['success']==True
        assert response_create_order.status_code ==200



    @allure.description('Тест создания заказа без авторизации и  без добавления ингредиентов | POST| CREATE_ORDER_URL')
    @allure.title('Сообщение об ошибке "Ingredient ids must be provided"')
    def test_create_new_order_without_ingredient(self):
        payload= Ingredient.WITHOUT_INGREDIENTS
        response_create_order = requests.post(TestCreatedOrderAPI.CREATE_ORDER_URL, data=payload)
        assert OrdersErrors.create_order_without_ingredients in response_create_order.text
        assert response_create_order.status_code ==400


    @allure.description('Тест создания заказа для авторизованного юзера и с неверным хэшем | POST| CREATE_ORDER_URL')
    @allure.title('Сообщение об ошибке "Ingredient ids must be provided"')
    def test_create_new_order_without_ingredient(self,user_token):
        token = user_token
        payload = Ingredient.INCORRECT_INGREDIENTS
        response_create_order = requests.post(TestCreatedOrderAPI.CREATE_ORDER_URL,headers={'Authorization': token}, data=payload)
        assert OrdersErrors.error_500 in response_create_order.text
        assert response_create_order.status_code == 500




    @allure.description('Проверка получения заказов для авторизованного пользователя | GET | GET_ORDERS_USER_URL')
    @allure.title('Успешное получение заказа')
    def test_check_get_order_auth_user(self,user_token):
        token = user_token
        response = requests.get(TestCreatedOrderAPI.GET_ORDERS_USER_URL, headers={'Authorization': token})
        assert response.status_code == 200
        assert response.json()['success'] == True


    @allure.description('Проверка получения заказов для неавторизованного пользователя | GET | GET_ORDERS_USER_URL')
    @allure.title('Получение сообщения "You should be authorised"')
    def test_check_get_orders_without_auth(self):
        response_get_order = requests.get(TestCreatedOrderAPI.GET_ORDERS_USER_URL)
        assert OrdersErrors.get_order__without_auth in response_get_order.text
        assert response_get_order.status_code == 401