from time import sleep
from selenium.webdriver.common.by import By

import conftest

class LoginPage:
    def __init__(self) -> None:
        # ======================= Iniciar Navegador ==============================
        self.driver = conftest.driver
        self.nome_field = (By.ID,"user-name")
        self.password_field = (By.ID,"password")
        self.login_field = (By.ID,"login-button")


    def fazer_login(self, usuario, senha):
        sleep(1)
        self.driver.find_element(*self.nome_field).send_keys(usuario) # identifica as tag no site
        sleep(1)
        self.driver.find_element(*self.password_field).send_keys(senha) # identifica as tag no site
        sleep(1)
        self.driver.find_element(*self.login_field).click() # identifica as tag no site

