#Arquivo responsável pelas configurações iniciais do Selenium

from selenium import webdriver #Webdrive é o que faz a interação com o navegador(não especificado)
from selenium.webdriver.common.by import By #Importa os localizadores de elementos (não especificado)
from selenium.webdriver.chrome.options import Options  #Importa as opções do Chrome (para configuração)
from webdriver_manager.chrome import ChromeDriverManager #Instala automaticamente o ChromeDriver e configura para o navegador
from selenium.webdriver.chrome.service import Service #modulo de utilização de serviço do webdriver
from selenium.webdriver.support import expected_conditions as EC #condição esperada
from selenium.webdriver.support.ui import WebDriverWait #O Webdriver espera uma função

Chrome_Options = Options() #instancia de Options
DriverChrome = ChromeDriverManager().install() #instala automaticamente o chromedriver do chrome
ChromeService = Service(DriverChrome) #roda o serviço do chrome driver

#Chrome_Options.page_load_strategy = 'eager' #estratégia de carregamento de pagina será eager (carrega a parte interativa)
#Chrome_Options.add_argument('--headless') #--headless é para executar em segundo plano
Chrome_Options.add_argument('--incognito') #--incognito roda em guia anonima evitando de salvar senhas e cookies
Chrome_Options.add_argument("--disable-gpu") #desabilita o uso de GPU
Chrome_Options.add_argument("--disable-images") #desabilita o carregamento de imagens para rodar de forma mais rapida

Chrome_driver = webdriver.Chrome(service= ChromeService, options = Chrome_Options)