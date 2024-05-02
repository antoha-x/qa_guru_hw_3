import pytest
from selene import browser


@pytest.fixture(scope="session", autouse=True)
def config_browser():
    browser.config.driver.maximize_window()
    yield
    browser.quit()
