import os

import allure
from allure_commons.types import Severity
from selene import have
from selene.support.shared import browser


@allure.title('Просмотр данных пользователя')
@allure.tag('api_plus_api')
@allure.label('owner', 'o_prokopenko')
@allure.severity(Severity.CRITICAL)
@allure.feature('Профиль')
@allure.story('demowebshop')
def test_watch_profile(auth_browser):
    with allure.step('Открыть главную страницу под залогининым пользователем'):
        auth_browser.open("")

    with allure.step("Проверить информацию о пользователе"):
        browser.element(".account").should(have.text(os.getenv('LOGIN'))).click()
        browser.element('#FirstName').should(have.value('Oksana'))
        browser.element('#LastName').should(have.value('Oksana'))
        browser.element('#Email').should(have.value(os.getenv('LOGIN')))
        browser.element('[checked="checked"]#gender-female')