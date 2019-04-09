# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 19:22:52 2019

@author: UNO - Unified negotiation organization
"""
#import relevant modules

#pandas for the datastructures
import pandas as pd
#tkinter to make a nice interface
import tkinter as tk
#sys to make an exit button
import sys

#all of the classes

#choosing category to research in the interface
import CategoryChoiceApp as co

#choosing multiple categories to research in the interface
import CategoryCheckApp as ce

#choosing  part of society to research
import SocietyChoiceApp as s

#choosing which question you want to be answered
import QuestionApp as q

#classes for line and barplots
import LineApp as l
import BarApp as b

# Quick function to load a file correctly.
def loadData(file):
    try:
        df = pd.read_csv(file, sep=';')
        df_obj = df.select_dtypes(['object'])
        df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())
        return df
    except: 
        print("Could not load file")
        return False

# Function that will plot the demo.
def ageDemo(research):
    #Putting the target variables from dataset into easily readable variables and lists.
    filename = '83429NED_UntypedDataSet_19032019_231356.csv'
    gencodes = ['52020', '53105', '53500', '53700', '53800', '53900', '53925', '21600']
    generations = ['12-18', '18-25', '25-35', '35-45', '45-55', '55-65', '65-75', '75+']
    yearcodes = ['2012JJ00','2013JJ00','2014JJ00','2015JJ00','2016JJ00','2017JJ00','2018JJ00']
    certain = 'MW00000'
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
    
    #replacing all .'s with 0's to avoid potential calculation errors
    for i in range(len(genresults)):
        for j in range(len(genresults[i])):
            if genresults[i][j] == '.':
                genresults[i][j] = '0'

    return genresults, generations

def societyDemo(research, data):
    #Putting the target variables from dataset into easily readable variables and lists.
    filename = '83429NED_UntypedDataSet_19032019_231356.csv'
    yearcodes = ['2012JJ00','2013JJ00','2014JJ00','2015JJ00','2016JJ00','2017JJ00','2018JJ00']
    certain = 'MW00000'
    societyPartCodes = data[0]
    societyParts = data[1]
    
    #loading the correct file
    data = loadData(filename)
    
    #creating subset for test
    subset = data[(data['Marges'] == certain) & (data['KenmerkenPersonen'].isin(societyPartCodes))]
    
    # Set all to 0
    data = []
    for x in range(len(societyParts)):
        yearresults = []
        for y in range(len(yearcodes)):
            yearresults.append(0)
        data.append(yearresults)
    
    # fill in all categories with their percentages    
    for index, row in subset.iterrows():
        if(row.loc['KenmerkenPersonen'] in societyPartCodes):
            indexkenmerk = societyPartCodes.index(row.loc['KenmerkenPersonen'])
            indexyear = yearcodes.index(row.loc['Perioden'])
            data[indexkenmerk][indexyear] = row.loc[research]
    
    return data
    
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
    
    return [manresults, womanresults], categories
         

def main():
    
    while True:
        
        # Create first frame
        root1 = tk.Tk()
        app0 = q.QuestionApp(root1)
        root1.lift()
        root1.title("Subject")
        root1.mainloop()
        
        print(app0.getQuestion())
        
        if app0.getExit():
            sys.exit()
        
        data = []
        labels = []
        question = app0.getQuestion()
    
        try:
            # Check which question is selected
            if question == "Q1":
                # Create frame to select a category
                root2 = tk.Tk()
                app = co.CategoryChoiceApp(root2)
                root2.lift()
                root2.title("Category")
                root2.mainloop()
                
                # Check if exit- or homebutton is pressed
                if app.getExit():
                    sys.exit()
                elif not app.getHome():
                    # Ask for selected category
                    category, title = app.getCategory()
                    
                    # Run selected question
                    data, labels = ageDemo(category)
                    
                    # Create frame to plot
                    root3 = tk.Tk()
                    app4 = l.LineApp(root3, data, labels, title)
                    root3.lift()
                    root3.title("Data")
                    root3.mainloop()
                    
                    if app4.getExit():
                        sys.exit()
                        
            elif question == "Q2":
                # Create frame to select a category
                root2 = tk.Tk()
                app1 = co.CategoryChoiceApp(root2)
                root2.lift()
                root2.title("Category")
                root2.mainloop()
                
                if app1.getExit():
                    sys.exit()
                elif not app1.getHome():
                    # Ask for selected category
                    category, title = app1.getCategory()
                    
                    root4 = tk.Tk()
                    app2 = s.SocietyChoiceApp(root4)
                    root4.lift()
                    root4.title("Society")
                    root4.mainloop()
                    
                    if app2.getExit():
                        sys.exit()
                    elif not app2.getHome():
                        societyPart = app2.getSocietyPart()
                        
                        # Run selected question
                        data = societyDemo(category, societyPart)
                        
                        # Create frame to plot
                        root3 = tk.Tk()
                        app4 = l.LineApp(root3, data, societyPart[1], title)
                        root3.lift()
                        root3.title("Data")
                        root3.mainloop()
                        
                        if app4.getExit():
                            sys.exit()
                            
            elif question == "Q3":            
                # Create frame to select categories
                root2 = tk.Tk()
                app = ce.CategoryCheckApp(root2)
                root2.lift()
                root2.title("Category")
                root2.mainloop()
                title = 'Internet usage per gender'
                
                if app.getExit():
                    sys.exit()
                elif not app.getHome():
                    # Ask for selected categories
                    categories, titles = app.getCategories()
                    
                    # Run selected question
                    data, labels = genderDemo(categories)
                    
                    # Create frame to plot
                    root3 = tk.Tk()
                    app4 = b.BarApp(root3, data, titles, title)
                    root3.lift()
                    root3.title("Data")
                    root3.mainloop()
                    
                    if app4.getExit():
                        sys.exit()
                
        except Exception as ex:
            arguments = ex.args
            print (f"An exception of type {type(ex).__name__} occurred. Arguments:" +
                                           f"\n {arguments}")

if __name__ == "__main__":
   main()  