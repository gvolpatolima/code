import tkinter as tk
from pytube import YouTube
from tkinter import filedialog
from pytube.exceptions import RegexMatchError

# Creates the window

window = tk.Tk()
window.title('mp4 youtube download')

"""
Checks if the link exists
If the link isn't given show the err() function
Asks for a folder to direct the mp4 file and uses the Youtube().streams.get_highest_resolution().download() 
function to download it
Spits out an error if anything goes wrong
"""
def download(link_):
    if link_:
        try:
            folder = filedialog.askdirectory()
            YouTube(link_).streams.get_highest_resolution().download(folder)
            alert()
        except RegexMatchError:
            err()
    else:
        err()

# Alert for when everything went fine

def alert():
    top = tk.Toplevel()
    top.title('Alert')
    top.geometry('300x200')

    tk.Label(top, text='Done', font='arial 14 bold', pady=30).pack()
    tk.Button(top, text='OK', command=top.destroy).pack()


# Error funcion for every error 

def err():
    top = tk.Toplevel()
    top.title('ERROR')
    top.geometry('300x200')

    tk.Label(top, text='Invalid link', font='arial 14 bold', pady=50).pack()
    tk.Button(top, text='OK', command=top.destroy).pack()




frame = tk.Frame(window)
frame.pack()

ilink = tk.Label(frame, text='Insert Link ', font='courier 15 bold')
ilink.pack(side = 'left')

link = tk.Entry(frame, font='arial 20', width=30)
link.pack(side='left')

tk.Button(frame, bg='green', text='>>>', bd=1, fg='white', width=4, height=2, command=lambda: download(link.get())).pack()
window.mainloop()