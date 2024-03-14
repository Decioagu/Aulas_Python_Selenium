# video aula 32
import pytest
from selenium import webdriver

driver: webdriver.Remote
'''
https://docs.pytest.org/en/7.1.x/contents.html
Para executar, P:\REPOSITORIO\PRIVADO\Aulas_Python_Selenium\Pytest> pytest .\teste_aula_01.py:
ou
Para executar, P:\REPOSITORIO\PRIVADO\Aulas_Python_Selenium\> pytest -v .\Pytest.\teste_aula_01.py
'''
@pytest.fixture()
def setup_teardown():
    # ======================= Iniciar Navegador ==============================
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(12)
    driver.maximize_window() # maximiza a tela do "site"
    driver.get('https://www.saucedemo.com/v1/') # acesso a pagina desejada "site"

    yield # pausar sua execução e retomar mais tarde

    driver.quit()


