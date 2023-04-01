import allure
from allure_commons.types import Severity
from pytest_voluptuous import S

from schemas.user import users_list_schema


@allure.title('Получить список пользователей')
@allure.tag('api')
@allure.label('owner', 'o_prokopenko')
@allure.severity(Severity.CRITICAL)
@allure.feature('Получение списка пользователей')
@allure.story('reqres')
def test_get_list_users_ok(reqres):
    with allure.step('Выполнить запрос на получение списка пользователей'):
        response = reqres.get('/api/users', params={"page": 2})

    with allure.step('Проверить, что код ответа 200'):
        assert response.status_code == 200
    with allure.step('Проверить, что схема ответа соответствует спецификации'):
        assert S(users_list_schema) == response.json()
    with allure.step('Проверить,что среди указанных пользователей есть michael.lawson@reqres.in'):
        assert response.json()["data"][0]["email"] == "michael.lawson@reqres.in"
