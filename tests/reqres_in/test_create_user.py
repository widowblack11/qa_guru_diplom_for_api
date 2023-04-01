import allure
from allure_commons.types import Severity
from pytest_voluptuous import S

from schemas.user import add_user


@allure.title('Создание пользователя')
@allure.tag('api')
@allure.label('owner', 'o_prokopenko')
@allure.severity(Severity.CRITICAL)
@allure.feature('Создание пользователя')
@allure.story('reqres')
def test_create_user_ok(reqres):
    body = {
    "name": "morpheus",
    "job": "leader"
}
    with allure.step('Выполнить запрос на создание пользователя - указано имя и работа'):
        response = reqres.post('/api/users', data=body)
    with allure.step('Проверить, что код ответа 201'):
        assert response.status_code == 201
    with allure.step('Проверить, что схема ответа соответствует спецификации'):
        assert S(add_user) == response.json()
    with allure.step('Проверить, что имя в ответе соответствует введенному'):
        assert response.json()["name"] == "morpheus"


@allure.title('Создание пользователя без указания работы')
@allure.tag('api')
@allure.label('owner', 'o_prokopenko')
@allure.severity(Severity.CRITICAL)
@allure.feature('Создание пользователя')
@allure.story('reqres')
def test_create_user_without_job(reqres):
    body = {
        "name": "morpheus"
    }
    with allure.step('выполнить запрос на создания пользователя без указания работы'):
        response = reqres.post('/api/users', data=body)
    with allure.step('Проверить, что код ответа 201'):
        assert response.status_code == 201
    with allure.step('Проверить, что схема ответа соответствует спецификации'):
        assert S(add_user) == response.json()




