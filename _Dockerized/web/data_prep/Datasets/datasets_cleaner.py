# -*- coding: utf-8 -*-



import pandas as pd


## Function that separates useful columns from Ordnance Survey Ireland datasets

def prep_data(csv):
    dataset = pd.read_csv(csv)
    dataset = dataset[['X','Y','County','English_Name']]
    dataset['county'] = dataset['County'].str.title()
    dataset['townland'] = dataset['English_Name'].str.title()
    dataset = dataset.iloc[:,[0,1,4,5]]
    dataset.to_csv(csv, index=False,encoding = "utf-8")
    
prep_data("centres_of_population.csv")    
prep_data("townlands.csv")      
prep_data("baronies.csv")  
prep_data("civil_parishes.csv")      
prep_data("counties.csv")  


### Alternative Names may be useful as well

dataset = pd.read_csv("centres_of_population.csv")
dataset = dataset[['X','Y','County','Alternative_Name']]
dataset['county'] = dataset['County'].str.title()
dataset['townland'] = dataset['Alternative_Name'].str.title()
dataset = dataset.loc[dataset['townland'].notnull()]
dataset = dataset.iloc[:,[0,1,4,5]]
dataset.to_csv("centres_of_population_alt.csv", index=False, encoding = "utf-8")


## Creating dataset with all the localities

centres_of_population = pd.read_csv("centres_of_population.csv")
townlands = pd.read_csv("townlands.csv")
baronies = pd.read_csv("baronies.csv")
civil_parishes = pd.read_csv("civil_parishes.csv")
localities_alt = pd.read_csv("centres_of_population_alt.csv")


## Merge to one dataframe

localities_full = pd.concat([centres_of_population, townlands, baronies, civil_parishes, localities_alt])


## Save to CSV

localities_full.to_csv("localities_full.csv", index=False, encoding = "utf-8")














