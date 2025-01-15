from selenium_config import Chrome_driver
from variables import *
from selenium.webdriver.common.by import By #Importa os localizadores de elementos (não especificado)
from credenciais import *

Chrome_driver.get('https://app.kcms.com.br/login')

Chrome_driver.find_element(By.NAME, input_loginEmail).send_keys(loginEmail)
Chrome_driver.find_element(By.NAME, input_loginEmail).send_keys("1234")

input("Click")

