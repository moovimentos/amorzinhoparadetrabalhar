import pyautogui

INPUT_NUMERO_SEQUENCIAL = (354, 363)
BOTAO_PESQUISAR = (580, 363)
URL_CHROME = (430, 63)
LINK_PROCESSUM_HOME = 'http://processum.telespcelular.com.br:8080/processumweb/modulo/processo/filtro.jsf'

def operacao_amorzinho_para_de_trabalhar():
    print("Amorzinho, você tem 10 segundos pra clicar o mouse na cedula do número do sequencial")
    pyautogui.sleep(10)

    print("Acessando o link do Processum...")
    pyautogui.click(URL_CHROME)  # Clica na barra de URL do Chrome
    pyautogui.typewrite(LINK_PROCESSUM_HOME)  # Digita o link
    pyautogui.press('enter')  # Pressiona Enter para acessar o link

    pyautogui.sleep(5)  # Espera a página carregar

    print("Iniciando a operação...")
    pyautogui.click()  # Clica na posição atual do mouse
    pyautogui.hotkey('ctrl', 'c')  # Copia o número
    
    pyautogui.sleep(1) # Espera
    pyautogui.hotkey('alt', 'tab')  # Alterna para a janela do Processum


    pyautogui.click(INPUT_NUMERO_SEQUENCIAL)  # Clica no campo do número sequencial
    pyautogui.hotkey('ctrl', 'v')  # Cola o número

    pyautogui.click(BOTAO_PESQUISAR) # Clica no botão pesquisar


