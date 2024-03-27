from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

'''
O módulo "selenium.webdriver.support.events" fornece classes e interfaces para registrar
e responder a eventos do navegador durante a automação com Selenium.

Importância:
# Permite monitorar e reagir a ações do usuário, como cliques, digitações e navegação.
# Facilita o desenvolvimento de testes automatizados mais robustos e confiáveis.
# Útil para depuração e logging de atividades do navegador.

Classes e Interfaces:

# EventFiringWebDriver: Uma classe que encapsula um WebDriver e fornece
  métodos para registrar ouvintes de eventos.

# AbstractEventListener: Uma interface que define métodos para lidar com
  diferentes tipos de eventos do navegador.

# WebDriverEventListener: Uma subclasse de AbstractEventListener que fornece
  implementações vazias para todos os métodos de eventos.

# EventFiringWebElement: Uma classe que encapsula um WebElement e fornece
  métodos para registrar ouvintes de eventos.
'''

class MyListener(AbstractEventListener):
    def after_quit(self, driver) -> None:
        print()
        print(f"Fechando navegador...")

    def after_navigate_to(self, url, driver):
        print()
        print(f"Navegador {url} aberto.")

    def after_click(self, element, driver) -> None:
        print(f'Depois de clicado no elemento...')

    def before_click(self, element, driver):
        print()
        print(f"Antes de clicar no elemento...")

    def before_navigate_to(self, url, driver):
        print()
        print(f"Navegando para: {url}")

driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
driver.get("https://www.google.com/")

driver.find_element(By.NAME,"q").send_keys("Selenium") # escrever em campo

sleep(5)
driver.find_element(By.NAME,"btnK").click() # clicar elemento
sleep(5)

driver.quit() # fecha o browser
