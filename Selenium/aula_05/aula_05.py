# video aula 19
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from time import sleep

'''
Métodos Selenium:

1. click():
Este método "simula o clique do mouse" em um elemento web.
É utilizado para acionar botões, links, imagens e outros elementos interativos.

2. send_keys():
Este método "insere texto em um campo de texto ou caixa de entrada".
É utilizado para preencher formulários, digitar em caixas de pesquisa e realizar
outras ações que exigem a digitação de texto.

4. get_attribute():
Este método "obtém o valor de um atributo" de um elemento web.
É utilizado para recuperar informações como o valor de um campo de texto,
o href de um link ou o título de uma imagem.

5. text:
Este método "retorna o texto" presente em um elemento web.
É utilizado para obter o conteúdo de um texto, título,
legenda ou outro elemento que exiba texto.
'''

browser = webdriver.Chrome()

browser.maximize_window() # maximiza a tela do "site"

browser.get('https://www.saucedemo.com/v1/') # acesso a pagina desejada "site"

# OBS: .find_element() não encontrado causa erro; .find_elements() NÃO ocorre erro

nome_usuario = browser.find_element(By.ID,"user-name") # identifica as tag no site
senha = browser.find_element(By.ID,"password") # identifica as tag no site
botao_login = browser.find_element(By.ID,"login-button")
sleep(1)
nome_usuario.send_keys('standard_user') # inserir texto na tag selecionada
senha.send_keys('secret_sauce') # inserir texto na tag selecionada
sleep(1)
# botao_login.click() # clicar 1x
# ActionChains(browser).double_click(botao_login).perform() # clicar 2x
# ActionChains(browser).context_click(botao_login).perform() # clicar 1x botão direito

botao_login.send_keys(Keys.ENTER) # simula um clicar 1x no "botao_login"

'''
O método .send_keys(Keys.ENTER) é utilizado para simular a tecla "Enter"em
um campo de texto. Isso pode ser útil para realizar diversas ações em websites, como:

Enviar um formulário:
Após preencher os campos de um formulário, utilize .send_keys(Keys.ENTER) no botão
de envio para submetê-lo.
'''
titulo = browser.find_element(By.XPATH, '//div[@class="product_label"]')
print(titulo.text) # exibe o texto dentro da tag
assert titulo.text == 'Products' # teste

foto_mochila = browser.find_element(By.XPATH, '(//img[@class="inventory_item_img"])[1]')
# foto_mochila = browser.find_element(By.XPATH, '(//a[@id])[5]') # ou
# foto_mochila = browser.find_element(By.XPATH, '//img[@src="./img/sauce-backpack-1200x1500.jpg"]') # ou
# foto_mochila = browser.find_element(By.XPATH, '//a[@id="item_4_img_link"]/img[@class="inventory_item_img"]') # ou

print(foto_mochila.get_attribute('src')) # exibe atributo da tag
sleep(3)

