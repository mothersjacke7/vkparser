import PySimpleGUI as sg
from main import *

sg.theme('DarkBlue')

layout = [  [sg.Text('Введите Ваш токен доступа VK')],
            [sg.InputText('', key = 'valuet')],
            [sg.Text('Введите ссылку паблика 1')],
            [sg.InputText('', key = 'public1')],
            [sg.Text('Введите ссылку паблика 2')],
            [sg.InputText('', key ='public2')],
            [sg.Button('Ok', key = "Okay"), sg.Button('Cancel')],
            [sg.Text('', key='-TEXT-')],
            [sg.Output(key='-TEXT_response-', expand_x=True, expand_y = True)]]

window = sg.Window('Поиск общих пользователей', layout, size=(400, 400))

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        print("Cancel")
        break
    if event == 'Okay':
        common_ids_output, percent1, percent2 = common_idsf(values["public1"], values["public2"], values["valuet"])
        window['-TEXT-'].update(f'Количество общих пользователей: {len(common_ids_output)}\nПроцент пользователей паблика 1: {percent1}%\nПроцент пользователей паблика 2: {percent2}%\nID пользователей смежных групп:')
        window['-TEXT_response-'].update(common_ids_output)
window.close()