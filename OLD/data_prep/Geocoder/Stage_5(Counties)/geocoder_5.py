# -*- coding: utf-8 -*-



import pandas as pd 

## Upload Counties CSV and creating dictionary

dataset = pd.read_csv("counties.csv")
dataset = dataset.drop_duplicates()
localities_dict = dataset.to_dict('records')

## Uploading un-geocoded dataset from Stage 4

geocode = pd.read_csv("geocode.csv")
geocode['long'] = ""
geocode['lat'] = ""


## Address search function

for index, row in geocode.iterrows():
    for element in localities_dict:
            if row['county'] == element['county']: 
                row['long'] = str(element['X'])
                row['lat'] = str(element['Y'])
            if row['county'] == "Dun Laoghaire-Rathdown":  
                row['long'] = "-6.173638367"
                row['lat'] = "53.2108073991251"
                
                
                

## Preparing csv files for Final Stage

geocode.to_csv("geocoded_5.csv", index=False, encoding = "utf-8")    