import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "/home/almagro/Escritorio/Selenium/chromedriver")

    def test_buscar_por_xpath(self):
        driver = self.driver
        driver.get("http://www.google.com")
        time.sleep(5)
        buscar_por_xpath = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
        time.sleep(5)
        buscar_por_xpath.send_keys("selenium", Keys.ARROW_DOWN)#una tecleo hacia abajo
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    







# xpath es una estructura de carpetas, objetos.
#xpath relativo: //*[@id='fakebox-input'] SE USA ESTE!!!
#xpath absoluto: /html/body/div[4]/div[2]/div/input
