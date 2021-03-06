from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from .forms import HashForm
import hashlib


# class FunctionalTestCase(TestCase):
#
#     def setUp(self):
#         self.browser = webdriver.Firefox()
#
#     def test_there_is_homepage(self):
#         self.browser.get('http://localhost:8000')
#         self.assertIn('Enter hash here', self.browser.page_source)
#
#     def test_hash_of_hello(self):
#         self.browser.get('http://localhost:8000')
#         text = self.browser.find_element(By.ID, 'id_text')
#         text.send_keys('hello')
#         self.browser.find_element(By.NAME, 'submit').click()
#         self.assertIn('2CF24DBA5FB0A30E26E83B2AC5B9E29E1B161E5C1FA7425E73043362938B9824', self.browser.page_source)
#
#     def tearDown(self):
#         self.browser.quit()


class UnitTestCase(TestCase):

    def test_home_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'hashing/home.html')

    def test_hash_form(self):
        form = HashForm(data={'text': 'hello'})
        self.assertTrue(form.is_valid())

    def test_hash_func_works(self):
        text_hash = hashlib.sha256('hello'.encode('utf-8')).hexdigest()
        self.assertEqual('2CF24DBA5FB0A30E26E83B2AC5B9E29E1B161E5C1FA7425E73043362938B9824', text_hash.upper())
