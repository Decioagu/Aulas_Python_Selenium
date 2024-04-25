

# Aulas_Python_Selenium

- O Selenium é um conjunto de ferramentas open-source usadas para automatizar tarefas em navegadores web.  Ele simula a interação do usuário com o navegador, como clicar em botões, preencher formulários e navegar por páginas.
---

## Page Objects

- No contexto de testes automatizados, o __Page Objects__ é um padrão de design (design pattern) que visa melhorar a organização, manutenção e legibilidade dos testes. Resumidamente, o __Page Objects__ torna os testes mais organizados e fáceis de manter.
---

## Pytest

- O __Pytest__ é uma ferramenta gratuita e popular utilizada para automatizar testes em código Python.  Resumidamente, o __Pytest__ auxilia no processo de desenvolvimento de software Python ao garantir a qualidade do código através da automatização de testes.
---

## Selenium

**Aula_01**
- Métodos Selenium para navegação:
    - __.refresh()__: Recarrega a página web atualmente aberta no navegador. 
    - __.get(url)__: Navega para uma URL específica abrir página da Web
    - __.back()__: Navega para a página anterior no histórico do navegador.
    - __.forward()__: Navega para a próxima página no histórico do navegador.
    - __.switch_to.new_window()__: Muda o foco para uma nova janela/aba do navegador.  
    - __.close()__: Fecha a janela/aba do navegador atualmente em foco. 
    - __.quit()__: Fecha todas as janelas/abas do navegador e encerra a sessão WebDriver.
---

**Aula_02**
- Três métodos do objeto __WebDriver__.
    - O método __.title__ retornará uma string com o título da página.
    - O método __.current_url__ retornará uma string com a URL completa da página.
    - O método __.page_source__ retornará uma string com o código-fonte HTML da página.
---

**Aula_03**
- Localização de elemento pagina Web:
    - __.find_element()__: Este método retorna apenas um único elemento da página web
    que corresponde ao localizador especificado. Se nenhum elemento for encontrado,
    ele lançará uma exceção.
    - __.find_elements()__: Este método retorna uma lista de todos os elementos da página web
    que correspondem ao localizador especificado. Se nenhum elemento for encontrado,
    ele retornará uma lista vazia.
---

**Aula_04**
- assert é uma instrução em Python que permite verificar se uma determinada condição é verdadeira durante a execução do programa:
    - __is_displayed()__: Verifica se um elemento está visível na tela.
    - __is_enabled()__: Verifica se um elemento está habilitado e pode ser interrompido.
    - __is_selected()__: Verifica se um elemento está selecionado.
---

**Aula_05**
- Métodos Selenium:
- __.click()__: Este método "simula o clique do mouse" em um elemento web.
- __.send_keys()__: Este método "insere texto em um campo de texto ou caixa de entrada".
- __.text__: Este método "retorna o texto" presente em um elemento web.
- __.get_attribute()__: Este método "obtém o valor de um atributo" de um elemento web.
--- 

**Aula_06**
- Métodos Selenium:
- __.implicitly_wait()__ define  um tempo limite global para quanto tempo o WebDriver aguardará que um elemento esteja presente na página antes de lançar uma exceção. É essencialmente uma  "rede de segurança" para evitar que seu script falhe, por não esta carregado.

__Python:__
- browser.find_element(By.XPATH, '(//img[@class="inventory_item_img"])[1]')
---

**Aula_07**
- "__WebDriverWait()__": Especifica um tempo de espera para um único elemento ou condição, como:
    - Condições de Visibilidade:
    - Condições de Presença:
    - Condições de Clique:
    - Condições de Atributo:
    - Condições de Título:
    - Condições de URL:
    - Condições de Janela/Navegador:
    - Condições de Alertas:
    - Condições Lógicas:
---

**Aula_08**
- __dropdowns__ ou __menu suspenso__: são elementos de navegação comuns em sites e aplicativos. Eles funcionam como __caixa de seleção__ que revelam uma lista de opções quando acionadas pelo usuário.
---

**Aula_09**
- Um __iframe__ (abreviação de "inline frame") é uma tag HTML que permite incorporar o conteúdo de uma página web dentro de outra página web. Isso significa que você pode exibir uma página dentro de uma área específica de sua própria página, como se fosse uma janela dentro da sua página.

- __/following-sibling::__ é um eixo XPath usado para navegar por um documento XML ou HTML e selecionar
elementos irmãos que vêm depois de um elemento específico, dentro do mesmo elemento pai.

