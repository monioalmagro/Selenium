import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(executable_path = "/home/almagro/Escritorio/Selenium/chromedriver")
driver.get("http://www.w3schools.com/")
time.sleep(3)
encontrar_link = driver.find_element_by_link_text('Learn CSS')
encontrar_link.click()
