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
    # takes the value from x and y from above and formats to center of screen
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


# catch if the user wants to close the app
def ask_quit(self):
    # opens message box on button click, and asks if to close or not
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)
    

def browseSrc(self):
    # opens browser window
    source = filedialog.askdirectory()
    # sets absolute path of source folder
    self.filepath.set(source)
    

def browseDest(self):
    # opens browser window
    destination = filedialog.askdirectory()
    # sets absolute path of destination folder
    self.filepath2.set(destination)
    


### TRANSFER FILES SECTION ###




def last_mod_time(self):
    # gets the absolute paths for both folders
    source = self.filepath.get()
    destination = self.filepath2.get()
    # time 24 hours from now
    hours_ago_24 = datetime.datetime.now() - timedelta(hours = 24)
    # loop for the file in the directory
    for fname in os.listdir(source):
        # joins the source path and file  
        src_fname = os.path.join(source, fname)
        # gets the modification time of the source file
        modTime = os.path.getmtime(src_fname)
        # variable for the timestamp of the modified source file
        date_time_of_file = datetime.datetime.fromtimestamp(modTime)
        # sees if the timestamp from source file is from within 24 period
        if date_time_of_file > hours_ago_24:
            # moves source file to destination folder
            shutil.move(src_fname, destination)
            print('These files have been tranfered', fname)
               



if __name__ == "__main__":
    pass

