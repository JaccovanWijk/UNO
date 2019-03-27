# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 19:22:52 2019

@author: sepke
"""

import pandas as pd
import matplotlib.pyplot as mp
import numpy as np

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
    
    # Plotting the target values by generation. Including a legend and a label for clarity.
    for i in range(len(genresults)):
        mp.plot(years, genresults[i], label = generations[i])
        mp.ylabel("Percentage of daily usage")
        mp.legend()
    mp.show()

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
    
    print(paygrade)
    
    # Plotting the target values by generation. Including a legend and a label for clarity.
    for i in range(len(paygrade)):
        mp.plot(years, paygrade[i], label = partspaygrade[i])
        mp.ylabel("Percentage of daily usage")
        mp.legend()
    mp.show()
    
def genderDemo():
    
    #Putting the target variables from dataset into easily readable variables and lists.
    filename = '83429NED_UntypedDataSet_19032019_231356.csv'
    gendercodes = ['3000', '4000']
    categories = ['ToegangTotInternet_1','PersonalComputerPCOfDesktop_3','MobieleTelefoonOfSmartphone_6','Spelcomputer_7']
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
    
    barwidth = 0.25  
    y_pos = np.arange(len(categories))
    y_pos2 = [x + barwidth for x in y_pos] 
    mp.bar(y_pos, manresults, color="blue", width=barwidth)
    mp.bar(y_pos2, womanresults, color="red", width=barwidth)
    mp.xticks(y_pos, categories)
    mp.ylabel('Availebility')
    mp.title('Availebility per gender')
    
    mp.legend()
    mp.show()
         

# Creating a user-interface while-loop.
while True:
    print('Options: \n', '1: Show internet usage per generation \n', '2: Show part of society with the least internet growth \n', '3: Show difference in internet usage between men/women \n' , '4: Exit' )
    
    #Try-Except to catch non-number inputs.
    try:
        option = int(input("What service would you like from us today (1-4)? : "))
    except ValueError:
        print("Enter a number")
    # Calling necessary functions that are requested by user (Still in progress.)
    if option == 1:
        ageDemo()
    elif option == 2:
        societyDemo()
    elif option == 3: 
        genderDemo()
    else:
        break;    
    