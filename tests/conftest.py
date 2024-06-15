import os
import pytest
from dotenv import load_dotenv
from selene import browser
from selenium.webdriver.chrome.options import Options
from demoqa_tests.utils import attach


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version', help='Версия браузера', default='100.0'
    )


@pytest.fixture(scope='function', autouse=True)
def browser_management(request):
    browser_version = request.config.getoption('--browser_version')

    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    options.capabilities.update(selenoid_capabilities)
    browser.config.driver_remote_url = (
        f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub"
    )

    browser.config.driver_options = options

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
