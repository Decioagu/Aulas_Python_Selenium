# video aula 40 até 42
import pytest

from login_page import LoginPage

'''
https://docs.pytest.org/en/7.1.x/contents.html
Para executar, P:\REPOSITORIO\PRIVADO\Aulas_Python_Selenium\Page_Objects\aula_07> pytest .\teste_aula_07.py:
ou
Para executar, P:\REPOSITORIO\PRIVADO\Aulas_Python_Selenium\> pytest -v .\Page_Objects.\aula_07.\teste_aula_07.py
'''

@pytest.mark.usefixtures('setup_teardown')
class TesteDriver():
    def teste_driver_selecionar_carrinho(self):

        # ========================== Entrar Login ================================
        login = LoginPage()
        login.fazer_login(usuario='standard_user', senha = 'secret_sauce') # senha = 'secret_sauce'



