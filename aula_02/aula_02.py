# video aula 16
from selenium import webdriver
from time import sleep

'''
Todos os três métodos são métodos do objeto WebDriver.
Todos os três métodos podem ser usados ​​em qualquer momento,
mesmo que a página ainda esteja carregando:

# O método .title retornará uma string com o título da página.
# O método .current_url retornará uma string com a URL completa da página.
# O método .page_source retornará uma string com o código-fonte HTML da página.
'''

browser = webdriver.Chrome()

browser.maximize_window() # maximiza a tela do "site"

browser.get('https://www.saucedemo.com/v1/') # acesso a pagina desejada "site"
print()
print(browser.title) # exibi titulo da pagina (nome da aba)
print(browser.current_url) # exibe o endereço da pagina "site"
print(browser.page_source) # exibe código-fonte HTML da pagina "site"
sleep(3)
