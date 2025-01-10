#Arquivo responsável pelas configurações iniciais do Selenium

from selenium import webdriver #Webdrive é o que faz a interação com o navegador(não especificado)
from selenium.webdriver.chrome.options import Options  #Importa as opções do Chrome (para configuração)
from webdriver_manager.chrome import ChromeDriverManager #Instala automaticamente o ChromeDriver e configura para o navegador
from selenium.webdriver.chrome.service import Service #modulo de utilização de serviço do webdriver

#Criando instancias das opções do chrome
Chrome_Options = Options() #instancia de Options
#Chrome_Options.add_argument('--headless') #--headless é para executar em segundo plano
Chrome_Options.add_argument("--disable-software-rasterizer") # Aumenta a performance
Chrome_Options.add_argument('--incognito') #--incognito roda em guia anonima evitando de salvar senhas e cookies
Chrome_Options.add_argument("--disable-gpu") #desabilita o uso de GPU
Chrome_Options.add_argument("--disable-images") #desabilita o carregamento de imagens para rodar de forma mais rapida

#Instalando e configurando
DriverChrome = ChromeDriverManager().install() #instala automaticamente o chromedriver do chrome
ChromeService = Service(DriverChrome) #roda o serviço do chrome driver

#Iniciaizando com as opções definidas
Chrome_driver = webdriver.Chrome(service= ChromeService, options = Chrome_Options)