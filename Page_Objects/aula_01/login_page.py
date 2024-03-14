from time import sleep
from selenium.webdriver.common.by import By

import conftest

class LoginPage:
    def __init__(self) -> None:
        # ======================= Iniciar Navegador ==============================
        self.driver = conftest.driver

    def fazer_login(self, usuario, senha):
        sleep(1)
        self.driver.find_element(By.ID,"user-name").send_keys(usuario) # identifica as tag no site
        sleep(1)
        self.driver.find_element(By.ID,"password").send_keys(senha) # identifica as tag no site
        sleep(1)
        self.driver.find_element(By.ID,"login-button").click() # identifica as tag no site

