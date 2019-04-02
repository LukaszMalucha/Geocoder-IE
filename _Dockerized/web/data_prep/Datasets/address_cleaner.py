# -*- coding: utf-8 -*-


import pandas as pd


#### Uploading dataset
dataset = pd.read_csv("addresses_for_task.csv")


### Separating parts of the address going backwards


######################################################################## COUNTY ################################################

## Desired county form = "Kerry"
dataset = pd.DataFrame(dataset['Address'].str.rsplit(',', 1).tolist(), columns=["address", "county"])


## Housekeeping
dataset['county'] = dataset['county'].str.strip()
dataset['county'] = dataset['county'].str.replace('Co. ', "")
dataset['county'] = dataset['county'].str.capitalize()

## Final check
county_unique = pd.Series(dataset['county'].unique())

## Quick Fix
dataset['county'] = dataset['county'].str.replace('Dunlaoghaire_rathdown', "Dun Laoghaire-Rathdown")



###################################################################### TOWNLAND ################################################

## Desired townland form = " Cratloe"
townland_data = pd.DataFrame(dataset['address'].str.rsplit(',', 1).tolist(), columns=["address", "townland"])

## Housekeeping
townland_data["townland"] = townland_data["townland"].str.strip()
townland_data["townland"] = townland_data["townland"].str.title()
townland_data["townland"] = townland_data["townland"].str.replace('~', "")
townland_data["townland"] = townland_data["townland"].str.replace('.', "")
townland_data["townland"] = townland_data["townland"].str.replace('(', "")
townland_data["townland"] = townland_data["townland"].str.replace(')', "")
townland_data["townland"] = townland_data["townland"].str.replace(' Po', "")
townland_data["townland"] = townland_data["townland"].str.replace('O Briensbridge', "O'Briensbridge")
townland_data["townland"] = townland_data["townland"].str.replace('Errarooey Mor', "Errarooey More")

townland_data['address'] = townland_data['address'].str.strip()
townland_data['address'] = townland_data['address'].str.replace('.', "")
townland_data['address'] = townland_data['address'].str.replace("'", "")
townland_data['address'] = townland_data['address'].str.replace('"', "")
townland_data['address'] = townland_data['address'].str.replace('-', "")    
townland_data['address'] = townland_data['address'].str.replace('(', "") 
townland_data['address'] = townland_data['address'].str.replace(')', "") 
townland_data['address'] = townland_data['address'].str.replace('N/A', "") 
townland_data['address'] = townland_data['address'].str.replace('n/a', "") 
townland_data['address'] = townland_data['address'].str.replace('/', ",") 
townland_data['address'] = townland_data['address'].str.title()


## Replace empty spots with None

for index, row in townland_data.iterrows():
    if row['townland'] == None or row['townland'] == ' ':
        row['townland'] = 'None'
    elif row['address'] == None or row['address'] == ' ':
        row['address'] = 'None'    
    
    
################################################################### LOCAL AREAS ################################################
 


local_data = pd.DataFrame(townland_data['address'])


## Splitting rest of the address by comas going backwards

local_data_1 = pd.DataFrame(local_data['address'].str.rsplit(',', 1).tolist(), columns=["address", "address_1"])

local_data_2 = pd.DataFrame(local_data_1['address'].str.rsplit(',', 1).tolist(), columns=["address", "address_2"])

local_data_3 = pd.DataFrame(local_data_2['address'].str.rsplit(',', 1).tolist(), columns=["address", "address_3"])

local_data_4 = pd.DataFrame(local_data_3['address'].str.rsplit(',', 1).tolist(), columns=["address", "address_4"])



## Filling the gaps

for index, row in local_data_4.iterrows():
    if row['address'] == None or row['address'] == '':
        row['address'] = 'None'
        
for index, row in local_data_4.iterrows():
    if row['address_4'] == None or row['address_4'] == ' ':
        row['address_4'] = 'None'
        
for index, row in local_data_3.iterrows():
    if row['address_3'] == None or row['address_3'] == ' ':
        row['address_3'] = 'None'        

for index, row in local_data_2.iterrows():
    if row['address_2'] == None or row['address_2'] == ' ' or row['address_2'] == '':
        row['address_2'] = 'None'        

for index, row in local_data_1.iterrows():
    if row['address_1'] == None or row['address_1'] == ' ' or row['address_1'] == '':
        row['address_1'] = 'None' 


## Assembling partitioned address into dataframe 

addresses_clean = pd.DataFrame()
addresses_clean["county"]    = dataset['county']
addresses_clean["townland"]  = townland_data["townland"]
addresses_clean["address_1"] = local_data_1["address_1"].str.strip()
addresses_clean["address_2"] = local_data_2["address_2"].str.strip()
addresses_clean["address_3"] = local_data_3["address_3"].str.strip()
addresses_clean["address_4"] = local_data_4["address_4"].str.strip()
addresses_clean["rest"] = local_data_4["address"].str.strip()


## Saving dataframe to csv

addresses_clean.to_csv("addresses_clean.csv", index = False, encoding = "utf-8")







