import os

from selenium import webdriver
import pytest
from dotenv import load_dotenv
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options
from framework.DemoQaWithEnv import DemoQaWithEnv
from utils import attach


authorization_cookie = None
load_dotenv()
DEFAULT_BROWSER_VERSION = "100.0"


def pytest_addoption(parser):
    parser.addoption("--env", action='store', default="prod")


@pytest.fixture(scope="session")
def get_option(request):
    return request.config.getoption("--env")


@pytest.fixture(scope='session')
def demoshop(get_option):
    return DemoQaWithEnv(get_option)


@pytest.fixture(scope='session')
def reqres(get_option):
    return DemoQaWithEnv(get_option).reqres


@pytest.fixture(scope='function')
def auth_browser(demoshop):
    global authorization_cookie
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN_SELENOID')
    password = os.getenv('PASSWORD_SELENOID')
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options)
    browser.config.driver = driver
    browser.config.base_url = demoshop.demoqa.url
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    if authorization_cookie is None:
        response = demoshop.login(os.getenv("LOGIN"), os.getenv("PASSWORD"))
        authorization_cookie = response.cookies.get('NOPCOMMERCE.AUTH')
    browser.open("/Themes/DefaultClean/Content/images/logo.png")
    browser.driver.add_cookie({"name": 'NOPCOMMERCE.AUTH', "value": authorization_cookie})
    yield browser
    attach.add_screenshot(browser)
    attach.add_video(browser)


