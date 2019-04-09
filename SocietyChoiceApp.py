# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:32:49 2019

@author: Jacco
"""

import tkinter as tk

class SocietyChoiceApp:
    
    def __init__(self, parent):
        self.parent = parent
        self.returnHome = False
        self.exit = False
        
        self.societyParts = [['1014752', '1014753', '1014754', '1014755', '1014756'], 
                             ['1012600','2012605'], ['2018700', '2018740', '2018790'],
                             ['3000795','3000805'], ['2021209','2021211','2021230','2021240']]
        self.societyTitles = [['First 20%', 'Second 20%','Thirth 20%','Fourth 20%','Fifth 20%'],
                              ['Imigration background', 'No imigration background'],
                              ['vmbo', 'havo/vwo', 'hbo/wo'], ['unemployed','employed'],
                              ['parttime','<20h','20-35h','Fulltime']]
        self.globalTitles = ['Different Paygrades', 'Imigration Background', 
                             'Educational Attainment', 'Employmend', 'Working Hours']
        self.selectedParts = []
        self.selectedTitles = []
        
        self.label = tk.Label( text = "Choose the parts of society to compare:")
        self.label.pack(padx=50)
        
        
        self.container = tk.Frame(self.parent, width=300, height = 200)
        self.container.pack(padx=20, pady = 20)
        
        
        self.Button1 = tk.Button(self.container, text = self.globalTitles[0])
        self.Button1.pack(pady = 1,  fill='x')
        self.Button1.bind("<Button-1>", self.useSociety1)
        
        self.Button2 = tk.Button(self.container, text = self.globalTitles[1])
        self.Button2.pack(pady = 1,fill='x')
        self.Button2.bind("<Button-1>", self.useSociety2)
        
        self.Button3 = tk.Button(self.container, text = self.globalTitles[2])
        self.Button3.pack(pady = 1,fill='x')
        self.Button3.bind("<Button-1>", self.useSociety3)
        
        self.Button4 = tk.Button(self.container, text = self.globalTitles[3])
        self.Button4.pack(pady = 1,fill='x')
        self.Button4.bind("<Button-1>", self.useSociety4)
        
        self.Button5 = tk.Button(self.container, text = self.globalTitles[4])
        self.Button5.pack(pady = 1,fill='x')
        self.Button5.bind("<Button-1>", self.useSociety5)
        
        self.HomeButton = tk.Button(self.container, text="Home", fg="green")
        self.HomeButton.pack(pady=10)
        self.HomeButton.bind("<Button-1>", self.home)
        
        self.ExitButton = tk.Button(self.container, text="Exit", fg="red")
        self.ExitButton.pack(pady=1)
        self.ExitButton.bind("<Button-1>", self.exitWindow)
        
        
    def useSociety1(self, event):
        
        self.selectedParts = self.societyParts[0]
        self.selectedTitles = self.societyTitles[0]
        
        self.parent.destroy()
        
    def useSociety2(self, event):
        
        self.selectedParts = self.societyParts[1]
        self.selectedTitles = self.societyTitles[1]
        
        self.parent.destroy()
        
    def useSociety3(self, event):
        
        self.selectedParts = self.societyParts[2]
        self.selectedTitles = self.societyTitles[2]
        
        self.parent.destroy()
        
    def useSociety4(self, event):
        
        self.selectedParts = self.societyParts[3]
        self.selectedTitles = self.societyTitles[3]
        
        self.parent.destroy()
        
    def useSociety5(self, event):
        
        self.selectedParts = self.societyParts[4]
        self.selectedTitles = self.societyTitles[4]
        
        self.parent.destroy()
        
    def home(self, event):
        
        self.returnHome = True
        
        self.parent.destroy()
        
    def exitWindow(self, event):
        
        self.exit = True
        
        self.parent.destroy()
        
    def getSocietyPart(self):
        
        return self.selectedParts, self.selectedTitles
    
    def getHome(self):
        
        return self.returnHome
    
    def getExit(self):
        
        return self.exit