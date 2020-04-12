import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC 
import cv2
import time


class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "/home/almagro/Escritorio/Selenium/chromedriver")

    def test_usando_select(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        time.sleep(3)
        select = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/div[3]/div[1]/select")
        opcion = select.find_elements_by_tag_name("option")
        print(opcion)
        time.sleep(3)
        #print("estoy aca ")
        for option in opcion:
            print("Valores son: %s " % option.get_attribute("value") )
            option.click()
            #print("estoy aca 2 ")
            time.sleep(1)
        seleccionar = Select(driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/div[3]/div[1]/select"))                
        seleccionar.select_by_value("10")
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()        