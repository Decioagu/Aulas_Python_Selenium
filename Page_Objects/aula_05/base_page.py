import conftest

class BasePage:
    def __init__(self) -> None:
        self.driver = conftest.driver


    def encontrar_elemento(self, localizar):
        return self.driver.find_element(*localizar)

    # def encontrar_elementos(self, localizar):
    #     return self.driver.find_elements(*localizar)

    def escrever(self, localizar, texto):
        return self.encontrar_elemento(localizar).send_keys(texto)

    def clicar(self, localizar):
        return self.encontrar_elemento(localizar).click()

    def verificar_elemento_na_pagina(self, localizar):
        return self.encontrar_elemento(localizar).is_displayed(), "Não foi encontrado"
