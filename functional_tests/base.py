import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()

    def tearDown(self):
        time.sleep(1)
        self.browser.quit()

    def get_body_text(self):
        """Returns the html code on current time
        """
        body = self.browser.find_element_by_tag_name('body')
        return body.text

    def timeout(self, t=3):
        time.sleep(t)
