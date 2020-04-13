from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = "/home/almagro/Escritorio/Selenium/chromedriver")
driver.get("file:///home/almagro/Escritorio/Selenium/alert_simple.html")
time.sleep(5)
alerta_simple = driver.find_element_by_name("alert")
alerta_simple.click()
time.sleep(3)
alerta_simple = driver.switch_to_alert()
alerta_simple.dismiss()#por que tiene un solo boton
time.sleep(3)
driver.close()
