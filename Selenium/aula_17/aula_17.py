# video aula 19
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from time import sleep

browser = webdriver.Chrome()

browser.maximize_window() # maximiza a tela do "site"

browser.get('https://www.w3schools.com/html/html5_draganddrop.asp') # acesso a pagina desejada "site"

# texto = browser.find_element(By.XPATH, "//p[contains(text(),'In HTML, any element can be dragged and dropped.')]")  # entra pagina web
# texto = browser.find_element(By.XPATH, "//p[contains(text(),'Drag the W3Schools image into the rectangle.')]")  # entra pagina web



# Localize os elementos de origem e destino
elemento_origem = browser.find_element(By.ID,"div1")
elemento_destino = browser.find_element(By.ID,"div2")

ac = ActionChains(browser)
ac.pause(1)
ac.move_to_element(elemento_origem).perform() # focar elemento
ac.key_down(elemento_origem) # tecla ENTER
ac.pause(2)
ac.move_to_element(elemento_destino).perform()
ac.key_up(elemento_destino) # tecla ENTER
# ac.move_to_element(texto).perform() # focar elemento
# ac.pause(2)
# # Encadeie a ação de arrastar e soltar
# ac.drag_and_drop(elemento_origem, elemento_destino).perform()
ac.pause(2)

# Fecha o navegador após a operação ser concluída
browser.quit()