Exemplo de __"/following-sibling::"__

__HTML:__

- `<body>`
-	`<b style="color:green">Inner Frame Check box :</b>`
-	`<input id="a" type="checkbox">`
- `</body>`

__Python:__

- browser.find_element(By.XPATH,'//b[@style="color:green"]/following-sibling::input[@id="a"]')
---

**Aula_10 e Aula_11**
- Localização de elemento pagina Web por __Tag__ e __texto__:

__Python:__
- browser.find_element(By.XPATH, "//div[@class='inventory_item_name' __and__ text()='Sauce Labs Backpack']").is_displayed()
---

**Aula_12**
- Janelas de alertas:
	- A linha de código __"driver.switch_to.alert"__ é usada para alternar o foco do navegador para um alerta JavaScript. Isso significa que o navegador irá parar de interagir com a página web principal e se concentrará no alerta, permitindo que você acesse e manipule o conteúdo do alerta.
        - __Responder ao alerta__: Use os métodos __accept()__ ou __dismiss()__ para confirmar ou cancelar o alerta, respectivamente.
        - __Inserir dados no alerta__: Se o alerta for um prompt, use o método __sendKeys()__ para inserir o texto desejado.
        - OBS: (Causa erro se não houver alerta)

    - from selenium.webdriver.common.alert import Alert:
        - A __Alert__ classe fornece funcionalidades para interagir com caixas de alerta.
        - OBS: (Não causa erro se não houver alerta)
---

**Aula_13**
- O módulo __"selenium.webdriver.support.events"__ fornece método de class para registrar e responder a eventos do navegador durante a automação com Selenium. Permitindo monitorar e reagir a ações do usuário, como cliques, digitações e navegação.
---

**Aula_14 e Aula_15**
- __"ActionChains"__ simular interações complexas do usuário com elementos da web, como:
    - Movimentos do mouse: Passar o mouse sobre elementos, arrastar e soltar elementos.
    - Clique no botão do mouse: Executar cliques esquerdos, cliques direitos e cliques duplos.
    - Interações com o teclado: Simulação de pressionamentos e liberações de teclas.
    - Ações combinadas: Criação de ações para imitar o comportamento real do usuário.

- A __Keysclasse__ fornece uma coleção de constantes que representam várias teclas do teclado que você pode usar para simular interações do usuário com elementos da web.
-Exemplo:
    - Usamos .send_keys() para inserir texto na barra de pesquisa, podemos utilizar __.send_keys(Keys ENTER)__, para simular um click em uma Tag na Web.
---

**Aula_16**
- from selenium.webdriver import ActionChains, Keys
    - __ActionChains__ permite que você controle movimentos do mouse, cliques pressionamentos de teclado semelhante ao usuário.
        __.move_to_element(element)__: move o cursor do mouse sobre um elemento.
        __.click(element)__: realiza um clique simples no elemento.
        __.double_click(element)__: executa um clique duplo no elemento.
        __.context_click(element)__: clica com o botão direito no elemento (abre o menu de contexto).
        __.send_keys(keys)__: envia sequências de teclas para o campo de foco atual.
        __.pause(valor numérico)__: aguardar em segundo valor numérico
        

    - O método __Keys.ENTER__ é utilizado para simular a tecla "Enter"em um campo de texto. Isso pode ser útil para realizar diversas ações em websites
        - __.key_down(Keys.ENTER)__: pressionar tecla ENTER do teclado para baixo

__Python:__
- browser.find_element(By.XPATH,"//p[contains(text(), 'Eventos de mouse são baseados em ações do mouse.')]")
---

**Aula_17**
- Pop-up é uma janela que aparece no seu navegador sem você pedir.
- No Selenium, os identificadores de janela são usados para gerenciar e alternar entre várias janelas ou guias do navegador associadas a uma única instância do WebDriver.
    - Use para obter o identificador da janela __atual.get_window_handle()__
    - Use para obter todas as alças de janela __abertas.window_handles()__
    - Use para alternar o foco entre as __janelas.switch_to.window(handle)__
    
---

**Aula_18**
- O __".execute_script()"__ é um método poderoso em ferramentas de automação web como o Selenium WebDriver que permite executar scripts JavaScript diretamente no contexto da página web aberta no navegador. Isso oferece flexibilidade para realizar ações que não são diretamente suportadas pelas APIs do Selenium ou para automatizar tarefas complexas que exigem manipulação mais granular da página __browser.execute_script()__.
---
