#Arquivo para funções utilitárias relacionadas ao Selenium, como espera explícita, captura de exceções, etc.

from selenium_config import *

def pause_send_keys(variavel, parametro): #Criei o esquema para esperas para escrita
        try:
            WebDriverWait(Chrome_driver, 10).until( 
                EC.visibility_of_element_located(By.XPATH, variavel) #se a condição esperada for a visibilidade do element
            )
            element = Chrome_driver.find_element(By.XPATH, variavel)
            element.send_keys(parametro)
            return
        except Exception:
            print("Timeout e numero de tentativas atingidas")

def pause_click(variavel): #Criei a função para click  
    for i in range(0,3):
        try:
            WebDriverWait(Chrome_driver, 10).until( 
                EC.visibility_of_element_located(By.XPATH, variavel)
            )
            element = Chrome_driver.find_element(By.XPATH, variavel)
            element.click()
            return
        except Exception:
            print("Timeout")

def pause_get(variavel, parametro): #Criei a função para get
    for i in range(0,3):
        try:
            WebDriverWait(Chrome_driver, 10).until( 
                EC.visibility_of_element_located(By.XPATH, parametro)
            )
            element = Chrome_driver.find_element(By.XPATH, parametro)
            element.get(variavel)
            return
        except Exception:
            print("Timeout")