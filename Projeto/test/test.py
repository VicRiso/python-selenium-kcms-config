from selenium_py.selenium_utils import *
from selenium_py.selenium_config import Chrome_driver
from program_logic.variables import *

Chrome_driver.get('https://app.kcms.com.br/login')

pause_send_keys(input_loginEmail, "oiiii")

input("Click")

