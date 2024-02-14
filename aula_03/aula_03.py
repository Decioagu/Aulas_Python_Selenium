# video aula 17
'''
A principal diferença entre .find_element() e find_elements()
reside no número de elementos que cada método retorna:

- .find_element(): Este método retorna apenas um único elemento da página web
que corresponde ao localizador especificado. Se nenhum elemento for encontrado,
ele lançará uma exceção.

- find_elements(): Este método retorna uma lista de todos os elementos da página web
que correspondem ao localizador especificado. Se nenhum elemento for encontrado,
ele retornará uma lista vazia.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()

browser.maximize_window() # maximiza a tela do "site"

browser.get('https://www.saucedemo.com/v1/') # acesso a pagina desejada "site"

# ========================== .find_element ================================
nome_usuario = browser.find_element(By.ID,"user-name") # identifica as tag no site
senha = browser.find_element(By.ID,"password") # identifica as tag no site
print(nome_usuario)
print(senha)

nome_usuario.send_keys('standard_user') # inserir texto na tag selecionada
senha.send_keys('secret_sauce') # inserir texto na tag selecionada
sleep(3)

# ========================== .find_elements ===============================

# elementos = browser.find_elements(By.CLASS_NAME, "form_input") # retorna lista dos elementos selecionados
# print(elementos)

# nome_x = elementos[0]
# senha_x = elementos[1]
# print(nome_x)
# print(senha_x)
# nome_x.send_keys('standard_user') # inserir texto na tag selecionada
# senha_x.send_keys('secret_sauce') # inserir texto na tag selecionada

# teste automatizado (assert)
# assert len(elementos) == 3, "O número de elementos encontrados foi diferentes"
# sleep(3)

'''

Localizadores do método find_element ou find_elements em Selenium:

1. Por ID:
By.ID - Localiza um elemento pelo seu ID, exemplo:
# driver.find_element(By.ID, "meu_elemento")

2. Por nome:
By.NAME - Localiza um elemento pelo seu nome, exemplo:
# driver.find_element(By.NAME, "nome_usuario")


3. Por classe CSS:
By.CLASS_NAME - Localiza um elemento pela sua classe CSS, exemplo:
# driver.find_element(By.CLASS_NAME, "botao")

4. Por XPath:
By.XPATH - Localiza um elemento usando uma expressão XPath, exemplo:
# driver.find_element(By.XPATH, "//input[@type='submit']")

5. Por CSS selector:
By.CSS_SELECTOR - Localiza um elemento usando um seletor CSS, exemplo:
# driver.find_element(By.CSS_SELECTOR, "input[type='submit']")

6. Por tag name:
By.TAG_NAME - Localiza um elemento pelo seu nome de tag, exemplo:
# driver.find_element(By.TAG_NAME, "input")

7. Por link text:
By.LINK_TEXT - Localiza um link pelo seu texto, exemplo:
# driver.find_element(By.LINK_TEXT, "Clique aqui")

8. Por partial link text:
By.PARTIAL_LINK_TEXT - Localiza um link por uma parte do seu texto, exemplo:
# driver.find_element(By.PARTIAL_LINK_TEXT, "Clique")
'''
