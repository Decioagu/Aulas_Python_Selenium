from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date
from pathlib import Path
from time import sleep
import requests
import os

hoje = (date.today().strftime('%d/%m/%Y')) # campo de inserção de data (dd/mm/aaaa)

def download_pfd(data = str(hoje)):
    print(data)

    # 1. definir caminho da pasta raiz
    PASTA_RAIZ = Path(__file__).parent

    nova_pasta = PASTA_RAIZ / 'PDF' # caminho nova_pasta.
    nova_pasta.mkdir(exist_ok=True) # exist_ok=True para não da erro se existir pasta (criar nova pasta)

    PASTA_NOVA = PASTA_RAIZ / nova_pasta # caminho nova_pasta.

    # 2. Definir a pasta de download padrão antes de iniciar a automação.
    options = webdriver.ChromeOptions() # definir navegador Chrome (Google)
    options.add_experimental_option("prefs", {"download.default_directory": str(PASTA_NOVA)})

    # 3. Abrir o navegador:
    driver = webdriver.Chrome(options=options) # (options=options) = # 2. Definir a pasta de download padrão
    driver.maximize_window() # maximiza a tela do "site"
    url = "https://doweb.rio.rj.gov.br/"
    driver.get(url) # abrir

    # 4. Definir data de edição para download
    data_PDF = driver.find_element(By.ID,"dataEdicaoPortal") # tag "data de edição"
    data_PDF.clear() # limpar campo
    sleep(2)

    '''
    A linha de código "driver.switch_to.alert" é usada para alternar o foco do navegador
    para um alerta JavaScript. Isso significa que o navegador irá parar de interagir
    com a página web principal e se concentrará no alerta, permitindo que você acesse
    e manipule o conteúdo do alerta.

    Quando usar:

    Ler a mensagem do alerta: Use o método "getText()" para recuperar a mensagem exibida no alerta.
    Responder ao alerta: Use os métodos "accept()" ou "dismiss()" para confirmar ou cancelar o alerta,
    respectivamente.
    Inserir dados no alerta: Se o alerta for um prompt, use o método "sendKeys()" para inserir
    o texto desejado.
    '''

    # alerta
    alerta = driver.switch_to.alert # identificar alerta
    sleep(2)
    alerta.accept() # clicar alerta
    sleep(2)

    # tag "data de edição"
    data_PDF.send_keys(data) # inserir texto na tag "data de edição"

    # clicar botão "OK"
    botaõ_data_PDF = driver.find_element(By.XPATH,'//input[@class="btn col-xs-2 col-sm-3 col-md-1 col-lg-1 "]') # identifica as tag no site
    botaõ_data_PDF.click() # click na caixa da pagina "site"
    sleep(2)

    # caso a data seja inexistente
    try:
        alerta = driver.switch_to.alert.text
        sleep(2)
        if not alerta == '':
            print('Data não existente!!!')
            # FIM retorno
            return False
    except Exception as erro:
        # print(erro.__class__, erro) # ver class do erro
        print('Aguardar download...')

    # 5. Localizar tag para download:
    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//img[@id="imagemCapa"]'))
    )

    # 6. Clicar na tag de download:
    ActionChains(driver).move_to_element(link).click().perform()

    # 7. Esperar o download terminar:
    tempo_maximo_download = 10 # "tempo_maximo_download" em segundos
    arquivo_em_download = ''
    while True:
        ok = False
        sleep(1) # tempo do ciclo
        # percorrer lista de arquivo na "PASTA_NOVA"
        for arquivo_pdf in os.listdir(PASTA_NOVA):
            # se extensão do arquivo for ".crdownload" continuar download
            if arquivo_pdf.endswith(".crdownload"):
                print('Fazendo download...')
                ok = False
                tempo_maximo_download-=1
                arquivo_em_download = arquivo_pdf
                break
            else:
                ok = True
        # se downlode finalizado ou "tempo_maximo_download" acabar
        if ok or tempo_maximo_download == 0:
            # excluir arquivo download incompleto
            try:
                os.unlink(PASTA_NOVA / arquivo_em_download)
                print('Arquivo download incompleto excluído...')
            except OSError as e:
                print('Download finalizado...')

            break

    # 8. Fechar o navegador:
    driver.quit()

    # mensagem final
    print('FIM download_pdf...')

    # FIM retorno
    return True

# Verificar se internet esta on-line
def verifica_conexao_internet():
    try:
        # Faz uma requisição para o Google
        requests.get('https://www.google.com.br/', timeout=5)
        print("Conectado à internet!")
        texto_conexao = "Conectado à internet!"
        return texto_conexao
    except requests.ConnectionError:
        # Se a requisição falhar, retorna False
        print("Sem conexão com a internet.")
        texto_conexao = "Sem conexão com a internet."
        return texto_conexao

if __name__ == '__main__':
    download_pfd()

