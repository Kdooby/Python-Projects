import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import askopenfile 
import os


# Blueprint to create a basic tkinter window
class ParentWindow(tk.Frame):
    def __init__(self, master, initialdir='', filetypes=()):
        tk.Frame.__init__(self)
        
        self.master = master
        self.master.resizable(width=False, height=False) # not resizable
        self.master.geometry(f'{600}x{100}')
        self.master.title('Check files')
        self.master.config(bg = '#f0f0f0')
        
        self.filepath = tk.StringVar()
        self.initialdir = initialdir
        self.filetypes = filetypes
        self.Buttons()
        self.Entry()
        #Creates Buttons
    
    def Buttons(self):
        self.btnBrowse = tk.Button(self.master, text = 'Browse...', width = 13, height = 1, command = self.browse)
        self.btnBrowse.grid(row = 0, column = 0, padx = (20,0), pady = (30, 0))
        
        self.btnClose = tk.Button(self.master, text = 'Close Program', width = 13, height = 1, command = self.ask_quit)
        self.btnClose.grid(row = 1, column = 2, padx = (350,0), pady = (5, 0))
        
        
        # Calls the "ENTRY" Widget that was imported 
    def Entry(self):
        self._entry = tk.Entry(self.master, textvariable=self.filepath, width = 35, font = ('Helvetica', 12))
        self._entry.grid(row = 0, column = 2, padx = (20,0), pady = (30, 0))
        
        
         # Browses a .png file or all files and then puts it on the entry.
    def browse(self):
        self.filepath.set(filedialog.askopenfilename(initialdir=self.initialdir,
                          filetypes=self.filetypes))  
    
            
    def ask_quit(self):
        if messagebox.askokcancel("Exit program", "Okay to exit application?"):
            # This closes app
            self.master.destroy()
            os._exit(0)
            

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root, initialdir=r"/",
                       filetypes=(("All Files", "*.*"),("JPEG Files","*.jpg"),('Portable Network Graphics','*.png')))
                                                   
    root.mainloop()
