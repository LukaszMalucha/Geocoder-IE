# -*- coding: utf-8 -*-


import pandas as pd 

## Uploading geocoded dataset
dataset = pd.read_csv("geocoded_all.csv")


## Merging all address columns into one, starting with the last one

dataset['address'] = dataset['rest'].map(str) + ', ' + dataset['address_4'].map(str) + ', ' + \
                     dataset['address_3'].map(str) + ', ' + dataset['address_2'].map(str) + \
                     ', ' + dataset['address_1'].map(str) + ', ' + dataset['townland'].map(str)
                     
## Housekeeping             

dataset['address'] = dataset['address'].str.replace('nan,', "")    
dataset['address'] = dataset['address'].str.replace('  ', " ")     
dataset['address'] = dataset['address'].str.replace('   ', " ") 
dataset['address'] = dataset['address'].str.replace('  ', " ")              
dataset['address'] = dataset['address'].str.strip()         

## Preparing desired columns

geocoded_addresses = dataset.iloc[:, [0,7,8,9]]    
geocoded_addresses = geocoded_addresses[['county','address','long','lat']]        

## Saving dataset

geocoded_addresses.to_csv("geocoded_addresses.csv", index=False, encoding = "utf-8")   