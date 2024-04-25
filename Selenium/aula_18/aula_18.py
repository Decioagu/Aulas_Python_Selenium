from selenium import webdriver

browser = webdriver.Chrome()

browser.get('http://selenium.dunossauro.live/aula_11_c')

'''
O ".execute_script()" é um método poderoso em ferramentas de automação web como o Selenium
WebDriver que permite executar scripts JavaScript diretamente no contexto da página web
aberta no navegador. Isso oferece flexibilidade para realizar ações que não são
diretamente suportadas pelas APIs do Selenium ou para automatizar tarefas complexas
que exigem manipulação mais granular da página browser.execute_script().

    # Conteúdo Dinâmico: Sites que dependem fortemente de JavaScript para manipulação de
      conteúdo ou atualizações geralmente exigem execução de JavaScript para acessar os
      dados subjacentes. permite que você interaja com esses elementos dinâmicos.execute_script()

    # Interações Complexas: Determinadas ações de página da Web, como rolar para um elemento
    específico que não está no visor ou simular eventos de foco do mouse, podem ser obtidas
    com mais eficiência com JavaScript.

    # Lógica personalizada: Você pode escrever código JavaScript personalizado para executar
    tarefas que não são suportadas diretamente pela API WebDriver. Por exemplo, talvez seja
    necessário analisar dados específicos da estrutura DOM da página.
'''

browser.execute_script('window.open("")')

browser.switch_to.window(
    browser.window_handles[-1]
)

browser.get('http://ddg.gg')
