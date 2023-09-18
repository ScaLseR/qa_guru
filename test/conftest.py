import pytest
from selene.support.shared import browser

#  url открываемого сайтк
URL = 'https://google.com'


@pytest.fixture(scope='function')
def open_browser_full_screen():
    browser.driver.fullscreen_window()
    browser.open(URL)
    yield browser
    browser.quit()
