#Arquivo para funções utilitárias relacionadas ao Selenium, como espera explícita, captura de exceções, etc.

from selenium_config import *
from selenium.webdriver.support.ui import WebDriverWait #O Webdriver espera uma função
from selenium.webdriver.support import expected_conditions as EC #condição esperada
from selenium.webdriver.common.by import By #Importa os localizadores de elementos (não especificado)

def pause_send_keys(variavel, parametro): #Criei o esquema para esperas para escrita
    try:
        WebDriverWait(Chrome_driver, 10).until(  #se a condição esperada for a visibilidade do element
            EC.presence_of_element_located(variavel)or
            EC.element_to_be_clickable(variavel) 
        )
        Chrome_driver.find_element((By.XPATH, variavel)).send_keys(parametro)
    except Exception:
        WebDriverWait(Chrome_driver, 5).until(  #se a condição esperada for a visibilidade do element
            EC.presence_of_element_located(variavel)or
            EC.element_to_be_clickable(variavel)
        )
        Chrome_driver.find_element(*variavel).send_keys(parametro)

def pause_click(variavel): #Criei a função para click  
    WebDriverWait(Chrome_driver, 10).until( 
        EC.visibility_of_element_located(*variavel)
    )
    Chrome_driver.find_element(*variavel).click()

def pause_get(variavel, parametro): #Criei a função para get
    WebDriverWait(Chrome_driver, 10).until( 
        EC.visibility_of_element_located(*variavel)
    )
    Chrome_driver.get(parametro)
