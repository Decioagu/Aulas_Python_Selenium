# video aula 34
import pytest
from selenium import webdriver

driver: webdriver.Remote

@pytest.fixture()
def setup_teardown():
    # ======================= Iniciar Navegador ==============================
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window() # maximiza a tela do "site"
    driver.get('https://www.saucedemo.com/v1/') # acesso a pagina desejada "site"

    yield # pausar sua execução e retomar mais tarde

    driver.quit()


