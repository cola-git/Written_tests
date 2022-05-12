import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def get_browser():
    """启动浏览器"""
    browser = webdriver.Chrome()
    wait_timeout = 20
    browser.implicitly_wait(wait_timeout)
    browser.maximize_window()
    yield browser
    browser.quit()
