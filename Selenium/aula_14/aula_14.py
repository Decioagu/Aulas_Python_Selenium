from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

from time import sleep

browser = webdriver.Chrome()

browser.maximize_window() # maximiza a tela do "site"

browser.get('https://selenium.dunossauro.live/aula_08_a') # acesso a pagina desejada "site"

# ========================== .find_element ================================
texto = browser.find_element(By.XPATH,"//textarea") # identifica as tag no site

texto.send_keys('selenium') # inserir texto na tag selecionada
sleep(2)

# digitação no teclado tecla por tecla
ac = ActionChains(browser)
'''
"ActionChains" simular interações complexas do usuário com elementos da web, como:

# Movimentos do mouse: Passar o mouse sobre elementos, arrastar e soltar elementos.
# Clique no botão do mouse: Executar cliques esquerdos, cliques direitos e cliques duplos.
# Interações com o teclado: Simulação de pressionamentos e liberações de teclas.
# Ações combinadas: Criação de ações para imitar o comportamento real do usuário.
'''
ac.move_to_element(texto) # focar elemento
ac.key_down(Keys.ENTER) # tecla ENTER
ac.perform() # acionar ações acima
sleep(3)
ac.key_down(Keys.SHIFT) # tecla SHIFT
ac.key_down('s') # botão "p" fica precionado
ac.key_up("s") # botão "p" retorna na condição normal
ac.key_down('e') # botão "p" fica precionado
ac.key_up("e") # botão "p" retorna na condição normal
ac.key_down('l') # botão "p" fica precionado
ac.key_up("l") # botão "p" retorna na condição normal
ac.key_down('e') # botão "p" fica precionado
ac.key_up("e") # botão "p" retorna na condição normal
ac.perform() # acionar ações acima
sleep(3)
ac.key_down('n') # botão "p" fica precionado
ac.key_up("n") # botão "p" retorna na condição normal
ac.key_down('i') # botão "p" fica precionado
ac.key_up("i") # botão "p" retorna na condição normal
ac.key_down('u') # botão "p" fica precionado
ac.key_up("u") # botão "p" retorna na condição normal
ac.key_down('m') # botão "p" fica precionado
ac.key_up("m") # botão "p" retorna na condição normal
ac.perform() # acionar ações acima

ac.key_up(Keys.SHIFT).perform() # tecla SHIFT
'''
A Keysclasse fornece uma coleção de constantes que representam várias teclas do
teclado que você pode usar para simular interações do usuário com elementos da web.
Exemplo:
Usamos .send_keys() para inserir texto na barra de pesquisa, podemos utilizar
.send_keys(Keys.ENTER), para simular um click em uma Tag da WEB.
'''
sleep(3)
# Fecha o navegador após a operação ser concluída
browser.quit()
