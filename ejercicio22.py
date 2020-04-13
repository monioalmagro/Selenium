from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = "/home/almagro/Escritorio/Selenium/chromedriver")
driver.get("file:///home/almagro/Escritorio/Selenium/promp_alert.html")
time.sleep(3)
alert = driver.find_element_by_name("promp_alert")
alert.click()
time.sleep(3)
alert = driver.switch_to_alert()
#alert.accept()
alert.dismiss()
time.sleep(3)
driver.close()
