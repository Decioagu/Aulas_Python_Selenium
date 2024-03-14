# Aulas_Python_Selenium

- O Selenium é um conjunto de ferramentas open-source usadas para automatizar tarefas em navegadores web.  Ele simula a interação do usuário com o navegador, como clicar em botões, preencher formulários e navegar por páginas.
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
- Três métodos do objeto WebDriver.
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
- __click()__: Este método "simula o clique do mouse" em um elemento web.
- __send_keys()__: Este método "insere texto em um campo de texto ou caixa de entrada".
- __get_attribute()__: Este método "obtém o valor de um atributo" de um elemento web.
- __text__: Este método "retorna o texto" presente em um elemento web.
OBS: método __.send_keys(Keys.ENTER)__ é utilizado para simular a tecla __"Enter"__ em um campo de texto, como um click.
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
- __.implicitly_wait()__: Aplicável globalmente a todos os elementos da página.
Define um tempo máximo que o Selenium espera para encontrar um elemento
antes de lançar uma exceção.
---

**Aula_09**
- Um __iframe__ (abreviação de "inline frame") é uma tag HTML que permite incorporar o conteúdo de uma página web dentro de outra página web. Isso significa que você pode exibir uma página dentro de uma área específica de sua própria página, como se fosse uma janela dentro da sua página.

- __/following-sibling::__ é um eixo XPath usado para navegar por um documento XML ou HTML e selecionar
elementos irmãos que vêm depois de um elemento específico, dentro do mesmo elemento pai.

Exemplo de __/following-sibling::__ :
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
- Fechar janela de alerta no site:
	- __.switch_to.alert.accept()__ "identificar alerta e clica"
---

## Pytest

- O __Pytest__ é uma ferramenta gratuita e popular utilizada para automatizar testes em código Python.  Resumidamente, o __Pytest__ auxilia no processo de desenvolvimento de software Python ao garantir a qualidade do código através da automatização de testes.

---

## Page Objects

- No contexto de testes automatizados, o __Page Objects__ é um padrão de design (design pattern) que visa melhorar a organização, manutenção e legibilidade dos testes. Resumidamente, o __Page Objects__ torna os testes mais organizados e fáceis de manter.
