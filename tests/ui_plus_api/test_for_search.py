import allure
from allure_commons.types import Severity
from selene import have
from selene.support.shared import browser


@allure.title('Поиск - нет результатов по запросу')
@allure.tag('api_plus_api')
@allure.label('owner', 'o_prokopenko')
@allure.severity(Severity.CRITICAL)
@allure.feature('Поиск')
@allure.story('demowebshop')
def test_search_negative_result(auth_browser):
    with allure.step('Открыть главную страницу под залогининым пользователем'):
        auth_browser.open("")

    with allure.step('Кликнуть в строку поиска'):
        browser.element('.search-box [value="Search store"]').click()
    with allure.step('Ввести "negative test" и нажать enter'):
        browser.element('.search-box [value="Search store"]').type('negative test').press_enter()
    with allure.step('Проверить текст ответа на поиск'):
        browser.element('.result').should(have.text('No products were found that matched your criteria.'))
