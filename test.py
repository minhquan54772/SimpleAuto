from pywinauto import application, mouse, keyboard
from time import sleep

app = application.Application()

app.start('notepad.exe')
sleep(1)
mouse.right_click((1280,270))