from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
from time import sleep
import os


# 1. Definir a URL e o local de download:
url = "https://doweb.rio.rj.gov.br/"
download_path = Path(__path__).parents

# 2. Definir a pasta de download padrão antes de iniciar a automação.
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {"download.default_directory": download_path})

# 3. Abrir o navegador e navegar até a página:
driver = webdriver.Chrome(options=options) # (options=options) = # 1.
driver.get(url)

# 4. Localizar o link de download:
link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//img[@id="imagemCapa"]'))
)

# 5. Clicar no link de download:
ActionChains(driver).move_to_element(link).click().perform()

# 6. Esperar o download terminar:
while not os.path.exists(os.path.join(download_path, "arquivo.pdf")):
    sleep(2)
    # 7. Fechar o navegador:
    driver.quit()



