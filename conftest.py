import configparser
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

IMPLICIT_WAIT_TIME = 10


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")


@pytest.fixture
def config():
    config = configparser.ConfigParser()
    config.read("../config.ini")
    return {
        "email": config.get("credentials", "email"),
        "password": config.get("credentials", "password"),
        "email_password": config.get("credentials", "email_password"),
        "country": config.get("settings", "country"),
        "language": config.get("settings", "language"),
    }


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser", default="chrome")

    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise ValueError(f"Unsupported browser: {browser}. Supported browsers are: chrome, firefox")

    driver.implicitly_wait(IMPLICIT_WAIT_TIME)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()
