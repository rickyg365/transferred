import PySimpleGUI as sg

from pytube import YouTube
from utoob2 import *


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Welcome to Utoob downloader')],
            [sg.Text('Enter the video URL'), sg.InputText()],
            [sg.Button('download'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Utoob downloader', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break

    url = values[0]
    print("\n")
    th = threading.Thread(target=load_video, args=(url,))
    th.start()
    startup(th)

    th.join()

    title = yt.title
    raw_len = yt.length
    length_min = raw_len // 60
    length_sec = raw_len % 60
    description = yt.description
    video = yt.streams.get_lowest_resolution()

    width, rows = os.get_terminal_size()

    # clear_screen()
    print(f"{width * '_'}\n{length_min}m {length_sec}s | {title}")

    down = input("\nWould you like to download?(y/n): ")

    print("\n")
    if down.lower() == 'y':
        video.download()  # path)
    # print(description)
    print('You entered ', values[0])

window.close()
