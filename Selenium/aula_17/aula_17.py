from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()

browser.get('http://selenium.dunossauro.live/aula_11_b')
sleep(1)
browser.find_element(By.ID, 'popup').click()
sleep(1)

def find_window(content: str):
    wids = browser.window_handles # identifica quantas janelas abertas no navegador
    print("Lista código de paginas:",wids)
    for window in wids:
        browser.switch_to.window(window)
        if content in browser.page_source.lower():
            print(f'Achei linha de texto correspondente: {content}')
            break
'''
"browser.page_source.lower()"
browser: Instância do navegador da Web no como o Selenium WebDriver.
.page_source: Recupera o código-fonte HTML completo da página da Web atual em texto.
.lower(): Converte todos os caracteres de uma string em minúsculas.

'''
sleep(1)
print()
find_window('<h1>popup</h1>') # função encontrar texto
print()
