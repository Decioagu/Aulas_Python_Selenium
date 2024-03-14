# video aula 34
from time import sleep
from selenium.webdriver.common.by import By

import conftest
from base_page import BasePage

class LoginPage(BasePage):
    def __init__(self) -> None:
        # ======================= Iniciar Navegador ==============================
        self.driver = conftest.driver
        self.nome_field = (By.ID,"user-name")
        self.password_field = (By.ID,"password")
        self.login_field = (By.ID,"login-button")
        self.produto1_field = (By.XPATH, "//a[@id='item_4_title_link']//div[@class='inventory_item_name']")
        self.botao_produto1_field = (By.XPATH, "//button[@class='btn_primary btn_inventory']")
        self.carrinho_field = (By.XPATH,"//a[@class='shopping_cart_link fa-layers fa-fw']")
        self.produto2_field = (By.ID, "item_0_title_link")
        self.botao_produto2_field = (By.XPATH,"//button[@class='btn_primary btn_inventory']")

        self.titulo_pagina_field = (By.XPATH,'//div[@class="product_label"]')
        self.erro_field = (By.XPATH, '//h3[@data-test="error"]')


    def fazer_login(self, usuario, senha):
        sleep(1)
        self.escrever(self.nome_field, usuario)
        sleep(1)
        self.escrever(self.password_field, senha)
        sleep(1)
        self.clicar(self.login_field)

        if self.verficar_login_com_sucesso(self.titulo_pagina_field):
            sleep(1)
            self.clicar(self.produto1_field)
            sleep(1)
            self.clicar(self.botao_produto1_field)
            sleep(1)
            self.clicar(self.carrinho_field)
            sleep(1)
            self.voltar_pagina()
            sleep(1)
            self.voltar_pagina()
            sleep(1)
            self.clicar(self.produto2_field)
            sleep(1)
            self.clicar(self.botao_produto2_field)
            sleep(1)
            self.clicar(self.carrinho_field)
            sleep(1)
            self.voltar_pagina()
            sleep(1)
            self.voltar_pagina()
            sleep(1)
            self.finalizar()
        else:
            self.verficar_login_com_erro(self.erro_field)
