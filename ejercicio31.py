import unittest
from selenium import webdriver
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "/home/almagro/Escritorio/Selenium/chromedriver")

    def test_asserEqual(self):
        driver = self.driver
        driver.get("http://www.google.com")
        titulo_de_la_pagina = driver.title
        self.assertEqual("Google",titulo_de_la_pagina,"El titulo de la pagina no coincide")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()            