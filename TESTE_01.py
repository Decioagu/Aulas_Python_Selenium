from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
from time import sleep
import os

# 2. Definir a URL e o local de download:
url = "https://doweb.rio.rj.gov.br/"
download_path = Path(__file__).parent
pasta = Path(__file__).parent

# 3. Abrir o navegador e navegar até a página:
driver = webdriver.Chrome()
driver.get(url)

# 4. Localizar o link de download:
link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//img[@id="imagemCapa"]'))
)

# 5. Clicar no link de download:
ActionChains(driver).move_to_element(link).click().perform()
# sleep(2)

# 6. Esperar o download terminar:
# while not os.path.exists(os.path.join(download_path, f"{x}")):
#     sleep(1)
#     driver.quit()

# 7. Fechar o navegador:
driver.quit()
