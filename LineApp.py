# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:35:05 2019

@author: Jacco
"""

import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class LineApp:

    def __init__(self, parent, data, labels, title):
        self.parent = parent
        
        #years used in the datas
        self.years = ['2012','2013','2014','2015','2016','2017','2018']
        
        #home and exit buttons are not pressed, therefore set to false
        self.returnHome = False
        self.exit = False
        
        # Make frame
        frame = tk.Frame(self.parent)

        # Make a figure and insert the plot
        fig = Figure()
        ax = fig.add_subplot(111)
        for i in range(len(data)):
            ax.plot(self.years, data[i], label=labels[i])
        ax.legend(loc="upper left")
        ax.grid()
        ax.set_title(title)
        ax.set_ylim([0,100])
        
        # Make a canvas in the frame and add figure
        self.canvas = FigureCanvasTkAgg(fig, master=parent)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
        frame.pack()
        
        #make homebutton 
        self.HomeButton = tk.Button(text="Home", fg="green")
        self.HomeButton.pack(pady=10)
        self.HomeButton.bind("<Button-1>", self.home)
        
        #make exitbutton
        self.ExitButton = tk.Button(text="Exit", fg="red")
        self.ExitButton.pack(pady=1)
        self.ExitButton.bind("<Button-1>", self.exitWindow)
        
    def home(self, event):
        
        #when homebutton is called
        self.returnHome = True
        
        self.parent.destroy()
        
    def exitWindow(self, event):
        
        #when exitbutton is called
        self.exit = True
        
        self.parent.destroy()
        
    def getHome(self):
        
        #returns true if home button is pressed
        return self.returnHome
    
    def getExit(self):
        
        #returns true if exit button is pressed
        return self.exit