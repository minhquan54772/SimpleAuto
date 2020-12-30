import PySimpleGUI as sg
import pyautogui

sg.theme('System Default')
sg.set_options(text_color='black', background_color='#5882FA', text_element_background_color='#A6B2BE')

layout = [
    [sg.Text('Keyboard Input:',background_color='#2EFEF7')],
    [sg.InputText(key='keyboard')],
    [sg.Frame(layout=[[sg.Text(
             "+  = SHIFT\t {SPACE} = SPACE\n"
             "^   = CTRL\t {TAB}   = TAB\n"
             "% = ALT \t                {F1} = F1\n",background_color='#33E5FF')]],title='Tips',background_color='#33E5FF')],
    [sg.Button('OK')]
    ]


window = sg.Window('Keyboard', layout, resizable=1, return_keyboard_events=True, background_color='#2EFEF7')
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == 'OK':
        keyboard = values['keyboard']
        break
    else:
        keyboard = event
        if keyboard == ' ': keyboard = '{SPACE}'
        elif keyboard == '  ': keyboard = '{TAB}'
        break

window.close()

