import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "/home/almagro/Escritorio/Selenium/chromedriver")

    def test_pagina_siguiente_o_anterior(self):
        driver = self.driver
        driver.get("http:/www.lainterempresarial.com")
        time.sleep(3)
        driver.get("http:/www.google.com")
        time.sleep(3)
        driver.get("http:/www.youtube.com")
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.forward()
        time.sleep(3)

if __name__ == "__main__":
    unittest.main() 