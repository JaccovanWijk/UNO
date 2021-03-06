# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:29:09 2019

@author: Jacco
"""

import tkinter as tk

class CategoryChoiceApp:
    
    def __init__(self, parent):
        
        #set parent
        #set home and exit to false, those buttons are not pressed
        self.parent = parent
        self.returnHome = False
        self.exit = False
        #categories as listed in the data set
        self.allcategories = ['PersonalComputerPCOfDesktop_3',
                              'MobieleTelefoonOfSmartphone_6','Spelcomputer_7',
                              'SpelletjesMuziekAfSpelenDownloaden_44',
                              'SociaalNetwerk_31']
        
        #category titles as we want them to be listed in the program
        self.categorytitles = ['Using Internet on a Personal Computer',
                               'Using internet on a Smartphone',
                               'Using internet on a Gaming System',
                               'Using internet to play and download music and/or games',
                               'Using internet for Social Media']
        
        #make variable for the selected category
        self.selectedCategory = ""
        self.selectedTitle = ""
        
        #label
        self.label = tk.Label(text = "Choose a category")
        self.label.pack()
        
        #make container
        self.container = tk.Frame(self.parent)
        self.container.pack(padx=20, pady=20)
        
        
        #make buttons per category
        
        self.Button1 = tk.Button(self.container, text=self.categorytitles[0])
        self.Button1.pack(pady = 1,fill='x')
        self.Button1.bind("<Button-1>", self.useCategory1)
        
        self.Button2 = tk.Button(self.container, text=self.categorytitles[1])
        self.Button2.pack(pady = 1,fill='x')
        self.Button2.bind("<Button-1>", self.useCategory2)
        
        self.Button3 = tk.Button(self.container, text=self.categorytitles[2])
        self.Button3.pack(pady = 1,fill='x')
        self.Button3.bind("<Button-1>", self.useCategory3)
        
        self.Button4 = tk.Button(self.container, text=self.categorytitles[3])
        self.Button4.pack(pady = 1,fill='x')
        self.Button4.bind("<Button-1>", self.useCategory4)
        
        self.Button5 = tk.Button(self.container, text=self.categorytitles[4])
        self.Button5.pack(pady = 1,fill='x')
        self.Button5.bind("<Button-1>", self.useCategory5)
        
        self.HomeButton = tk.Button(self.container, text="Home", fg="green")
        self.HomeButton.pack(pady=10)
        self.HomeButton.bind("<Button-1>", self.home)
        
        self.ExitButton = tk.Button(self.container, text="Exit", fg="red")
        self.ExitButton.pack(pady=1)
        self.ExitButton.bind("<Button-1>", self.exitWindow)
    
    #per category button, if it's pressed: set selected category to that one. Corresponding title as well.
    
    def useCategory1(self, event):
        
        self.selectedCategory = self.allcategories[0]
        self.selectedTitle = self.categorytitles[0]
        
        self.parent.destroy()
        
    def useCategory2(self, event):
        
        self.selectedCategory = self.allcategories[1]
        self.selectedTitle = self.categorytitles[1]
        
        self.parent.destroy()
        
    def useCategory3(self, event):
        
        self.selectedCategory = self.allcategories[2]
        self.selectedTitle = self.categorytitles[2]
        
        self.parent.destroy()
        
    def useCategory4(self, event):
        
        self.selectedCategory = self.allcategories[3]
        self.selectedTitle = self.categorytitles[3]
        
        self.parent.destroy()
        
    def useCategory5(self, event):
        
        self.selectedCategory = self.allcategories[4]
        self.selectedTitle = self.categorytitles[4]
        
        self.parent.destroy()
        
    #get chosen category
    def getCategory(self):
        
        return self.selectedCategory, self.selectedTitle
    
    #return home and exit button functions
    
    def home(self, event):
        
        self.returnHome = True
        
        self.parent.destroy()
        
    def exitWindow(self, event):
        
        self.exit = True
        
        self.parent.destroy()
        
    
    #functions to get the home and exit values (true if pressed)
    def getHome(self):
        
        return self.returnHome
    
    def getExit(self):
        
        return self.exit