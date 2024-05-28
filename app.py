from PySimpleGUI import PySimpleGUI as sg
import re

r = re.compile(r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*?])[A-Za-z\d!@#$%^&*?]{8,}$')

sg.theme('Reddit')
layout = [
    [sg.Text('Sua senha: '), sg.Input(key='senha', password_char='*')],
    [sg.Button('Verificar senha')]
]

janela = sg.Window('Tela de verificação de senha', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Verificar senha':
        senha = valores['senha']
        if r.match(senha):
            sg.popup('Senha forte')
        else:
            sg.popup('Senha muito fraca')

janela.close()