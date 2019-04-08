# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 19:22:52 2019

@author: sepke
"""

import pandas as pd
import numpy as np
import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class InsertDataApp:

    def __init__(self, parent):
        self.parent = parent

        # Make container
        self.container = tk.Frame(self.parent)
        self.container.pack()

        # Set text and buttons for the questions
        self.text = tk.Label(self.container, text=
                             "Which question do you want to be answered?")
        self.text.pack()

        self.Q1Button = tk.Button(self.container, text=
                                  "Daily usage in % per age age-group per year")
        self.Q1Button.pack()
        self.Q1Button.bind("<Button-1>", self.insertQ1)

        self.Q2Button = tk.Button(self.container, text=
                                  "Comparing parts of society")
        self.Q2Button.pack()
        self.Q2Button.bind("<Button-1>", self.insertQ2)

        self.Q3Button = tk.Button(self.container, text=
                                  "Comparing genders by monthly internet usage.")
        self.Q3Button.pack()
        self.Q3Button.bind("<Button-1>", self.insertQ3)

    # Set selected question to global variable
    def insertQ1(self, event):
        question.append("Q1")
        self.parent.destroy()

    def insertQ2(self, event):
        question.append("Q2")
        self.parent.destroy()

    def insertQ3(self, event):
        question.append("Q3")
        self.parent.destroy()


class CategoryChoiceApp:
    
    def __init__(self, parent):
        self.parent = parent
        
        self.allcategories = ['PersonalComputerPCOfDesktop_3',
                              'MobieleTelefoonOfSmartphone_6','Spelcomputer_7',
                              'SpelletjesMuziekAfSpelenDownloaden_44',
                              'SociaalNetwerk_31']
        
        self.categorytitles = ['Using Internet on a Personal Computer',
                               'Using internet on a Smartphone',
                               'Using internet on a Gaming System',
                               'Using internet to play and download music and/or games',
                               'Using internet for Social Media']
        self.selectedCategory = ""
        self.selectedTitle = ""
        
        self.label = tk.Label(text = "Choose a category you'd like to use:")
        self.label.pack()
        
        self.container = tk.Frame(self.parent)
        self.container.pack()
        
        self.Button1 = tk.Button(self.container, text=self.categorytitles[0])
        self.Button1.pack()
        self.Button1.bind("<Button-1>", self.useCategory1)
        
        self.Button2 = tk.Button(self.container, text=self.categorytitles[1])
        self.Button2.pack()
        self.Button2.bind("<Button-1>", self.useCategory2)
        
    def useCategory1(self, event):
        
        self.selectedCategory = self.allcategories[0]
        self.selectedTitle = self.categorytitles[0]
        
        self.parent.destroy()
        
    def useCategory2(self, event):
        
        self.selectedCategory = self.allcategories[1]
        self.selectedTitle = self.categorytitles[1]
        
        
        self.parent.destroy()
        
    def getCategory(self):
        
        return self.selectedCategory, self.selectedTitle
        

class CategoryCheckApp:
    
    def __init__(self, parent):
        self.parent = parent
        
        self.allcategories = ['PersonalComputerPCOfDesktop_3',
                              'MobieleTelefoonOfSmartphone_6','Spelcomputer_7',
                              'SpelletjesMuziekAfSpelenDownloaden_44',
                              'SociaalNetwerk_31']
        
        self.categorytitles = ['Using Internet on a Personal Computer',
                               'Using internet on a Smartphone',
                               'Using internet on a Gaming System',
                               'Using internet to play and download music and/or games',
                               'Using internet for Social Media']
        self.selectedCategories = []
        self.selectedTitles = []
        
        self.label = tk.Label(text = "Choose categories you'd like to compare:")
        self.label.pack()
        
        # Make container
        self.container = tk.Frame(self.parent)
        self.container.pack()

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
        
        nextButton = tk.Button(self.container, text="Next")
        nextButton.pack()
        nextButton.bind("<Button-1>", self.nextPage)
        
    def nextPage(self, event):
        
        for i in range(len(self.vars)):
            if self.vars[i].get() == 1:
                self.selectedCategories.append(self.allcategories[i])
                self.selectedTitles.append(self.categorytitles[i])
        
        print(self.selectedCategories)
        self.parent.destroy()
        
    def getCategories(self):
        
        return self.selectedCategories, self.selectedTitles


class LineApp:

    def __init__(self, parent, data, labels):
        self.parent = parent
        self.years = ['2012','2013','2014','2015','2016','2017','2018']

        # Make frame
        frame = tk.Frame(self.parent, width=1000)

        # Make a figure and insert the plot
        fig = Figure()
        ax = fig.add_subplot(111)
        for i in range(len(data)):
            ax.plot(self.years, data[i], label=labels[i])
        ax.legend()
        ax.grid()
        
        # Make a canvas in the frame and add figure
        self.canvas = FigureCanvasTkAgg(fig, master=parent)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
        frame.pack()
        

class BarApp:
    
    def __init__(self, parent, data, titles):
        self.parent = parent
        
        # Make frame
        frame = tk.Canvas(self.parent, width=1000) 
        
        # Make a figure and insert barplot
        fig = Figure()
        barwidth = 0.25
        y_pos = np.arange(len(titles))
        y_pos2 = [x + barwidth for x in y_pos]
        ax = fig.add_subplot(111)
        ax.bar(y_pos, data[0], color="blue", width=barwidth, label="Men")
        ax.bar(y_pos2, data[1], color="red", width=barwidth, label="Women")
        ax.legend()
        ax.set_xticks(y_pos + barwidth / 2)
        ax.set_xticklabels(titles)
        ax.set_ylim([0,100])
        ax.grid()
        
        
        # Make a canvas in the frame and add figure
        self.canvas = FigureCanvasTkAgg(fig, master=parent)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
        frame.pack()  

# Quick function to load up a file correctly.
def loadData(file):
    df = pd.read_csv(file, sep=';')
    df_obj = df.select_dtypes(['object'])
    df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())
    return df

# Function that will plot the demo.
def ageDemo():
    #Putting the target variables from dataset into easily readable variables and lists.
    filename = '83429NED_UntypedDataSet_19032019_231356.csv'
    generations= ['12-18', '18-25', '25-35','35-45', '45-55', '55-65', '65-75', '75+']
    gencodes = ['52020', '53105', '53500', '53700', '53800', '53900', '53925', '21600']
    yearcodes = ['2012JJ00','2013JJ00','2014JJ00','2015JJ00','2016JJ00','2017JJ00','2018JJ00']
    certain = 'MW00000'
    research = 'BijnaElkeDag_13'
    #loading the correct file
    data = loadData(filename)
    
    #creating subset for test
    subset = data[(data['Marges'] == certain) & (data['Perioden'].isin(yearcodes))]
    
    #creating list of lists to store the yearly results per generation.
    genresults = []
    for x in range(len(gencodes)):
        yearresults = []
        for y in range(len(yearcodes)):
            yearresults.append(0)
        genresults.append(yearresults)
    
    # Iterating over each row and saving the target values in our brand new list of lists.
    for index, row in subset.iterrows():
        if(row.loc['KenmerkenPersonen'] in gencodes):
            indexkenmerk = gencodes.index(row.loc['KenmerkenPersonen'])
            indexyear = yearcodes.index(row.loc['Perioden'])
            genresults[indexkenmerk][indexyear] = row.loc[research] 
    
#    # Plotting the target values by generation. Including a legend and a label for clarity.
#    for i in range(len(genresults)):
#        mp.plot(years, genresults[i], label = generations[i])
#        mp.ylabel("Percentage of daily usage")
#        mp.legend()
#    mp.show()

    return genresults, generations

def societyDemo(research):
    
    #Putting the target variables from dataset into easily readable variables and lists.
    filename = '83429NED_UntypedDataSet_19032019_231356.csv'
    partspaygrade = ['First 20%', 'Second 20%','Thirth 20%','Fourth 20%','Fifth 20%']
    partspaygradecodes = ['1014752', '1014753', '1014754', '1014755', '1014756']
    yearcodes = ['2012JJ00','2013JJ00','2014JJ00','2015JJ00','2016JJ00','2017JJ00','2018JJ00']
    certain = 'MW00000'
    #research = 'BijnaElkeDag_13'
    
    #loading the correct file
    data = loadData(filename)
    
    #creating subset for test
    subset = data[(data['Marges'] == certain) & (data['KenmerkenPersonen'].isin(partspaygradecodes))]
    
    # Set all to 0
    paygrade = []
    for x in range(len(partspaygrade)):
        yearresults = []
        for y in range(len(yearcodes)):
            yearresults.append(0)
        paygrade.append(yearresults)
    
    # fill in all categories with their percentages    
    for index, row in subset.iterrows():
        if(row.loc['KenmerkenPersonen'] in partspaygradecodes):
            indexkenmerk = partspaygradecodes.index(row.loc['KenmerkenPersonen'])
            indexyear = yearcodes.index(row.loc['Perioden'])
            paygrade[indexkenmerk][indexyear] = row.loc[research]
    
#    # Plotting the target values by generation. Including a legend and a label for clarity.
#    for i in range(len(paygrade)):
#        mp.plot(years, paygrade[i], label = partspaygrade[i])
#        mp.ylabel("Percentage of daily usage")
#        mp.legend()
#    mp.show()
    
    return paygrade, partspaygrade
    
def genderDemo(categories):
    
    #Putting the target variables from dataset into easily readable variables and lists.
    filename = '83429NED_UntypedDataSet_19032019_231356.csv'
    gendercodes = ['3000', '4000']
    yearcodes = ['2012JJ00','2013JJ00','2014JJ00','2015JJ00','2016JJ00','2017JJ00','2018JJ00']
    certain = 'MW00000'
    
    #loading the correct file
    data = loadData(filename)
    
    #creating subset for test
    subset = data[(data['Marges'] == certain) & (data['KenmerkenPersonen'].isin(gendercodes))]
    
    #set every category for both genders to 0
    manresults = []
    womanresults = []
    for x in range(len(categories)):
        manresults.append(0)
        womanresults.append(0)
    
    # Add up all percentages over all 7 years
    for index, category in enumerate(categories):
        for i, row in subset.iterrows():
            if (row.loc['KenmerkenPersonen'] == gendercodes[0]):
                manresults[index] += float(row[category])
            elif (row.loc['KenmerkenPersonen'] == gendercodes[1]):
                womanresults[index] += float(row[category])
    
    # Scale to mean per year      
    years = len(yearcodes)      
    for i in range(len(manresults)):
        manresults[i] = manresults[i]/years
        womanresults[i] = womanresults[i]/years
    
#    barwidth = 0.25  
#    y_pos = np.arange(len(categories))
#    y_pos2 = [x + barwidth for x in y_pos] 
#    mp.bar(y_pos, manresults, color="blue", width=barwidth)
#    mp.bar(y_pos2, womanresults, color="red", width=barwidth)
#    mp.xticks(y_pos, categories)
#    mp.ylabel('Availebility')
#    mp.title('Availebility per gender')
#    
#    mp.legend()
#    mp.show()
    
    return [manresults, womanresults], categories
         

question = []

def main():

    # Create first frame
    root1 = tk.Tk()
    InsertDataApp(root1)
    root1.lift()
    root1.mainloop()
    
    data = []
    labels = []

    try:
        # Check which question is selected
        if question[-1] == "Q1":
            # Run selected question
            data, labels = ageDemo()
            
            # Create frame to plot
            root2 = tk.Tk()
            LineApp(root2, data, labels)
            root2.lift()
            root2.mainloop()
        elif question[-1] == "Q2":
            # Create frame to select a category
            root2 = tk.Tk()
            app = CategoryChoiceApp(root2)
            root2.lift()
            root2.mainloop()
            
            # Ask for selected category
            category, title = app.getCategory()
            
            # Run selected question
            data, labels = societyDemo(category)
            
            # Create frame to plot
            root3 = tk.Tk()
            LineApp(root3, data, labels)
            root3.lift()
            root3.mainloop()
        elif question[-1] == "Q3":            
            # Create frame to select categories
            root2 = tk.Tk()
            app = CategoryCheckApp(root2)
            root2.lift()
            root2.mainloop()
            
            # Ask for selected categories
            categories, titles = app.getCategories()
            
            # Run selected question
            data, labels = genderDemo(categories)
            
            # Create frame to plot
            root3 = tk.Tk()
            BarApp(root3, data, titles)
            root3.lift()
            root3.mainloop()
            
    except Exception as ex:
        arguments = ex.args
        print (f"An exception of type {type(ex).__name__} occurred. Arguments:" +
                                       f"\n {arguments}")

if __name__ == "__main__":
   main()  