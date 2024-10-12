'''
Selenium é um conjunto de ferramentas de código aberto multiplataforma para
testes automatizados de aplicações web. Ele simula as ações de um usuário real,
como clicar em botões, inserir dados em formulários e navegar por páginas,
para verificar se a aplicação está funcionando de acordo com o esperado.
https://www.selenium.dev/pt-br/

    Métodos Selenium para navegação:
    # .refresh():
    Recarrega a página web atualmente aberta no navegador. É como pressionar F5 ou o botão de atualizar.
    Útil para conteúdo dinâmico que muda frequentemente e você precisa da versão mais recente.
    Não possui argumentos.

    # .get(url):
    Navega para uma URL específica. É como digitar um endereço na barra de URLs.
    Utilizado para abrir novas páginas ou ir para páginas específicas durante seus testes.

    # .back():
    Navega para a página anterior no histórico do navegador. É como clicar na seta "voltar" do navegador.
    Útil para testes que envolvem retroceder em um fluxo de navegação.
    Não possui argumentos.

    # .forward():
    Navega para a próxima página no histórico do navegador. É como clicar na seta "avançar" do navegador.
    Útil para testes que envolvem avançar em um fluxo de navegação.
    Não possui argumentos.

    # .switch_to.new_window():
    Muda o foco para uma nova janela/aba do navegador. Útil quando o site abre novas janelas/abas.
    Possui diferentes métodos para selecionar a nova janela/aba (por título, handle etc.).
    É importante lidar com a janela anterior após a alternância.

    # .close():
    Fecha a janela/aba do navegador atualmente em foco. É como clicar no "X" da janela/aba.
    Use com cautela, pois pode fechar uma janela indesejada.
    Não possui argumentos.

    # .quit():
    Fecha todas as janelas/abas do navegador e encerra a sessão WebDriver. É como encerrar o navegador por completo.
    Use no final de seus testes para liberar recursos.
    Não possui argumentos.
'''
# video aula 15
from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()

browser.maximize_window() # maximiza a tela do "site"

browser.get('https://doweb.rio.rj.gov.br/') # acesso a pagina desejada "site"
sleep(3)

browser.refresh() # atualizar a pagina "site"
sleep(3)

browser.get('https://www.google.com.br/') # acesso a pagina desejada "site"
sleep(3)

browser.back() # retorna a pagina anterior "site"
sleep(3)

browser.forward() # avança a pagina acessada "site"
sleep(3)

browser.switch_to.new_window("tab") # nova pagina aberta "site"
sleep(3)

browser.close() # fecha a pagina atual "site"
sleep(3)

browser.quit() # fecha o browser
