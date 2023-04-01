import os

import allure
from allure_commons.types import Severity
from selene import have
from selene.support.shared import browser


@allure.title('Просмотр страницы смены пароля')
@allure.tag('api_plus_api')
@allure.label('owner', 'o_prokopenko')
@allure.severity(Severity.CRITICAL)
@allure.feature('Настройки пользователя')
@allure.story('demowebshop')
def test_watch_page_change_password(auth_browser):
    with allure.step('Открыть главную страницу под залогининым пользователем'):
        auth_browser.open("")

    with allure.step('Нажать на кнопку "change password" и проверить наличие обязательных полей'):
        browser.element(".account").should(have.text(os.getenv('LOGIN'))).click()
        browser.element('[href="/customer/changepassword"]').should(have.text('Change password')).click()
    with allure.step('Проверить наличие обязательных полей'):
        browser.element('[for="OldPassword"]').should(have.text('Old password:'))
        browser.element('[for="NewPassword"]').should(have.text('New password:'))
        browser.element('[for="ConfirmNewPassword"]').should(have.text('Confirm password:'))