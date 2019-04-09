# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:36:44 2019

@author: Jacco
"""

import tkinter as tk
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class BarApp:
    
    def __init__(self, parent, data, titles, title):
        self.parent = parent
        self.returnHome = False
        self.exit = False
        
        # Make frame
        frame = tk.Frame(self.parent) 
        
        # Make a figure and insert barplot
        fig = Figure()
        barwidth = 0.25
        y_pos = np.arange(len(titles))
        y_pos2 = [x + barwidth for x in y_pos]
        ax = fig.add_subplot(111)
        ax.bar(y_pos, data[0], color="blue", width=barwidth, label="Men")
        ax.bar(y_pos2, data[1], color="red", width=barwidth, label="Women")
        ax.legend(loc="upper right")
        ax.set_xticks(y_pos + barwidth / 2)
        ax.set_xticklabels(titles)
        ax.set_ylim([0,100])
        ax.grid()
        ax.set_title(title)
        
        # Make a canvas in the frame and add figure
        self.canvas = FigureCanvasTkAgg(fig, master=parent)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
        frame.pack()  
        
        #create homebutton
        self.HomeButton = tk.Button(text="Home", fg="green")
        self.HomeButton.pack(pady=10)
        self.HomeButton.bind("<Button-1>", self.home)
        
        #create exitbutton
        self.ExitButton = tk.Button(text="Exit", fg="red")
        self.ExitButton.pack(pady=1)
        self.ExitButton.bind("<Button-1>", self.exitWindow)
    
    
    #home and exit button functions, same as in lineApp
    
    def home(self, event):
        
        self.returnHome = True
        
        self.parent.destroy()
        
    def exitWindow(self, event):
        
        self.exit = True
        
        self.parent.destroy()
        
    def getHome(self):
        
        return self.returnHome
    
    def getExit(self):
        
        return self.exit