class TestBaseLinksAPI:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site/'


class TestCreatedUserAPI:
    CREATE_LOGIN_URL = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    AUTH_LOGIN_URL = 'https://stellarburgers.nomoreparties.site/api/auth/login'
    CHANGE_DATA_USER_URL = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    DELETE_USER_URL = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    GET_DATA_USER_URL = 'https://stellarburgers.nomoreparties.site/api/auth/user'


class TestCreatedOrderAPI:
    CREATE_ORDER_URL = 'https://stellarburgers.nomoreparties.site/api/orders'
    GET_ORDERS_USER_URL = 'https://stellarburgers.nomoreparties.site/api/orders'
    GET_INGREDIENT_URL ='https://stellarburgers.nomoreparties.site/api/ingredients'