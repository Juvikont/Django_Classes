from django.test import TestCase, LiveServerTestCase
from django.contrib.auth.models import User
from selenium.webdriver import Chrome
from time import sleep


class SeleniumTestCase(LiveServerTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.driver = Chrome(r'C:\Users\Yuri\Desktop\chromedriver.exe')

    def tearDown(self) -> None:
        super().tearDown()
        self.driver.quit()


class LogiTest(SeleniumTestCase):
    def setUp(self) -> None:
        super().setUp()
        User.objects.create_user('bob', password='bob')

    def test(self):
        self.driver.get(self.live_server_url+'/login')
        sleep(2)
        username = self.driver.find_element_by_id('input-username')
        password = self.driver.find_element_by_id('input-password')
        submit = self.driver.find_element_by_id('input-submit')
        username.send_keys('bob')
        password.send_keys('bob')
        sleep(2)
        submit.click()
        self.assertEqual(self.driver.current_url, self.live_server_url+'/')