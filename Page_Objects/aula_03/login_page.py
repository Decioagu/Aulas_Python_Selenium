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


    def fazer_login(self, usuario, senha):
        sleep(1)
        self.escrever(self.nome_field, usuario)
        sleep(1)
        self.escrever(self.password_field, senha)
        sleep(1)
        self.clicar(self.login_field)

