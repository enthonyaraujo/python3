import math
import PySimpleGUI as sg


sg.theme('Default')  #adicionando tema a interface
    
layout =  [
    [sg.Text('n = '), sg.InputText(key='n')],
    [sg.Text('p = '), sg.InputText(key='p')],
    [sg.Text('', key='result')],
    [sg.Button('Calcular'), sg.Button('Sair')]
 ]
    
window = sg.Window('Coenfiente Binomial', layout)   #cria a janela
    
while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Sair':
            break
        if event == 'Calcular':
            try:
                n = int(values['n'])
                p = int(values['p'])
                if n>=0 and p>=0:
                    coenfiente_binomial = math.comb(n, p)
                    window['result'].update(coenfiente_binomial)
                else:
                    window['result'].update('Insira números inteiros')
            except ValueError:
                window['result'].update('Insira números inteiros')
window.close()
