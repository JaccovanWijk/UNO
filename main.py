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
                                  "Comparing difference in age per year")
        self.Q1Button.pack()
        self.Q1Button.bind("<Button-1>", self.insertQ1)

        self.Q2Button = tk.Button(self.container, text=
                                  "Camparing parts of society")
        self.Q2Button.pack()
        self.Q2Button.bind("<Button-1>", self.insertQ2)

        self.Q3Button = tk.Button(self.container, text=
                                  "Comparing different genders")
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


class LineApp:

    def __init__(self, parent, data, labels):
        self.parent = parent
        self.years = ['2012','2013','2014','2015','2016','2017','2018']

        # Make frame
        frame = tk.Frame(self.parent)

        # Make a figure and insert the plot
        fig = Figure()
        ax = fig.add_subplot(111)
        for i in range(len(data)):
            ax.plot(self.years, data[i], label=labels[i])
        ax.legend()
        
        # Make a canvas in the frame and add figure
        self.canvas = FigureCanvasTkAgg(fig, master=parent)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
        frame.pack()
        

class BarApp:
    
    def __init__(self, parent, data, labels):
        self.parent = parent
        
        # Make frame
        frame = tk.Frame(self.parent) 
        
        # Make a figure and insert barplot
        fig = Figure()
        barwidth = 0.25
        y_pos = np.arange(len(labels))
        y_pos2 = [x + barwidth for x in y_pos]
        ax = fig.add_subplot(111)
        ax.bar(y_pos, data[0], color="blue", width=barwidth, label="Men")
        ax.bar(y_pos2, data[1], color="red", width=barwidth, label="Women")
        ax.legend()
        
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
    years = ['2012','2013','2014','2015','2016','2017','2018']
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

def societyDemo():
    
    #Putting the target variables from dataset into easily readable variables and lists.
    filename = '83429NED_UntypedDataSet_19032019_231356.csv'
    partspaygrade = ['First 20%', 'Second 20%','Thirth 20%','Fourth 20%','Fifth 20%']
    partspaygradecodes = ['1014752', '1014753', '1014754', '1014755', '1014756']
    years = ['2012','2013','2014','2015','2016','2017','2018']
    yearcodes = ['2012JJ00','2013JJ00','2014JJ00','2015JJ00','2016JJ00','2017JJ00','2018JJ00']
    certain = 'MW00000'
    research = 'BijnaElkeDag_13'
    
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
    
def genderDemo():
    
    #Putting the target variables from dataset into easily readable variables and lists.
    filename = '83429NED_UntypedDataSet_19032019_231356.csv'
    gendercodes = ['3000', '4000']
    categories = ['ToegangTotInternet_1','PersonalComputerPCOfDesktop_3','MobieleTelefoonOfSmartphone_6','Spelcomputer_7']
    yearcodes = ['2012JJ00','2013JJ00','2014JJ00','2015JJ00','2016JJ00','2017JJ00','2018JJ00']
    certain = 'MW00000'
    
    #loading the correct file
    data = loadData(filename)
    
    #SEP IS KONINGS
    
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
            # Run selected question
            data, labels = societyDemo()
            
            # Create frame to plot
            root2 = tk.Tk()
            LineApp(root2, data, labels)
            root2.lift()
            root2.mainloop()
        elif question[-1] == "Q3":
            # Run selected question
            data, labels = genderDemo()
            
            # Create frame to plot
            root2 = tk.Tk()
            BarApp(root2, data, labels)
            root2.lift()
            root2.mainloop()
            
    except Exception as ex:
        arguments = ex.args
        print (f"An exception of type {type(ex).__name__} occurred. Arguments:" +
                                       f"\n {arguments}")

if __name__ == "__main__":
   main()  