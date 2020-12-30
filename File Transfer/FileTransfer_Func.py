# Python Ver: 3.9
#
# Author:       Kevin Deming 
#
# Purpose:      File Transfer.  Demonstrating OOP, Tkinter GUI module, using Tkinter
#               Parent and Child relationships
#
# Tested OS:    This code was written and tested to work with Windows 10

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import datetime
from datetime import timedelta


import shutil
import os
import time

import FileTransfer_GUI
import FileTransfer_Main

def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


# catch if the user wants to close the app
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)
    

def browseSrc(self):
    # set where the source of the files are
    source = filedialog.askdirectory()
    self.filepath.set(source)
    

def browseDest(self):
    # set where the source of the files are
    destination = filedialog.askdirectory()
    self.filepath2.set(destination)
    


### TRANSFER FILES SECTION ###

# time 24 hours from now
hours_ago_24 = datetime.datetime.now() - timedelta(hours = 24)


def last_mod_time(fname):
    return os.path.getmtime(fname)

    for fname in os.listdir(source):
        src_fname = os.path.join(source, fname)
        modTime = os.path.getmtime(src_fname)
        date_time_of_file = datetime.datetime.fromtimestamp(modTime)
        if date_time_of_file < hours_ago_24:
            dst_fname = os.path.join(destination, fname)
            shutil.move(src_fname, dst_fname)
               



if __name__ == "__main__":
    pass

