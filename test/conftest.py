import pytest
from selene.support.shared import browser

#  url открываемого сайтк
URL = 'https://google.com'


@pytest.fixture(scope='function')
def browser_setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture(scope='function')
def open_url(browser_setup):
    browser.open(URL)
    yield browser
    browser.quit()
