from selenium import webdriver

driver = webdriver.Chrome(executable_path = "/home/almagro/Escritorio/Selenium/chromedriver")
driver.get("http://almagro.pythonanywhere.com/porfolio/")
driver.get_screenshot_as_file('/home/almagro/Escritorio/Selenium/screen.png')
driver.close()