import os

import allure
from allure_commons.types import Severity
from dotenv import load_dotenv
from selene import have
from selene.support.shared import browser

load_dotenv()


@allure.title('Войти на сайт под зарегестрированным пользователем')
@allure.tag('api_plus_api')
@allure.label('owner', 'o_prokopenko')
@allure.severity(Severity.CRITICAL)
@allure.feature('Логин')
@allure.story('demowebshop')
def test_login_with_api(auth_browser):
    with allure.step('Открыть главную страницу под залогининым пользователем'):
        auth_browser.open("")

    with allure.step("Verify successful authorization"):
        auth_browser.element(".account").should(have.text(os.getenv("LOGIN")))











