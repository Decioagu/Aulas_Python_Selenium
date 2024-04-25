from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from time import sleep

browser = webdriver.Chrome()

browser.get('http://selenium.dunossauro.live/aula_11_a')
sleep(1)
browser.find_element(By.ID, 'alert').click()
sleep(1)
alerta_01 = browser.switch_to.alert # identificar alerta | (Causa erro se não houver alerta)
print(alerta_01.text) # texto do alerta
sleep(1)
alerta_01.accept() # clicar alerta (OK)
sleep(1)
# ========================================================================================
sleep(1)
browser.find_element(By.ID, 'alert').click()
sleep(3)
alerta_02 = Alert(browser) # clicar alerta (OK) | (Não causa erro se não houver alerta)
sleep(1)
alerta_02.accept() # clicar alerta (OK)
sleep(1)
# ========================================================================================
sleep(1)
browser.find_element(By.ID, 'prompt').click()
sleep(1)
alerta_03 = browser.switch_to.alert
sleep(1)
alerta_03.send_keys('Décio') # prompt
sleep(1)
alerta_03.dismiss()
sleep(1)
# ========================================================================================
sleep(1)
browser.find_element(By.ID, 'prompt').click()
alerta_04 = browser.switch_to.alert
sleep(1)
alerta_04.send_keys("Décio") # prompt
sleep(1)
alerta_04.accept()
sleep(1)

