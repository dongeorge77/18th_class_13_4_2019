import time
from Pages.loginpage import LoginPage
from Pages.homepage import HomePage
import pytest

@pytest.mark.usefixtures("test_launch_browser")
class Testlogin:
    def test_login(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.enter_un()
        lp.enter_pwd()
        lp.click_login()
    def test_logout(self):
        driver = self.driver
        time.sleep(5)
        hp = HomePage(driver)
        hp.logout_page()