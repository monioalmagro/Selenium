
import configparser
configuracion = configparser.ConfigParser()

configuracion['General'] = {'chrome': '/home/almagro/Escritorio/Selenium/chromedriver'}
configuracion['Paginas'] = {'page' : 'https://www.google.com.ar' }

with open('configuracion.ini','w') as archivoconfig:
    configuracion.write(archivoconfig)