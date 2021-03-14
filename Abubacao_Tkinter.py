"""
Com base na estação atual fornece informações para cuidar de plantas
"""

from datetime import date, datetime
from tkinter import *

data_atual = date.today()


def estacao(data_atual):
    if data_atual.month in range(3,7):
        if data_atual.month == 4 or data_atual.month == 5 or (data_atual.month == 3 and data_atual.day >=21):
            estacao = 'Outono'
        else: 
            estacao = 'Verão' if (data_atual.month == 3 and data_atual.day <= 21) else 'Inverno'

    elif data_atual.month in range(7,10):
        estacao = 'Primavera' if data_atual.month == 9 and data_atual.day >=23 else 'Inverno'
    elif data_atual.month in range(10,13):
        estacao = 'Verão' if data_atual.month == 12 and data_atual.day >=21 else 'Primavera'
    else:
        estacao = 'Verão'
    return estacao


def informacoes(estacao, tipo):
    
    if estacao == 'Verão':
        l1 = 'Adubo: Manutenção: NPK 10:10:10, Alto K, ex.: NPK 6:6:12'
        l2 = 'Rega : Abundante'
        l3 = 'Poda: Ramos'
        l4 = 'Transplantação: Não'
        if tipo == 'Adubo':
            return l1
        elif tipo == 'Rega':
            return l2
        elif tipo == 'Poda':
            return l3
        elif tipo == 'Transplantação':
            return l4
        
    elif estacao == 'Inverno':   
        l1 = 'Adubo: Não adubar'
        l2 = 'Rega : Moderada'
        l3 = 'Poda: Estrutural'
        l4 = 'Transplantação: Não'
        if tipo == 'Adubo':
            return l1
        elif tipo == 'Rega':
            return l2
        elif tipo == 'Poda':
            return l3
        elif tipo == 'Transplantação':
            return l4

    elif estacao == 'Outono':
        l1 = 'Adubo: Baixo N, Alto P, K. ex.: NPK 04:14:08'
        l2 = 'Rega : Abundante '
        l3 = 'Poda: Ramos'
        l4 = 'Transplantação: Não'
        if tipo == 'Adubo':
            return l1
        elif tipo == 'Rega':
            return l2
        elif tipo == 'Poda':
            return l3
        elif tipo == 'Transplantação':
            return l4

    elif estacao == 'Primavera':   
        l1 = 'Adubo: Alto N, ex.: NPK 30:10:10'
        l2 = 'Rega : Abundante'
        l3 = 'Poda: Ramos'
        l4 = 'Transplantação: Sim'
        if tipo == 'Adubo':
            return l1
        elif tipo == 'Rega':
            return l2
        elif tipo == 'Poda':
            return l3
        elif tipo == 'Transplantação':
            return l4
    print(l1)
    print(l2)
    print(l3)
    print(l4)
             


#print(data_atual)
estacao = estacao(data_atual)
print(f'Data atual: {data_atual:%d/%m/%Y}')
print(f'A estação atual é {estacao}')
#tipo = 'Adubo'
informacoes(estacao, 'Adubo')


window = Tk()

window.title('Cronograma de Adubação')
window.geometry('550x300')


lbl1 = Label(window, text= f'Data: {data_atual:%d/%m/%Y}',font='helvetica 12')
lbl1.place(x=80, y=30)


lbl2 = Label(window, text= f'Estação: {estacao}', font='helvetica 12 bold')
lbl2.place(x=80, y=70)

lblAdubo = Label(window, text= informacoes(estacao, 'Adubo'),font='helvetica 12')
lblAdubo.place(x=80, y=120)

lblRega = Label(window, text= informacoes(estacao, 'Rega'),font='helvetica 12')
lblRega.place(x=80, y=150)

lblPoda = Label(window, text= informacoes(estacao, 'Poda'),font='helvetica 12')
lblPoda.place(x=80, y=180)

lblTransplantacao = Label(window, text= informacoes(estacao, 'Transplantação'),font='helvetica 12')
lblTransplantacao.place(x=80, y=210)

window.mainloop()

















