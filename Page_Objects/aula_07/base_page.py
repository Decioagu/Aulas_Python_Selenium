import conftest

class BasePage:
    def __init__(self) -> None:
        self.driver = conftest.driver

    # find_element()
    def encontrar_elemento(self, localizar):
        return self.driver.find_element(*localizar)

    # def encontrar_elementos(self, localizar):
    #     return self.driver.find_elements(*localizar)

    # send_keys()
    def escrever(self, localizar, texto):
        return self.encontrar_elemento(localizar).send_keys(texto)

    # click()
    def clicar(self, localizar):
        return self.encontrar_elemento(localizar).click()

    # .is_displayed()
    def verificar_elemento_na_pagina(self, localizar):
        try:
            return self.encontrar_elemento(localizar).is_displayed(), "Não foi encontrado" # True
        except Exception:
            return False

    # back()
    def voltar_pagina(self):
        return self.driver.back()

    # quit()
    def finalizar(self):
        return self.driver.quit()

    def verficar_login_com_sucesso(self, localizar):
        return self.verificar_elemento_na_pagina(localizar)

    def verficar_login_com_erro(self, localizar):

        teste = self.encontrar_elemento(localizar).text

        if teste == 'Epic sadface: Username and password do not match any user in this service':
            assert self.encontrar_elemento(localizar).text == 'Epic sadface: Username and password do not match any user in this service'
        else:
            assert self.encontrar_elemento(localizar).text == 'Epic sadface: Password is required'
        self.finalizar()



