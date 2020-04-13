from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = "/home/almagro/Escritorio/Selenium/chromedriver")
driver.get("file:///home/almagro/Escritorio/Selenium/confirm_alert.html")
time.sleep(5)
confirm_alert = driver.find_element_by_name("confirmar_alert")
confirm_alert.click()
time.sleep(3)
confirm_alert = driver.switch_to_alert()
#confirm_alert.dismiss()
confirm_alert.accept()
time.sleep(3)
driver.close()
