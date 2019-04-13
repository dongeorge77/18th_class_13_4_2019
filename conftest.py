from selenium import webdriver
import pytest
from Testdata.data import *

@pytest.fixture(scope='class')
def test_launch_browser(request):
    global driver
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.implicitly_wait(30)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
