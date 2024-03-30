# video aula 21
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

'''
".implicitly_wait()"  define  um tempo limite global para quanto tempo o WebDriver
aguardará que um elemento esteja presente na página antes de lançar uma exceção.
É essencialmente uma  "rede de segurança" para evitar que seu script falhe
imediatamente se os elementos com os quais você está tentando interagir ainda
não tiverem sido carregados.

Veja como funciona:
Você chama sua instância WebDriver..implicitly_wait(time_in_seconds).
Para todas as pesquisas de elementos subsequentes usando métodos como,
o WebDriver aguardará até o tempo especificado para que
o elemento esteja presente no ".find_element()".
Se o elemento for encontrado dentro do prazo, Seu script continua normalmente.
Se o elemento não for encontrado dentro do limite de tempo, uma exceção como é lançada.
'''

browser = webdriver.Chrome()

browser.implicitly_wait(30) # aguarda

browser.maximize_window() # maximiza a tela do "site"

browser.get('https://chercher.tech/practice/implicit-wait-example') # acesso a pagina desejada "site"

# OBS: .find_element() não encontrado causa erro / em .find_elements() NÃO ocorre erro

checkbox = browser.find_element(By.XPATH, "//input[@type='checkbox']") # identifica as tag no site
assert checkbox.is_displayed() # teste

checkbox.click() # clicar checkbox
# sleep(15) # aguardar 15s
