import pyautogui as py
import pyperclip as pc
import time
from datetime import datetime
import ctypes

time.sleep(5)

py.PAUSE=0.2

# Obter a data atual
data_atual = datetime.now()

# Definir os dias da semana e meses em português
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

data_por_extenso = f"Fortaleza, {data_atual.day + 1} de {meses[data_atual.month - 1]} de {data_atual.year}"

qtdPaginas = 2
qtdLinhas = 3
qtdCards = 3

def get_key_state(key_code):
    """
    Retorna True se a tecla especificada estiver pressionada, False caso contrário.
    """
    return ctypes.windll.user32.GetKeyState(key_code) & 0xFFFF != 0

# Verifica se o NumLock está ativado
if get_key_state(0x90):
    py.press('NumLock')

for pag in range (qtdPaginas):
    for linha in range(qtdLinhas):
        #titulo do livro
        for card in range(qtdCards):
            titulos = {}
            contador = 1
            py.hotkey('ctrl','c')
            titulos[f"titulo{contador}"] = pc.paste()
            py.press('right', presses=7)

            #nome do aluno
            py.hotkey('ctrl','c')
            aluno = pc.paste()
            py.press('down')
            py.hotkey('ctrl','c')
            aluno2 = pc.paste()

            contador = 2
            while(aluno == aluno2):
                py.press("left", presses=7)
                py.hotkey('ctrl','c')
                titulos[f"titulo{contador}"] = pc.paste()
                py.press("right", presses=7)
                py.press('down')
                py.hotkey('ctrl','c')
                aluno2 = pc.paste()
                contador += 1

            py.press("left", presses=7)

            #serie e turma
            py.hotkey('alt','tab')
            pc.copy(aluno)
            py.hotkey('ctrl','v')
            py.press('enter')
            time.sleep(1)
            py.press('enter',presses=4)
            py.press('tab', presses=5)
            py.press('enter')
            py.press('tab')
            py.press('down', presses=31)

            #serie
            py.press('enter')
            py.rightClick(x=439,y=381)
            py.press('down',presses=6)
            py.press('enter')
            py.hotkey('ctrl','c')
            serie = pc.paste()
            py.press('enter')
            py.press('down')

            #turno e turma
            py.press('enter')
            py.rightClick(x=439,y=381)
            py.press('down',presses=6)
            py.press('enter')
            py.hotkey('ctrl','c')
            turma = pc.paste()
            py.press('enter')
            py.press('down')

            py.press('enter')
            py.rightClick(x=439,y=381)
            py.press('down',presses=6)
            py.press('enter')
            py.hotkey('ctrl','c')
            turno = pc.paste()
            py.press('enter')
            py.press('f12')
            py.press('up')
            py.press('enter')
            py.press('up', presses=2)

            #passar para a planilha
            with py.hold('alt'):
                py.press('tab', presses=2)
            time.sleep(1)

            #escrever o nome do aluno
            pc.copy("Nome: " + aluno)
            py.hotkey('ctrl','v')
            py.press('enter', presses=2)

            # escrever o ano do aluno
            py.press('tab')
            pc.copy("Ano: " + serie[:7] + " / " + turno + turma)
            py.hotkey('ctrl','v')
            py.press('enter', presses=2)

            #titulos no cartao
            py.press('down')
            #verifica se há mais de um titulo


            numTitle = 1
            for i in range(len(titulos)):
                pc.copy(str(numTitle)+ ". " + titulos["titulo" + str(numTitle)].split(':')[0] if ':' in titulos["titulo" + str(numTitle)] else str(numTitle)+ ". " + titulos["titulo" + str(numTitle)])
                py.hotkey('ctrl','v')
                py.press('enter', presses=2)
                numTitle += 1

            if(len(titulos)>2):
                py.press('down')
                pc.copy(data_por_extenso)
                py.hotkey('ctrl','v')
                py.press('up')
                py.press('right')
                py.press('right')
                time.sleep(0.5)
                py.press('up')
                py.press('up')
                py.press('up')
                py.press('up')
                py.press('up')
                py.press('up')
                time.sleep(0.5)
                py.press('right')
            elif(len(titulos) > 1 and len(titulos) <= 2 ):
                py.press('delete')
                py.press('down')
                py.press('down')
                pc.copy(data_por_extenso)
                py.hotkey('ctrl','v')
                py.press('up')
                py.press('right')
                py.press('right')
                time.sleep(0.5)
                py.press('up')
                py.press('up')
                py.press('up')
                py.press('up')
                py.press('up')
                py.press('up')
                time.sleep(0.5)
                py.press('right')
            else:
                py.press('delete')
                py.press('down')
                py.press('delete')
                py.press('down')
                py.press('down')
                pc.copy(data_por_extenso)
                py.hotkey('ctrl','v')
                py.press('up')
                py.press('right')
                py.press('right')
                time.sleep(0.5)
                py.press('up')
                py.press('up')
                py.press('up')
                py.press('up')
                py.press('up')
                py.press('up')
                time.sleep(0.5)
                py.press('right')


            py.hotkey('alt','tab')

            with py.hold('alt'):
                py.press('tab', presses=2)
            time.sleep(1)

        with py.hold('alt'):
            py.press('tab', presses=2)
        time.sleep(1)

        for i in range(12):
            py.press('down')

        py.press('home')
        py.press('right')

        for i in range(2):
            with py.hold('alt'):
                py.press('tab', presses=2)
            time.sleep(1)

    with py.hold('alt'):
        py.press('tab', presses=2)
    time.sleep(1)
    # logica para imprimir
    py.hotkey('ctrl','p')
    time.sleep(1)
    py.press('tab')
    py.press('enter')
    time.sleep(3)
    py.press('enter')

    #restet
    for press in range(32):
        py.press('up')

    for i in range(2):
        with py.hold('alt'):
            py.press('tab', presses=2)
        time.sleep(1)
