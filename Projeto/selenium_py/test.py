from selenium_utils import pause_send_keys
from selenium_config import Chrome_driver
from variables import *

Chrome_driver.get('https://app.kcms.com.br/login')

from selenium_utils import pause_send_keys  # Import from selenium_config.py

pause_send_keys(input_loginEmail, "oiiii")

input("Click")

