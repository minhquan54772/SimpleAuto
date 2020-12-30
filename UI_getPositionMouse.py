import PySimpleGUI as sg
import pyautogui
status_click=''
sg.theme('System Default')
sg.set_options(text_color='black', background_color='#5882FA', text_element_background_color='#A6B2BE')

layout = [
   [sg.Frame(layout=[
        [sg.Radio('Left Click', "RADIO1", default=True, background_color='#33E5FF',key='_LEFT_CLICK_'),
         sg.Radio('Right Click', "RADIO1", background_color='#33E5FF',key='_RIGHT_CLICK_')],
        [sg.Frame(layout=[
            [sg.Text('X:', background_color='#33E5FF'), sg.InputText(key='pos_x')],
            [sg.Text('Y:', background_color='#33E5FF'), sg.InputText(key='pos_y')],
            [sg.Text('Press SPACE key to get mouse coordinates', justification='center', background_color='#33E5FF')],
            [sg.Button('OK')]
        ], title='Coordinate', background_color='#33E5FF')]], title='Mouse', background_color='#33E5FF', relief=sg.RELIEF_SUNKEN)]]


window = sg.Window('Mouse', layout, resizable=1, return_keyboard_events=True, background_color='#2EFEF7')
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == ' ':
            pos = pyautogui.position()
            print(pos)
            window['pos_x'].update(pos.x)
            window['pos_y'].update(pos.y)
    elif event == 'OK':
        if values['_LEFT_CLICK_'] == True:
            status_click = "Left Click"
        else: status_click = "Right Click"
        break
window.close()