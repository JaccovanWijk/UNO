# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:31:34 2019

@author: Jacco
"""

import tkinter as tk

class CategoryCheckApp:
    
    def __init__(self, parent):
        self.parent = parent
        self.returnHome = False
        self.exit = False
        
        #categories as listed in the data set
        self.allcategories = ['PersonalComputerPCOfDesktop_3',
                              'MobieleTelefoonOfSmartphone_6','Spelcomputer_7',
                              'SpelletjesMuziekAfSpelenDownloaden_44',
                              'SociaalNetwerk_31']
        
        #titles of the categories as we want them to be listed in the program. 
        #Same index as allCategories
        self.categorytitles = ['Using Internet on a Personal Computer',
                               'Using internet on a Smartphone',
                               'Using internet on a Gaming System',
                               'Using internet to play and download music and/or games',
                               'Using internet for Social Media']
        
        #set selectedcategories to empty list
        self.selectedCategories = []
        self.selectedTitles = []
        
        #label
        self.label = tk.Label(text = "Choose the categories to compare:")
        self.label.pack()
        
        # Make container
        self.container = tk.Frame(self.parent)
        self.container.pack(padx=20, pady=20)
        
        #make checkbuttons for the categories
        
        self.var1 = tk.IntVar()
        checkButton1 = tk.Checkbutton(self.container, text=self.categorytitles[0], variable=self.var1)
        checkButton1.pack()
        
        self.var2 = tk.IntVar()
        checkButton2 = tk.Checkbutton(self.container, text=self.categorytitles[1], variable=self.var2)
        checkButton2.pack()
        
        self.var3 = tk.IntVar()
        checkButton3 = tk.Checkbutton(self.container, text=self.categorytitles[2], variable=self.var3)
        checkButton3.pack()
        
        self.var4 = tk.IntVar()
        checkButton4 = tk.Checkbutton(self.container, text=self.categorytitles[3], variable=self.var4)
        checkButton4.pack()
        
        self.var5 = tk.IntVar()
        checkButton5 = tk.Checkbutton(self.container, text=self.categorytitles[4], variable=self.var5)
        checkButton5.pack()
        
        self.vars = [self.var1, self.var2, self.var3, self.var4, self.var5]
        
        #make next page button
        nextButton = tk.Button(self.container, text="Next")
        nextButton.pack()
        nextButton.bind("<Button-1>", self.nextPage)
        
        #make homebutton
        self.HomeButton = tk.Button(self.container, text="Home", fg="green")
        self.HomeButton.pack(pady=10)
        self.HomeButton.bind("<Button-1>", self.home)
        
        #make exitbutton
        self.ExitButton = tk.Button(self.container, text="Exit", fg="red")
        self.ExitButton.pack(pady=1)
        self.ExitButton.bind("<Button-1>", self.exitWindow)
    
    #when categories are selected, and next page is pressed    
    def nextPage(self, event):
        
        for i in range(len(self.vars)):
            #check which categories are selected and append them to the list
            if self.vars[i].get() == 1:
                self.selectedCategories.append(self.allcategories[i])
                self.selectedTitles.append(self.categorytitles[i])
        
        print(self.selectedCategories)
        self.parent.destroy()
        
    def getCategories(self):
        #function to get the selected categories and titles to plot them
        return self.selectedCategories, self.selectedTitles
    
    #homebutton and exitbutton functions
    def home(self, event):
        #when button is pressed, set return home to true
        self.returnHome = True
        
        self.parent.destroy()
        
    def exitWindow(self, event):
        #when exit button is pressed, set exit to true
        self.exit = True
        
        self.parent.destroy()
        
    
    
    def getHome(self):
        #check if homebutton is pressed
        return self.returnHome
    
    def getExit(self):
        #check if exit button is pressed
        return self.exit