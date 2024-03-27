from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from time import sleep

browser = webdriver.Chrome()

browser.maximize_window() # maximiza a tela do "site"

browser.get('https://selenium.dunossauro.live/keyboard') # acesso a pagina desejada "site"

# ========================== .find_element ================================
html = browser.find_element(By.XPATH, 'html') # identifica as tag no site

html.send_keys('rty') # inserir texto na tag selecionada
ac = ActionChains(browser)
ac.key_down('q') # botão "q" fica precionado
ac.key_down('p') # botão "p" fica precionado
# ac.key_down(Keys.SHIFT) # habilite e veja o efeito
ac.key_up("p") # botão "p" retorna na condição normal
ac.key_down('a') # botão "p" fica precionadoac.perform()
# ac.key_up(Keys.SHIFT) # habilite e veja o efeito
ac.key_down('z') # botão "q" fica precionado
ac.perform()
sleep(5)
# Fecha o navegador após a operação ser concluída
browser.quit()
