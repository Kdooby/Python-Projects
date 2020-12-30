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


import FileTransfer_GUI
import FileTransfer_Func

class ParentWindow(tk.Frame):
    def __init__(self, master, initialdir='', filetypes=()):
        tk.Frame.__init__(self, master)

        # define our master frame configuration
        self.master = master
        self.master.resizable(width=False, height=False) # not resizable
        self.master.geometry(f'{600}x{150}')
        # define the file information

        # source filepath
        self.filepath = tk.StringVar()

        # destination filepath
        self.filepath2 = tk.StringVar()

        self.initialdir = initialdir
        self.filetypes = filetypes
        
        # This CenterWindow method will center our app on the user's screen
        FileTransfer_Func.center_window(self,600,150)
        self.master.title("File Transfer")
        self.master.configure(bg="#f0f0f0")
        

        # load in the GUI widgets from a separate module, 
        # keeping your code comparmentalized and clutter free
        FileTransfer_GUI.load_gui(self)

        
        
        








if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root, initialdir=r"/",
                       filetypes=(("All Files", "*.*"),("JPEG Files","*.jpg"),('Portable Network Graphics','*.png')))
    root.mainloop()
