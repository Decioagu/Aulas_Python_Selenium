# video aula 18
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

'''
Métodos Selenium para verificar o estado de elementos:

1. is_displayed():
Verifica se um elemento está visível na tela.
Útil para garantir que um elemento está presente e pode ser interrompido.
Retorna True se o elemento estiver visível e False se não estiver.

2. is_enabled():
Verifica se um elemento está habilitado e pode ser interrompido.
Útil para garantir que um elemento pode ser clicado, preenchido ou usado de outra forma.
Retorna True se o elemento estiver habilitado e False se não estiver.

3. is_selected():
Verifica se um elemento está selecionado (aplica-se a caixas de seleção, opções de menu etc.).
Útil para verificar o estado de seleção de um elemento.
Retorna True se o elemento estiver selecionado e False se não estiver.
'''

browser = webdriver.Chrome()

browser.maximize_window() # maximiza a tela do "site"

browser.get('https://demo.applitools.com/') # acesso a pagina desejada "site"

# OBS: .find_element() não encontrado causa erro; .find_elements() NÃO ocorre erro

nome_usuario = browser.find_element(By.ID,"username") # identifica as tag no site
senha = browser.find_element(By.ID,"password") # identifica as tag no site
caixa_de_checagem = browser.find_element(By.CLASS_NAME, "form-check-input") # identifica as tag no site
# caixa_de_checagem = browser.find_element(By.XPATH, '//input[@class="form-check-input"]') # outra forma
sleep(2)
# verifica se um elemento está visível atualmente na página da Web (True ou False)
print(nome_usuario.is_displayed())
assert nome_usuario.is_displayed() # teste

# determinar se um elemento está atualmente interativo em uma página da Web (True ou False)
print(senha.is_enabled())
assert senha.is_enabled() # teste

# verificar se um elemento está selecionado no momento (True ou False)
print(caixa_de_checagem.is_selected()) # ex: checkbox
assert not caixa_de_checagem.is_selected() # teste
sleep(2)

caixa_de_checagem.click() # click na caixa da pagina "site"
print(caixa_de_checagem.is_selected()) # ex: checkbox
assert caixa_de_checagem.is_selected() # teste
sleep(2)

'''
Os métodos "assert" em Selenium são usados ​​para verificar se as condições
esperadas são atendidas durante a execução de seus testes de automação.
Eles permitem comparar valores reais com valores esperados e gerar falhas
de teste se as comparações falharem.
'''


