from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = "/home/almagro/Escritorio/Selenium/chromedriver")
driver.get("https://google.com")
time.sleep(10)
displaelemnten = driver.find_element_by_name("btnI")
print(displaelemnten.is_displayed())# regresa Bolean si cargo el elemento
print(displaelemnten.is_enabled())#regresa bolean si el elementoesta disponible


time.sleep(3)
