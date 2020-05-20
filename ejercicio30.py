import HtmlTestRunner
import unittest 
from selenium import webdriver
import time

class suite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "/home/almagro/Escritorio/Selenium/chromedriver")
        
    
    def test_busqueda(self):
        self.driver.get("http://www.google.com")
        self.busqueda = self.driver.find_element_by_name("q")
        self.busqueda.send_keys("selenium")
        self.busqueda.submit()
        time.sleep(3)

    def test_scroll_down(self):
        
        self.driver.get("https://www.amazon.com")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)

    def test_link_por_texto(self):
        
        self.driver.get("http://www.w3schools.com/")
        time.sleep(3)
        encontrar_link = self.driver.find_element_by_link_text('Learn CSS')
        encontrar_link.click()
        time.sleep(3)
        

    def tearDown(self): 
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='resultado de mi test plan'))