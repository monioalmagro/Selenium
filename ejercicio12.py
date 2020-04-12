import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "/home/almagro/Escritorio/Selenium/chromedriver")

    def test_usando_radio_button(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
        time.sleep(5)
        radio_bt = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/div[3]/div[3]/label[3]/span")
        radio_bt.click()
        time.sleep(3)
        radio_bt = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/div[3]/div[3]/label[2]/span") 
        radio_bt.click()
        time.sleep(2)
        radio_bt = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/div[3]/div[3]/label[1]/span")
        radio_bt.click()
        time.sleep(3)
        radio_bt = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/div[3]/div[3]/label[4]/span")
        radio_bt.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()             