from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"/home/almagro/Escritorio/Selenium/chromedriver")
driver.get("http://python.org")
input()
driver.close()