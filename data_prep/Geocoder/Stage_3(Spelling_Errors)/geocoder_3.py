# -*- coding: utf-8 -*-

import pandas as pd 


## Upload Full Localities CSV and creating dictionary

dataset = pd.read_csv("localities_full.csv")
dataset = dataset.drop_duplicates()
localities_dict = dataset.to_dict('records')

## Uploading un-geocoded dataset from Stage 2

geocode = pd.read_csv("geocode.csv")
geocode['long'] = ""
geocode['lat'] = ""

## Fixing some spelling errors

geocode['townland'] = geocode['townland'].str.replace('Ballintubber', "Ballintubbert")
geocode['townland'] = geocode['townland'].str.replace('Ballyduff Upper', "Ballyduff")
geocode['townland'] = geocode['townland'].str.replace('Carrigtoohil', "Carrigtohill")
geocode['townland'] = geocode['townland'].str.replace('Carrigtwohill', "Carrigtohill")
geocode['townland'] = geocode['townland'].str.replace('Castleboro', "Castleboro Demesne")
geocode['townland'] = geocode['townland'].str.replace('Lissarda', "Lissardagh")
geocode['townland'] = geocode['townland'].str.replace('Pettigo', "Pettigoe")
geocode['townland'] = geocode['townland'].str.replace('Rathcormac', "Rathcormack")


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
                
## 16 hits


## Merging Geocoded addresses into one dataframe

geocoded_3 = addresses_townland_geocoded
    
## Dataframe for addresses that still need to be geocoded   

geocode = addresses_townland  


## Preparing csv files for Stage 4

geocoded_3.to_csv("geocoded_3.csv", index=False,encoding = "utf-8")
geocode.to_csv("geocode.csv", index=False,encoding = "utf-8") 


  
                
                





