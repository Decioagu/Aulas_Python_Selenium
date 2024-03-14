from selenium.webdriver.common.by import By

import conftest
from base_page import BasePage

class HomePage(BasePage):
    def __init__(self) -> None:
        # ======================= Iniciar Navegador ==============================
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH,'//div[@class="product_label"]')
        self.erro_field = (By.XPATH, '//h3[@data-test="error"]')

    # ======================= Teste de Login ==============================
    def verficar_login_com_sucesso(self):
        self.verificar_elemento_na_pagina(self.titulo_pagina)

    def verficar_login_com_erro(self):
        self.verificar_elemento_na_pagina(self.erro_field)
