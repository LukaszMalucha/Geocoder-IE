# -*- coding: utf-8 -*-



import pandas as pd 


## Upload Localities CSV and creating dictionary

dataset = pd.read_csv("other_localities.csv")
dataset = dataset.drop_duplicates()
localities_dict = dataset.to_dict('records')


## Uploading un-geocoded dataset from Stage 1

addresses = pd.read_csv("geocode.csv")
addresses['long'] = ""
addresses['lat'] = ""


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


##################
                    
address_geocoder(addresses,'address_2')                     
                    
addresses_2_geocoded = addresses.loc[addresses['long'] != '']
addresses_2 = addresses.loc[addresses['long'] == '']                      
                    
################### 
                   
address_geocoder(addresses_2,'address_1') 

addresses_1_geocoded = addresses_2.loc[addresses_2['long'] != '']
addresses_1 = addresses_2.loc[addresses_2['long'] == ''] 

###################

address_geocoder(addresses_1,'townland') 

addresses_townland_geocoded = addresses_1.loc[addresses_1['long'] != '']
addresses_townland = addresses_1.loc[addresses_1['long'] == ''] 

## 131 hits all together  


## Merging Geocoded addresses into one dataframe

geocoded_2 = pd.concat([addresses_2_geocoded, addresses_1_geocoded, 
                        addresses_townland_geocoded ] )
    
    
## Dataframe for addresses that still need to be geocoded    
   
geocode = addresses_townland  


## Preparing csv files for Stage 3

geocoded_2.to_csv("geocoded_2.csv", index=False,encoding = "utf-8")
geocode.to_csv("geocode.csv", index=False,encoding = "utf-8") 


















