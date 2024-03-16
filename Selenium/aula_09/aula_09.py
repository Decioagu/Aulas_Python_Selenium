# video aula 25

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

'''
# pip install webdriver-manager
    O webdriver-manager é uma biblioteca que facilita o gerenciamento de drivers de
    navegador para automação web em Python. Ele automatiza o download e a instalação
    dos drivers específicos para a versão do navegador que você está usando,
    simplificando e agilizando seu processo de desenvolvimento.
'''
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.implicitly_wait(12)
'''
"implicitly_wait": Aplicável globalmente a todos os elementos da página.
Define um tempo máximo que o Selenium espera para encontrar um elemento
antes de lançar uma exceção.
'''
browser.maximize_window() # maximiza a tela do "site"

browser.get('https://chercher.tech/practice/frames-example-selenium-webdriver') # acesso a pagina desejada "site"

'''
Um iframe (abreviação de "inline frame") é uma tag HTML que permite incorporar o
conteúdo de uma página web dentro de outra página web. Isso significa que você
pode exibir uma página dentro de uma área específica de sua própria página,
como se fosse uma janela dentro da sua página.
'''
iframe1 = browser.find_element(By.ID, 'frame1')  # entra pagina web
browser.switch_to.frame(iframe1)
topic = browser.find_element(By.XPATH,'//b[@id="topic"]/following-sibling::input[@type="text"]')
'''
/following-sibling::é um eixo XPath usado para navegar por um documento XML ou HTMLe selecionar
elementos irmãos que vêm depois de um elemento específico, dentro do mesmo elemento pai.
'''
topic.send_keys("Décio Santana")
sleep(5)

iframe3 = browser.find_element(By.ID, 'frame3') # entra pagina web
browser.switch_to.frame(iframe3)
topic = browser.find_element(By.XPATH,'//b[@style="color:green"]/following-sibling::input[@id="a"]')
topic.click()
sleep(2)

browser.switch_to.default_content()  # sair pagina web

iframe2 = browser.find_element(By.ID, 'frame2') # entra pagina web
browser.switch_to.frame(iframe2)
dropdown_animals = Select(browser.find_element(By.XPATH,"//select[@id='animals']"))
dropdown_animals.select_by_value("avatar") # selecionar por valor
sleep(5)

