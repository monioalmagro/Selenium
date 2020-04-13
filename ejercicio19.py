from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = "/home/almagro/Escritorio/Selenium/chromedriver")
driver.get("https://www.w3schools.com/html/html_tables.asp")
time.sleep(5)

valor = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr[2]/td[2]").text
print(valor)

rows = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
col = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[1]/th"))

#ES importante saber el tamano de las filas y columnas para que no 
# nos desborde la info por que rompe el programa 

print(rows)
print(col)

for n in range(2 ,rows+1):
    for b in range(1,col+1):
        dato = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(n)+"]/td["+str(b)+"]").text
        print(dato)
    print()    
