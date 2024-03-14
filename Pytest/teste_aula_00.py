# video aula 32
import pytest
from time import sleep
from selenium.webdriver.common.by import By

import conftest
'''
https://docs.pytest.org/en/7.1.x/contents.html
Para executar, P:\REPOSITORIO\PRIVADO\Aulas_Python_Selenium\Pytest> pytest .\teste_aula_00.py:
ou
Para executar, P:\REPOSITORIO\PRIVADO\Aulas_Python_Selenium\> pytest -v .\Pytest.\teste_aula_00.py

'''

@pytest.mark.usefixtures('setup_teardown')
class TesteDriver():
    def teste_driver_selecionar_carrinho(self):
        # ======================= Iniciar Navegador ==============================
        driver = conftest.driver

        # ========================== Entrar Login ================================
        sleep(1)
        nome_usuario = driver.find_element(By.ID,"user-name") # identifica as tag no site
        nome_usuario.send_keys('standard_user') # inserir texto na tag selecionada
        sleep(1)
        senha = driver.find_element(By.ID,"password") # identifica as tag no site
        senha.send_keys('secret_sauce') # inserir texto na tag selecionada
        sleep(1)

        botao_login = driver.find_element(By.ID,"login-button") # identifica as tag no site
        botao_login.click()
        assert driver.find_element(By.XPATH, "//div[@class='product_label']").is_displayed()
        sleep(1)

        # ========================== Selecionar Produto ================================
        ver_produto1 = driver.find_element(By.XPATH,"//a[@id='item_4_title_link']//div[@class='inventory_item_name']") # identifica as tag no site
        # ver_produto = driver.find_element(By.XPATH,"//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']") # identifica as tag no site
        ver_produto1.click()
        sleep(1)
        botao_produto1 = driver.find_element(By.XPATH,"//button[@class='btn_primary btn_inventory']") # identifica as tag no site
        botao_produto1.click()
        sleep(1)

        # ========================== Ver carrinho ================================
        carrinho = driver.find_element(By.XPATH,"//a[@class='shopping_cart_link fa-layers fa-fw']") # identifica as tag no site
        carrinho.click()
        sleep(1)

        # ========================== Confirmar Produto ================================
        assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

        # ========================== Voltar pagina ================================
        driver.back() # retorna a pagina anterior "site"
        sleep(1)

        driver.back() # retorna a pagina anterior "site"
        sleep(1)

        # ========================== Selecionar Produto ================================
        ver_produto2 = driver.find_element(By.ID, "item_0_title_link")
        ver_produto2.click()
        sleep(1)
        botao_produto2 = driver.find_element(By.XPATH,"//button[@class='btn_primary btn_inventory']") # identifica as tag no site
        botao_produto2.click()
        sleep(1)

        # ========================== Ver carrinho ================================
        carrinho = driver.find_element(By.XPATH,"//a[@class='shopping_cart_link fa-layers fa-fw']") # identifica as tag no site
        carrinho.click()
        sleep(1)

        # ========================== Confirmar Produto ================================
        assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()
