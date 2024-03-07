import random
from faker import Faker


class User:
    faker = Faker()

    generate_new_user_for_register = {
        "email": faker.email(),
        "password": faker.random_int(100000, 999999),
        "name": faker.name()
    }

    login_user = {
        "email": "car123@mail.ru",
        "password": "123456",
        "name": "Cat"
    }

    only_password = {"password": faker.random_int(100000, 999999)}
    empty_password = {"email": faker.email(), "password": "","name":faker.name()}
    empty_email = {"email": "", "password": faker.random_int(100000, 999999)}
    empty_name = {"email": faker.email(), "password": faker.random_int(100000, 999999), "name": ""}

    user_auth = {"email": "car123@mail.ru","password": "123456"}
    user_auth_incorrect_data ={"email": "car123@miil.ru","password": "123456test"}

    create_email_user = {"email": faker.email()}
    create_password_user = {"password": faker.random_int(100000, 999999)}

class UserErrors:
    user_already_exist = 'User already exists'
    required_fields = 'Email, password and name are required fields'
    incorrect_data = 'email or password are incorrect'
    change_data_without_auth = 'You should be authorised'


class OrdersErrors:
    create_order_without_ingredients = "Ingredient ids must be provided"
    error_500 = 'Internal Server Error'
    get_order__without_auth = "You should be authorised"


class Ingredient:
    INGREDIENTS = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70"]}
    WITHOUT_INGREDIENTS = {"ingredients": []}
    INCORRECT_INGREDIENTS = {"ingredients": ["61c0c5a71d1f82001bdaaa6d1", "61c0c5a71d1f82001bdaaa701"]}

