#!/bin/python/
import os
import sys
import time

import threading

from pytube import YouTube
from pytube.exceptions import VideoUnavailable

"""
- Add a playlist Object from pytube so I can group all the links while im offline then when im online 
  I can batch download everything I have queued up
"""


def clear_screen():
    os.system("cls")


def load_video(url):
    global yt
    try:
        yt = YouTube(url, on_progress_callback=load, on_complete_callback=finish)
    except VideoUnavailable:
        print(f"Video unavailable: {url}")


def load(chunk, file_handle, bytes_remaining):
    contentSize = video.filesize
    size = contentSize - bytes_remaining

    print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
    '█' * int(size*20/contentSize), ' '*(20-int(size*20/contentSize)), float(size/contentSize*100)), end='')
# '█'


def finish(arg1=None, arg2=None):
    print('\r' + '[Download Completed]:D'+28*' ')


def startup(thread):
    # clear_screen()
    count = 0
    states = ["Loading   ", "Loading.  ", "Loading.. ", "Loading..."]
    
    while thread.is_alive():
        
        if count > 3:
            count = 0
        # elif count == 2:
            # clear_screen()
        
        print('\r' + states[count], end='')
        count += 1
        time.sleep(0.3)
    print("Process done!")


url = input("Youtube URL: ")
path = "~/downloads/"
print("\n")
th = threading.Thread(target=load_video, args=(url,))
th.start()
startup(th)

th.join()

title = yt.title
raw_len = yt.length
length_min = raw_len//60
length_sec = raw_len%60
description = yt.description
video = yt.streams.get_lowest_resolution()

width, rows = os.get_terminal_size()

# yt.streams.get_lowest_resolution().download()
# clear_screen()
print(f"{width*'_'}\n{length_min}m {length_sec}s | {title}")

down = input("\nWould you like to download?(y/n): ")

print("\n")
if down.lower() == 'y':
    video.download()  # path)
# print(description)
