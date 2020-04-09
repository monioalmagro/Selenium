from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"/home/almagro/Escritorio/Selenium/chromedriver")
driver.get("http://localhost:8000/admin")

usuario = driver.find_element_by_name("username")
usuario.send_keys("almagro")
input()
usuario.send_keys(Keys.ENTER)
time.sleep(5)
print("estoy en el primer sleep")
input()

clave = driver.find_element_by_name("password")
clave.send_keys("cafecito")
clave.send_keys(Keys.ENTER)