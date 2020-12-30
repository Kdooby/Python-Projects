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

import shutil
import os
import time


import FileTransfer_Main
import FileTransfer_Func


def load_gui(self):
    self.btnBrowse = tk.Button(self.master, text = 'Source Folder', width = 13, height = 1, command = FileTransfer_Func.browseSrc(self))
    self.btnBrowse.grid(row = 0, column = 0, padx = (20,0), pady = (30, 0))

    self.btnBrowse = tk.Button(self.master, text = 'Destination Folder', width = 13, height = 1, command = FileTransfer_Func.browseDest(self))
    self.btnBrowse.grid(row = 1, column = 0, padx = (20,0), pady = (30, 0))
        
    self.btnTransfer = tk.Button(self.master, text = 'Transfer Files', width = 13, height = 1, command = FileTransfer_Func.last_mod_time(self))
    self.btnTransfer.grid(row = 1, column = 3, padx = (10,0), pady = (0, 30))

    self.btnClose = tk.Button(self.master, text = 'Close', width = 13, height = 1, command = FileTransfer_Func.ask_quit(self))
    self.btnClose.grid(row = 2, column = 2, padx = (0,0), pady = (3, 0))

    # Calls the "ENTRY" Widget that was imported 
    self.src = tk.Entry(self.master, textvariable=self.filepath, width = 35, bg='lightgray', font = ('Helvetica', 12))
    self.src.grid(row = 0, column = 2, padx = (30,0), pady = (30, 0))

    self.dest = tk.Entry(self.master, textvariable=self.filepath2, width = 35, bg='lightgray', font = ('Helvetica', 12))
    self.dest.grid(row = 1, column = 2, padx = (30,0), pady = (30, 0))










if __name__ == "__main__":
    pass
