import unittest
import configparser
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class usando_unittest(unittest.TestCase):

    def setUp(self):
        configuracion = configparser.ConfigParser()
        configuracion.read('configuracion.ini')
        configuracion.sections()
        obtenerexplorer = configuracion['General']['chrome']
        self.page = configuracion['Paginas']['page']
        self.driver = webdriver.Chrome(executable_path=obtenerexplorer)
    
    def test_usando_implicit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get(self.page)
        navegador = driver.find_element_by_name("q")

if __name__ == "__main__":
    unittest.main()        