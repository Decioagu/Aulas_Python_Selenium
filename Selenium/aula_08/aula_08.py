# video aula 24

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
'''
# pip install webdriver-manager
    O webdriver-manager é uma biblioteca que facilita o gerenciamento de drivers de
    navegador para automação web em Python. Ele automatiza o download e a instalação
    dos drivers específicos para a versão do navegador que você está usando,
    simplificando e agilizando seu processo de desenvolvimento.
'''
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.implicitly_wait(30)
'''
"implicitly_wait": Aplicável globalmente a todos os elementos da página.
Define um tempo máximo que o Selenium espera para encontrar um elemento
antes de lançar uma exceção.
'''
browser.maximize_window() # maximiza a tela do "site"

browser.get('https://chercher.tech/practice/practice-dropdowns-selenium-webdriver') # acesso a pagina desejada "site"

dropdown_products = Select(browser.find_element(By.XPATH,"//select[@id='first']"))
dropdown_products.select_by_visible_text("Yahoo") # selecionar por texto
sleep(5)

dropdown_animals = Select(browser.find_element(By.XPATH,"//select[@id='animals']"))
dropdown_animals.select_by_value("avatar") # selecionar por valor
sleep(5)
dropdown_animals.select_by_index(1) # selecionar por valor
sleep(5)

dropdown_food_items_multiple = Select(browser.find_element(By.XPATH,"//select[@id='second']"))
dropdown_food_items_multiple.select_by_visible_text("Pizza") # selecionar por texto
sleep(5)
dropdown_food_items_multiple.select_by_visible_text("Bonda") # selecionar por texto
sleep(5)




