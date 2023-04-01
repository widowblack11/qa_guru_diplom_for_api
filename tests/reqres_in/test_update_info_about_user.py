import allure
from allure_commons.types import Severity
from pytest_voluptuous import S

from schemas.user import update_user


@allure.title('Обновить у пользователя инфо о работе и имени')
@allure.tag('api')
@allure.label('owner', 'o_prokopenko')
@allure.severity(Severity.CRITICAL)
@allure.feature('Обновление информации о пользователи')
@allure.story('reqres')
def test_update_info_about_user_ok(reqres):
    body = {
    "name": "morpheus",
    "job": "leader"
}
    with allure.step('Выполнить запрос на обновление имени и работы пользователя'):
        response = reqres.patch('/api/users/2', data=body)
    with allure.step('Проверить,что код ответа 200'):
        assert response.status_code == 200
    with allure.step('Проверить, что схема ответа соответствует спецификации'):
        assert S(update_user) == response.json()
    with allure.step('Проверить,что поля в ответе соответствуют введенным'):
        assert response.json()["name"] == "morpheus" and response.json()["job"] == "leader"


@allure.title('Обновить у пользователя инфо о работе(две работы) и имени')
@allure.tag('api')
@allure.label('owner', 'o_prokopenko')
@allure.severity(Severity.CRITICAL)
@allure.feature('Обновление информации о пользователи')
@allure.story('reqres')
def test_update_info_about_user_when_two_user_job(reqres):
    body = {
    "name": "morpheus",
    "job": ["leader", "teacher"]
}
    with allure.step('Выполнить запрос на обновление имени пользователя и работы(у пользователя две работы)'):
        response = reqres.patch('/api/users/2', data=body)
    with allure.step('Проверить,что код ответа 200'):
        assert response.status_code == 200
    with allure.step('Проверить,что поля в ответе соответствуют введенным'):
        assert response.json()["job"] == ["leader", "teacher"]