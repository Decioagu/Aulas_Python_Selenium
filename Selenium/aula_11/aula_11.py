# video aula 26 até 29

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
"implicitly_wait": Aplicável globalmente a todos os elementos da página.
Define um tempo máximo que o Selenium espera para encontrar um elemento
antes de lançar uma exceção.
'''

browser = webdriver.Chrome()
browser.implicitly_wait(12)
browser.maximize_window() # maximiza a tela do "site"

browser.get('https://www.saucedemo.com/v1/') # acesso a pagina desejada "site"

# ========================== Entrar Login ================================
sleep(1)
nome_usuario = browser.find_element(By.ID,"user-name") # identifica as tag no site
nome_usuario.send_keys('standard_user') # inserir texto na tag selecionada
sleep(1)
senha = browser.find_element(By.ID,"password") # identifica as tag no site
senha.send_keys('secret_sauce') # inserir texto na tag selecionada
sleep(1)

botao_login = browser.find_element(By.ID,"login-button") # identifica as tag no site
botao_login.click()
assert browser.find_element(By.XPATH, "//div[@class='product_label']").is_displayed()
sleep(1)

# ========================== Selecionar Produto ================================
ver_produto1 = browser.find_element(By.XPATH,"//a[@id='item_4_title_link']//div[@class='inventory_item_name']") # identifica as tag no site
# ver_produto = browser.find_element(By.XPATH,"//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']") # identifica as tag no site
ver_produto1.click()
sleep(1)
botao_produto1 = browser.find_element(By.XPATH,"//button[@class='btn_primary btn_inventory']") # identifica as tag no site
botao_produto1.click()
sleep(1)

# ========================== Ver carrinho ================================
carrinho = browser.find_element(By.XPATH,"//a[@class='shopping_cart_link fa-layers fa-fw']") # identifica as tag no site
carrinho.click()
sleep(3)

# ========================== Confirmar Produto ================================
assert browser.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

# ========================== Voltar pagina ================================
browser.back() # retorna a pagina anterior "site"
sleep(1)

browser.back() # retorna a pagina anterior "site"
sleep(1)

# ========================== Selecionar Produto ================================
ver_produto2 = browser.find_element(By.ID, "item_0_title_link")
ver_produto2.click()
sleep(1)
botao_produto2 = browser.find_element(By.XPATH,"//button[@class='btn_primary btn_inventory']") # identifica as tag no site
botao_produto2.click()
sleep(1)

# ========================== Ver carrinho ================================
carrinho = browser.find_element(By.XPATH,"//a[@class='shopping_cart_link fa-layers fa-fw']") # identifica as tag no site
carrinho.click()
sleep(1)

# ========================== Confirmar Produto ================================
assert browser.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()


browser.quit() # fecha o browser
