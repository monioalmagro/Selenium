import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import cv2
import time


class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "/home/almagro/Escritorio/Selenium/chromedriver")
        
    def test_usando_toggle(self):
        driver = self.driver 
        driver.get("https://www.w3schools.com/howto/howto_css_switch.asp") 
        time.sleep(3)
        toggle = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/label[1]/div")
        toggle.click()
        time.sleep(3)
        toggle.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()                