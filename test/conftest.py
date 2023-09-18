import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function')
def open_browser_full_screen():
    browser.driver.fullscreen_window()
    browser.open('https://google.com')
    yield browser
    browser.quit()
