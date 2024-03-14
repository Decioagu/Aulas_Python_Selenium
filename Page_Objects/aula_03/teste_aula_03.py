# video aula 36
import pytest
from time import sleep

from login_page import LoginPage
'''
https://docs.pytest.org/en/7.1.x/contents.html
Para executar, P:\REPOSITORIO\PRIVADO\Aulas_Python_Selenium\Page_Objects\aula_03> pytest .\teste_aula_03.py:
ou
Para executar, P:\REPOSITORIO\PRIVADO\Aulas_Python_Selenium\> pytest -v .\Page_Objects.\aula_03.\teste_aula_03.py
'''

@pytest.mark.usefixtures('setup_teardown')
class TesteDriver():
    def teste_driver_selecionar_carrinho(self):

        # ========================== Entrar Login ================================
        login = LoginPage()
        login.fazer_login(usuario='standard_user', senha='secret_sauce')
        sleep(3)


