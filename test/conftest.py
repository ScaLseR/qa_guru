import pytest
from selene.support.shared import browser
from test_python_8_2 import URL


@pytest.fixture(scope='function')
def browser_setup():
    """Фикстура настройки браузера"""
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture(scope='function')
def open_url(browser_setup):
    """Фикстура открытия браузера с указанным url"""
    browser.open(URL)
    yield browser
    browser.quit()
