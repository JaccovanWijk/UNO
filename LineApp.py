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
        self.years = ['2012','2013','2014','2015','2016','2017','2018']
        self.returnHome = False
        self.exit = False
        
        # Make frame
        frame = tk.Frame(self.parent)

        # Make a figure and insert the plot
        fig = Figure()
        ax = fig.add_subplot(111)
        for i in range(len(data)):
            ax.plot(self.years, data[i], label=labels[i])
        ax.legend(loc="upper right")
        ax.grid()
        ax.set_title(title)
        ax.set_ylim([0,100])
        
        # Make a canvas in the frame and add figure
        self.canvas = FigureCanvasTkAgg(fig, master=parent)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
        frame.pack()
        
        self.HomeButton = tk.Button(text="Home", fg="green")
        self.HomeButton.pack(pady=10)
        self.HomeButton.bind("<Button-1>", self.home)
        
        self.ExitButton = tk.Button(text="Exit", fg="red")
        self.ExitButton.pack(pady=1)
        self.ExitButton.bind("<Button-1>", self.exitWindow)
        
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