from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
from time import sleep
import os

# 2. Definir a URL e o local de download:
url = "https://doweb.rio.rj.gov.br/"
download_path = r'C:\Users\SeuUsuario\Downloads'  # Substitua pelo seu diretório de download

# 3. Configurar as opções do Chrome para definir o local de download:
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
}
options.add_experimental_option('prefs', prefs)

# 4. Criar o serviço e o driver do Chrome com as opções definidas:
service = Service('C:/caminho_para_o_seu_driver/chromedriver.exe')  # Substitua pelo caminho para o seu chromedriver
driver = webdriver.Chrome(service=service, options=options)

# 5. Abrir o navegador e navegar até a página:
driver.get(url)

# 6. Localizar o link de download:
link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//img[@id="imagemCapa"]'))
)

# 7. Clicar no link de download:
ActionChains(driver).move_to_element(link).click().perform()

# 8. Esperar o download terminar (você pode usar métodos mais robustos para isso):
while not any(filename.endswith('.pdf') for filename in os.listdir(download_path)):
    sleep(2)

# 9. Fechar o navegador:
driver.quit()
