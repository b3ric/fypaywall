from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time 
import pyautogui
from selenium.webdriver.common.keys import Keys
import random, string
import os

# Consts for building path - move outta here (maybe some constructor?)
LEN = 8
ASCII_U = string.ascii_uppercase
ASCII_L = string.ascii_lowercase
D = string.digits

# Implement this!
# move to utils 
def build_rand_path():
    return ''.join(random.choice(ASCII_U + ASCII_L + D) for _ in range(LEN))
    
    
# implement webdriver class
def generate_dir():
    # import this path from some class?
    #dir = 'C:\\Users\\ericm\\Desktop\\stuff\\bypass_paywall\\'
    dir = os.getcwd() + '.\\scrape\\'
    return (dir + build_rand_path())

# implement webdriver class
def build_driver(directory):
    
    op = Options()
    # kill js blocks
    op.set_preference('javascript.enabled', False)
    profile = webdriver.FirefoxProfile()
    # read doc for folderList, 2
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.dir", directory)
    
    # set geckodriver.exe path
    return webdriver.Firefox(profile, executable_path="geckodriver.exe",options=op)

# implement webdriver class
def get_page(driver):
    # allow pass url CLI
    # POST HTTP from form
    # move flask? 
    default_url = "https://www1.folha.uol.com.br/mercado/2022/03/franca-diz-que-sancoes-farao-economia-russa-colapsar.shtml"
    driver.get(default_url)
    
    # baixar html + css, vem tudo
    # gambiarra...... ta feio
    # send to cache.py
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1) # try reduce sleep?
    pyautogui.hotkey('enter')

# place in __init__.py
def main():
    get_page(build_driver(generate_dir()))
    
if __name__ == "__main__":
    main()