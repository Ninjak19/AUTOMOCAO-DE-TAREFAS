# passo a passo do projeto


# 1. Abrir o sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui  
import time  

pyautogui.PAUSE = 0.5

#pyautogui.click -> clicar mouse
#pyautogui.press -> apertar uma tecla do teclado
#pyautogui.write -> escrever um texto
#pyautogui.hotkey -> apertar um conjunto de teclas (ctrl c, crtl v, alt tab)

    # abrir o navegador (chrome)
pyautogui.press("win")    
pyautogui.write("chrome")
pyautogui.press("enter")



    # entrar no site do sistema
time.sleep(3)
pyautogui.press("tab")

pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


# 2. Fazer login
pyautogui.click(x=480, y=404)
pyautogui.write("tchulango@tchulango.com.br")
pyautogui.press("tab")
pyautogui.write("coxinha123")
pyautogui.press("enter")
# 3. Abrir/Importador a base de dados de produtos para cadastrar

#pip install pandas numpy openpyxl

import pandas as pd


tabela = pd.read_csv("produtos.csv")

# 4. Cadastrar um produto
#str = string = texto em programacao

for linha in tabela.index:

    #codigo do produto
    codigo = str(tabela.loc[linha,"codigo"])
    #clicar no campo codigo do produto
    pyautogui.click(x=511, y=292)
    #preencher o campo codigo do produto
    pyautogui.write(codigo)
    #passar para o proxim campo
    pyautogui.press("tab")
    #marca do produto
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    #passar para o proximo campo
    pyautogui.press("tab")
    #tipo do produto
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    #passar para o proximo campo
    pyautogui.press("tab")
    #categoria do produto
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    #passar para o proximo campo
    pyautogui.press("tab")
    #preco unitario do produto
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    #passar para o proximo campo
    pyautogui.press("tab")
    #custo do produto
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    #passar para o proximo campo
    pyautogui.press("tab")
    #obs
    obs = (str(tabela.loc[linha,"obs"]))
    if obs != "nan":
        pyautogui.write(obs)
    #passar para o proximo campo
    pyautogui.press("tab")
    #apertar o botao
    pyautogui.press("enter")    

pyautogui.scroll(5000)
# 5. Repetir tudo isso até acabar a lista de produtos
