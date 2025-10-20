import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene.support.shared import browser

from utils import attaches
from dotenv import load_dotenv
import os

from model.main_page import MainPage

@pytest.fixture
def open_main_page():
    main_page = MainPage()
    main_page.open()
    yield main_page


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    
    browser.config.base_url = "https://mybook.ru"

    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument("--incognito")
    driver_options.page_load_strategy = "eager"
    driver_options.add_argument("--window-size=1920,1280")

    browser.config.driver = webdriver.Chrome(options=driver_options)

    yield
    browser.quit()
    '''

DEFAULT_BROWSER_VERSION = "128.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='128.0'
    )


@pytest.fixture(scope="session", autouse=True)
def load_env():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    dotenv_path = os.path.join(base_dir, ".env")
    load_dotenv(dotenv_path=dotenv_path)


@pytest.fixture(scope="function")
def setup_browser(request):
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    browser.browser_version = browser_version

    options = Options()
    options.page_load_strategy = "eager"
    options.add_argument("--incognito")
    options.add_argument("--window-size=1920,1280")

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options,
    )

    browser.config.base_url = "https://mybook.ru"
    browser.config.driver = driver
    yield browser

    attaches.add_logs(browser)
    attaches.add_html(browser)
    attaches.add_screenshot(browser)
    attaches.add_video(browser, selenoid_url)

    browser.quit()
    '''