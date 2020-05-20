import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "/home/almagro/Escritorio/Selenium/chromedriver")

    def test_cambiar_ventana(self):
        driver = self.driver
        driver.get("http://www.google.com") 
        time.sleep(3) 
        driver.execute_script("window.open('');")#esto es de python
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        driver.get("http://stackoverflow.com")
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()

    