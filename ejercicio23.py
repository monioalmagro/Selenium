from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

opciones = Options()
#enviar argunmentos (1 permitiendola notificacion, 2 bloquea la modificacion)
opciones.add_experimental_option("prefs",{
    "profile.default_content_setting_values.notifications" : 1
})

driver = webdriver.Chrome(chrome_options = opciones, executable_path= "/home/almagro/Escritorio/Selenium/chromedriver")
driver.get('https://developer.mozilla.org/es/docs/Web/API/notification')
time.sleep(3)
