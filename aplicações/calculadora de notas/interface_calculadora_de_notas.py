import PySimpleGUI as sg


sg.theme('Default') 
layout = [
            [sg.Text('1ª UNIDADE: '), sg.Input(key='nota1')],
            [sg.Text('2ª UNIDADE: '), sg.Input(key='nota2')],
            [sg.Text('3ª UNIDADE: '), sg.Input(key='nota3')],
            [sg.Text('', key='resultado')],
            [sg.Button('Calcular'), sg.Button('Sair')] ]


janela = sg.Window('CALCULADORA DE NOTAS - UFERSA', layout)

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED or event == 'Sair': 
        break
    elif event == 'Calcular':
        n1 = float(values['nota1'])
        n2 = float(values['nota2'])
        n3 = float(values['nota3'])

        media = (n1+n2+n3)/3
        rec = (50-media*6)/4

        if media>=7 and media<=10:
            janela['resultado'].update("Aluno aprovado com media %.1f" %media)
        elif media>=5 and media<7:
            janela['resultado'].update("Você esta de recuperação, precisando de %.1f" %rec)
        elif media<5:
            janela['resultado'].update("Aluno Reprovado.")
        else: 
            janela['resultado'].update("Operação Invalida!\nDigite a nota corretamente.")
            
        
janela.close()