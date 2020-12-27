# Python Ver: 3.8.7
#
# Author:       Kevin Deming 
#
# Purpose:      Web Page Generator.  Demonstrating OOP, Tkinter GUI module, using Tkinter
#               Parent and Child relationships
#
# Tested OS:    This code was written and tested to work with Windows 10





from tkinter import *
import tkinter as tk
from tkinter import messagebox
import webbrowser
import os





class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define the Frame configuration
        self.master = master
        self.master.resizable(width=False, height=False) # Resizable
        self.master.geometry(f'{500}x{150}')

        self.master.title("What Should It Say?")
        self.master.config(bg = '#f0f0f0')

        ParentWindow.center_window(self,500,150) # Calls on the center_window method

        self.source = StringVar()  

        # CREATES LABELS 
        self.lbl_txt = Label(self.master, font= ('Helvetica', 12), bg= '#f0f0f0', fg = 'black', text = 'Website Content: ')
        self.lbl_txt.pack(side = TOP)

        # CREATE INPUT BOX
        self.txt = Entry(self.master, bg = 'lightgray', textvariable = self.source)
        self.txt.pack(ipadx=125, pady = 30)



        # CREATES BUTTONS
        # submits text and opens webpage
        self.btn_Submit = Button(self.master, text = "Submit", width = 13, height = 1, bg = 'lightgray', fg = 'black', command = self.open_webpage)
        self.btn_Submit.pack(side = RIGHT, padx = (0,65), pady = (0, 20))

        # closes application
        self.btnClose = tk.Button(self.master, text = 'Close', width = 13, height = 1, command = self.ask_quit)
        self.btnClose.pack(side = RIGHT, padx = (0, 10), pady = (0, 20))
        


        
    def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
        # get user's screen width and height
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        # calculate x and y coordinates to paint the app centered on the user's screen
        x = int((screen_width/2) - (w/2))
        y = int((screen_height/2) - (h/2))
        centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
        return centerGeo


    # Opens Webpage with user input text after hitting "Submit" button
    def open_webpage(self):
        f = open("your_webpage_here.html", "w") # will create a file if the specified file does not exist
        text = self.source.get()
        message = text
        f.write(message)
        f.close()

        filename = 'file:///' + os.getcwd() + '/' + 'your_webpage_here.html'  # finds the file from the directory
        webbrowser.open_new_tab(filename) # Opens a webpage in a new tab.
        

    # Asks if the user wants to quit the application
    def ask_quit(self):
        if messagebox.askokcancel("Exit program", "Okay to exit application?"):
            # This closes app
            self.master.destroy()
            os._exit(0)

 




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
