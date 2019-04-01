# -*- coding: utf-8 -*-


import pandas as pd 

## Upload Alternative Townland Names CSV and creating dictionary

dataset = pd.read_csv("centres_of_population_alt.csv")
dataset = dataset.drop_duplicates()
localities_dict = dataset.to_dict('records')


## Uploading un-geocoded dataset from Stage 3

geocode = pd.read_csv("geocode.csv")
geocode['long'] = ""
geocode['lat'] = ""


## Address search function

def address_geocoder(data, col): 
    for index, row in data.iterrows():
        if row[col] != 'None':
            for element in localities_dict:
                    if row['county'] == element['county']:
                        if row[col] == element['townland']:
                            row['long'] = str(element['X'])
                            row['lat'] = str(element['Y'])                 
    return data   



address_geocoder(geocode,'townland')                     
                    
addresses_townland_geocoded = geocode.loc[geocode['long'] != '']
addresses_townland = geocode.loc[geocode['long'] == '']  


geocoded_4 = addresses_townland_geocoded
geocode = addresses_townland  

## 0 hits

## Preparing csv files for Stage 5

geocoded_4.to_csv("geocoded_4.csv", index=False,encoding = "utf-8")
geocode.to_csv("geocode.csv", index=False,encoding = "utf-8") 
                             