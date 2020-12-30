import PySimpleGUI as sg
import pywinauto
import pyautogui
from pywinauto import application, mouse
from pywinauto import keyboard as kb
from time import sleep

window_loc = (0,0)
window_size = (800,600)
window_title = 'Simple Automator'

status_click = ''
point = any
keyBoard = ''
process = ''
actions = {}


def Mouse():
    sg.theme('System Default')
    sg.set_options(text_color='black', background_color='#5882FA', text_element_background_color='#A6B2BE')

    layout = [
        [sg.Frame(layout=[
            [sg.Radio('Left Click', "RADIO1", default=True, background_color='#33E5FF', key='_LEFT_CLICK_'),
             sg.Radio('Right Click', "RADIO1", background_color='#33E5FF', key='_RIGHT_CLICK_')],
            [sg.Frame(layout=[
                [sg.Text('X:', background_color='#33E5FF'), sg.InputText(key='pos_x',default_text=0)],
                [sg.Text('Y:', background_color='#33E5FF'), sg.InputText(key='pos_y',default_text=0)],
                [sg.Text('Press SPACE key to get mouse coordinates', justification='center',
                         background_color='#33E5FF')],
                [sg.Button('OK',disabled=True,key='OK')]
            ], title='Coordinate', background_color='#33E5FF')]], title='Mouse', background_color='#33E5FF',
            relief=sg.RELIEF_SUNKEN)]]

    window = sg.Window('Mouse', layout, resizable=1, return_keyboard_events=True, background_color='#2EFEF7')
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == ' ':
            global point
            point = pyautogui.position()
            window['pos_x'].update(point.x)
            window['pos_y'].update(point.y)
            window['OK'].update(disabled=False)
        elif event == 'OK':
            global status_click
            if values['_LEFT_CLICK_']:
                status_click = "Left Click"
            else:
                status_click = "Right Click"
            break
    window.close()

def KeyBoard():
    sg.theme('System Default')
    sg.set_options(text_color='black', background_color='#5882FA', text_element_background_color='#A6B2BE')

    layout = [
        [sg.Text('Keyboard Input:', background_color='#2EFEF7')],
        [sg.InputText(key='keyboard')],
        [sg.Frame(layout=[[sg.Text(
            "+  = SHIFT\t {SPACE} = SPACE\n"
            "^   = CTRL\t {TAB}   = TAB\n"
            "% = ALT \t                {F1} = F1\n", background_color='#33E5FF')]], title='Tips',
            background_color='#33E5FF')],
        [sg.Button('OK')]
    ]

    window = sg.Window('Keyboard', layout, resizable=1, return_keyboard_events=True, background_color='#2EFEF7')
    while True:
        event, values = window.read()
        global keyBoard
        if event == 'OK':
            keyBoard = values['keyboard']
            break
        elif event == sg.WIN_CLOSED or event == 'Cancel':
            break
    window.close()

def Automate():
    app = application.Application()
    app.start(process)
    sleep(2)
    for value in actions.values():
        if value[0] == 'Mouse click':
            if value[1] == 'Left Click':
                mouse.click('Left',(value[2], value[3]))
            elif value[1] == 'Right Click':
                mouse.click('Right',(value[2], value[3]))
        elif value[0] == 'Keyboard':
            kb.send_keys(value[1])


#--------Menu----------
menu = [['Project',['New Project', 'Open Project', 'Open Recent']],
        ['&Edit', ['Paste', 'Undo']],
        ['Help',['about']], ['Exit']]
# --------Layout----------
layout = [
    [sg.Menu(menu, tearoff=False)],
    [sg.Text('Simple Automator', size=(200, 1), justification='center', font=('Times New Roman', 25))],
    [sg.Text('_' * 80)],
    [sg.Text('Choose process you want to automate:')],
    [sg.Input('Choose a process', key='process'),
     sg.FileBrowse(file_types=(("Execution Files", "*.exe"), ("All Files", "*.*")))],
    [sg.Text('Number of Steps:'), sg.InputText('1', key='_Steps_', size=(5, 1)), sg.Button('OK')],
]
# -------Init First Window--------
window = sg.Window(title=window_title, layout=layout, size=window_size, location=window_loc, resizable=True)

while True:
    event, values = window.read()
    process = values['process']
    if event == 'OK':
        global steps
        steps = int(values['_Steps_'])
        col = [[sg.Text("Choose type of action:"),
                sg.Combo(('Mouse click', 'Keyboard','No Action'), readonly=True, default_value="No Action", key='{}'.format(i)),
                sg.Button('Get', key="get{}".format(i)),
                sg.Text('-', size=(30, 1), key='_STATE_{}_'.format(i))] for i in range(steps)]
        layout = [
            [sg.Menu(menu, tearoff=True)],
            [sg.Text('Simple Automator', size=(200, 1), justification='center', font=('Times New Roman', 25))],
            [sg.Text('_' * 80)],
            [sg.Text('Choose process you want to automate:')],
            [sg.InputText(process, key='process'), sg.FileBrowse()],
            [sg.Text('Number of Steps:'), sg.InputText(default_text='{}'.format(steps), key='_Steps_', size=(5, 1)),
             sg.Button('Start', button_color=('red', 'green'),key='Start')],
            [sg.Column(col, scrollable=True, vertical_scroll_only=True, size=window_size)],
        ]
        window.close()
        window1 = sg.Window(title=window_title, layout=layout, size=window_size, location=window_loc, resizable=True)
        window = window1
    if event == sg.WINDOW_CLOSED or event == sg.WIN_CLOSED or event == 'Exit':
        break

    for i in range(steps):
        if event == 'get{}'.format(i):
            if values['{}'.format(i)] == "Mouse click":
                Mouse()
                window['_STATE_{}_'.format(i)].update('{} at ({},{})'.format(status_click, point.x, point.y))
                actions.update({i: ('Mouse click', status_click, point.x, point.y)})
                print(actions)

            elif values['{}'.format(i)] == 'Keyboard':
                KeyBoard()
                window['_STATE_{}_'.format(i)].update('{}'.format(keyBoard))
                actions.update({i: ('Keyboard', keyBoard)})
                print(actions)

    if event == 'Start':
        Automate()

window.close()