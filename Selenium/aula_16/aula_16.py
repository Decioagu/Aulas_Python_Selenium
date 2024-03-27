# video aula 19
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from time import sleep

browser = webdriver.Chrome()

browser.maximize_window() # maximiza a tela do "site"

browser.get('https://selenium.dunossauro.live/caixinha') # acesso a pagina desejada "site"

caixa = browser.find_element(By.ID,"caixa") # identifica as tag no site
titulo = browser.find_element(By.XPATH,"//p[contains(text(), 'Eventos de mouse são baseados em ações do mouse.')]") # identifica as tag no site

ac = ActionChains(browser)
ac.pause(1)

ac.move_to_element(caixa).perform() # focar elemento
ac.pause(1)

ac.click(caixa).perform() # clicar 1x
ac.pause(1)

ac.double_click(caixa).perform() # clicar 2
ac.pause(1)

ac.key_down(Keys.CONTROL) # tecla ENTER
ac.click(caixa).perform() # clicar 1x
ac.pause(1)

ac.key_down(Keys.SHIFT) # tecla ENTER
ac.click(caixa).perform() # clicar 1x
ac.pause(1)

ac.key_up(Keys.CONTROL) # tecla ENTER
ac.key_down(Keys.SHIFT) # tecla ENTER
ac.click(caixa).perform() # clicar 1x
ac.pause(1)

ac.key_up(Keys.SHIFT) # tecla ENTER
ac.click(caixa).perform() # clicar 1x
ac.pause(1)

ac.move_to_element(caixa).perform() # focar elemento
ac.context_click(caixa).perform() # clicar 1x botão direito
ac.pause(2)

ac.move_to_element(titulo).perform() # focar elemento
ac.pause(3)

'''
O método .send_keys(Keys.ENTER) é utilizado para simular a tecla "Enter"em
um campo de texto. Isso pode ser útil para realizar diversas ações em websites, como:

Enviar um formulário:
Após preencher os campos de um formulário, utilize .send_keys(Keys.ENTER) no botão
de envio para submetê-lo.
'''
sleep(3)
# Fecha o navegador após a operação ser concluída
browser.quit()

