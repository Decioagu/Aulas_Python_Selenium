# video aula 22

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep

'''
"WebDriverWait": Especifica um tempo de espera para um único elemento ou condição.
Permite maior controle e flexibilidade para esperar por elementos específicos.
'''
browser = webdriver.Chrome()

browser.maximize_window() # maximiza a tela do "site"

browser.get('https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver') # acesso a pagina desejada "site"

# Esperar até que o elemento esteja presente
wait = WebDriverWait(browser, 15) # argumento

'''
Condições de Alertas:
alert_is_present() - Espera até que um alerta esteja presente.
'''
botao_alerta = browser.find_element(By.ID, "alert") # instância
botao_alerta.click()
aguardar_alerta = wait.until(expected_conditions.alert_is_present())
print(aguardar_alerta.text)
sleep(2)
# alerta
browser.switch_to.alert.accept() #identificar alerta e clica
sleep(2)

'''
Condições de Atributo:
text_to_be_present_in_element(locator, text) - Espera até que o texto esteja presente no elemento.
'''
botao_alterar_texto = browser.find_element(By.XPATH, "//button[@id='populate-text']")
botao_alterar_texto.click()
aguardar_botao_alterar_texto = wait.until(expected_conditions.text_to_be_present_in_element((By.XPATH, "//h2[@class='target-text']"), 'Selenium Webdriver'))
print(aguardar_botao_alterar_texto)
assert aguardar_botao_alterar_texto
sleep(2)

'''
Condições de Clique:
element_to_be_clickable(locator) - Espera até que o elemento esteja visível, habilitado e clicável.
'''
botao_de_ativacao = browser.find_element(By.XPATH, '//button[@id="display-other-button"]')
botao_de_ativacao.click()
aguardar_botao_de_ativacao = wait.until(expected_conditions.element_to_be_clickable((By.ID, 'hidden')))
print(aguardar_botao_de_ativacao.text)
assert aguardar_botao_de_ativacao.text == 'Enabled'
sleep(2)

'''
Condições de Clique:
element_to_be_clickable(locator) - Espera até que o elemento esteja visível, habilitado e clicável.
'''
botao_de_ativacao = browser.find_element(By.XPATH, '//button[@id="enable-button"]')
botao_de_ativacao.click()
aguardar_botao_de_ativacao = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[@id="disable"]')))
print(aguardar_botao_de_ativacao.text)
assert aguardar_botao_de_ativacao.text == 'Button'
sleep(2)

'''
Condições de Clique:
# element_to_be_selected(locator) - Espera até que o elemento esteja selecionado (para caixas de seleção).
'''
botao_caixa_de_selecao = browser.find_element(By.XPATH, '//button[@id="checkbox"]')
botao_caixa_de_selecao.click()
aguardar_caixa_de_selecao = wait.until(expected_conditions.element_located_to_be_selected((By.XPATH, '//input[@id="ch"]')))
print(aguardar_caixa_de_selecao)
sleep(2)

# '''
# Lista de Métodos expected_conditions em Selenium:
# Condições de Visibilidade:
# # visibility_of(locator) - Espera até que o elemento esteja visível e ocupando espaço no DOM.
# # visibility_of_all_elements_located(locator) - Espera até que todos os elementos estejam
# visíveis e ocupando espaço no DOM.
# # invisibility_of_element_located(locator) - Espera até que o elemento esteja invisível no DOM.
# # invisibility_of_all_elements_located(locator) - Espera até que todos os elementos
# estejam invisíveis no DOM.

# Condições de Presença:
# # presence_of_element_located(locator) - Espera até que o elemento esteja presente no DOM.
# # presence_of_all_elements_located(locator) - Espera até que todos os elementos estejam presentes no DOM.
# # staleness_of(element) - Espera até que o elemento não esteja mais presente no DOM
# (útil para verificar se um elemento foi removido).

# Condições de Clique:
# # element_to_be_clickable(locator) - Espera até que o elemento esteja visível, habilitado e clicável.
# # element_to_be_selected(locator) - Espera até que o elemento esteja selecionado
# (para caixas de seleção e botões de rádio).

# Condições de Atributo:
# # text_to_be_present_in_element(locator, text) - Espera até que o texto esteja presente no elemento.
# # text_to_be_present_in_element_value(locator, text) - Espera até que o texto esteja presente no
# valor do atributo do elemento.value
# # attribute_to_be_equal(locator, attribute, value) - Espera até que o valor do atributo
# do elemento seja igual ao valor especificado.

# Condições de Título:
# # title_is(title) - Espera até que o título da página seja igual ao título especificado.
# # title_contains(title) - Espera até que o título da página contenha o título especificado.

# Condições de URL:
# # url_to_be(url) - Espera até que a URL da página seja igual à URL especificada.
# # url_to_contain(url) - Espera até que a URL da página contenha a URL especificada.

# Condições de Janela/Navegador:
# # number_of_windows_to_be(number) - Espera até que o número de janelas abertas seja
# igual ao número especificado.
# # window_to_be_switched_to(window) - Espera até que a janela especificada seja a janela ativa.

# Condições de Alertas:
# # alert_is_present() - Espera até que um alerta esteja presente.

# Condições Lógicas:
# # any_of(expected_conditions) - Espera até que qualquer uma das condições especificadas seja verdadeira.
# # all_of(expected_conditions) - Espera até que todas as condições especificadas sejam verdadeiras.

# Observações:
# Esta lista não é exaustiva. Existem outros métodos disponíveis no Selenium.ExpectedConditions
# A sintaxe dos métodos pode variar ligeiramente de acordo com a linguagem de
# programação que você está usando.
# É importante consultar a documentação do Selenium para obter mais informações
# sobre cada método e como utilizá-lo de forma eficaz.
# '''

