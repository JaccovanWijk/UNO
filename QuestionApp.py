# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:21:35 2019

@author: UNO
"""
import tkinter as tk


class QuestionApp:

    def __init__(self, parent):
        self.parent = parent
        self.question = ""
        self.exit = False
        
        # Set text and buttons for the questions
        self.text = tk.Label(text= "Which question do you want to be answered?", fg='blue')
        self.text.pack()
        # Make container
        self.container = tk.Frame(self.parent)
        self.container.pack(padx= 50, pady=50)

        # Initialize all buttons
        self.Q1Button = tk.Button(self.container, text=
                                  "Daily usage in % per age age-group per year" )
        self.Q1Button.pack(pady = 1, fill='x')
        self.Q1Button.bind("<Button-1>", self.insertQ1)

        self.Q2Button = tk.Button(self.container, text=
                                  "Comparing parts of society")
        self.Q2Button.pack(pady = 1, fill='x')
        self.Q2Button.bind("<Button-1>", self.insertQ2)

        self.Q3Button = tk.Button(self.container, text=
                                  "Comparing genders by monthly internet usage.")
        self.Q3Button.pack(pady = 1, fill='x')
        self.Q3Button.bind("<Button-1>", self.insertQ3)
        
        self.ExitButton = tk.Button(self.container, text="Exit", fg="red")
        self.ExitButton.pack(pady=1)
        self.ExitButton.bind("<Button-1>", self.exitWindow)

    # Set selected question to global variable
    def insertQ1(self, event):
        self.question = "Q1"
        self.parent.destroy()
        
    def insertQ2(self, event):
        self.question = "Q2"
        self.parent.destroy()

    def insertQ3(self, event):
        self.question = "Q3"
        self.parent.destroy()
    
    #exit button function
    def exitWindow(self, event):
        
        self.exit = True
        
        self.parent.destroy()
    
    def getExit(self):
        
        return self.exit
    
    #get selected question
    def getQuestion(self):
        
        return self.question