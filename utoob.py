#!/bin/python/
import os
import sys
import time

import threading

from pytube import YouTube

def clear_screen():
    os.system("clear")


def load(chunk, file_handle, bytes_remaining):
    contentSize = video.filesize
    size = contentSize - bytes_remaining

    print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
    '█' * int(size*20/contentSize), ' '*(20-int(size*20/contentSize)), float(size/contentSize*100)), end='')


def finish(arg1=None, arg2=None):
    print('\r' + '[Download Completed]:D'+28*' ')


def startup():
    clear_screen()
    count = 0
    loops = 0
    max_loops = 31
    loadin = True
    while loadin:
        states = [
            "Loading   ",
            "Loading.  ",
            "Loading.. ",
            "Loading...",
        ]
        if loops > max_loops:
            loadin = False
        elif count > 3:
            count = 0
        elif count == 2:
            clear_screen()
        
        print('\r' + states[count], end='')
        count += 1
        loops += 1
        time.sleep(0.40)

url = input("Youtube URL: ")
path = "~/downloads/"

try:
    th = threading.Thread(target=startup)
    th.start()
    yt = YouTube(url, on_progress_callback = load, on_complete_callback = finish)
    th.join()
except VideoUnavailable:
    print(f"Video unavailable: {url}")

title = yt.title
raw_len = yt.length
length_min = raw_len//60
length_sec = raw_len%60 
description = yt.description
video = yt.streams.get_lowest_resolution()

# yt.streams.get_lowest_resolution().download()
clear_screen()
print(f"{title}\t|{length_min}m {length_sec}s|")

down = input("\n Download?: ")

print("\n")
if down.lower() == 'y':
    video.download()  # path)
# print(description)
