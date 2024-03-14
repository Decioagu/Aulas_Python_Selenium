# video aula 39
import pytest
from time import sleep

from login_page import LoginPage
from home_page import HomePage

'''
https://docs.pytest.org/en/7.1.x/contents.html
Para executar, P:\REPOSITORIO\PRIVADO\Aulas_Python_Selenium\Page_Objects\aula_05> pytest .\teste_aula_05.py:
ou
Para executar, P:\REPOSITORIO\PRIVADO\Aulas_Python_Selenium\> pytest -v .\Page_Objects.\aula_05.\teste_aula_05.py
'''

@pytest.mark.usefixtures('setup_teardown')
class TesteDriver():
    def teste_driver_selecionar_carrinho(self):

        # ========================== Entrar Login ================================
        login = LoginPage()
        login.fazer_login(usuario='standard_user', senha='secret_sauce') # senha = 'secret_sauce'

        # ========================== Verifica Login ================================
        home_page = HomePage()
        try:
            home_page.verficar_login_com_sucesso()
            print('Senha correta.')
        except Exception:
            home_page.verficar_login_com_erro()
            print('Senha incorreta.')
        sleep(1)


