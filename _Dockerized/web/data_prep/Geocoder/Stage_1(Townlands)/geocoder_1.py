# -*- coding: utf-8 -*-

import pandas as pd 

## Uplaod Townlands CSV to dataframe
dataset = pd.read_csv("townlands.csv")

## As dataset doesn't have Dublin addresses

dataset = dataset[dataset.county != 'Dublin']


## Create townlands dictionary to check against addresses

townland_dict = dataset.to_dict('records')


## Upload addresses

addresses = pd.read_csv("addresses_clean.csv")

## Adding long & lat columns

addresses['long'] = ""
addresses['lat'] = ""

                
## Address search function

def address_geocoder(data, col): 
    for index, row in data.iterrows():
        if row[col] != 'None':
            for element in townland_dict:
                    if row['county'] == element['county']:
                        if row[col] == element['townland']:
                            row['long'] = str(element['X'])
                            row['lat'] = str(element['Y'])                 
    return data               
                    
                    
          
## Checking addresses columns staritng with the last one. On each stage separating
## geocoded addresses from the not-geocoded ones
          
      
address_geocoder(addresses,'rest') 

addresses_rest_geocoded = addresses.loc[addresses['long'] != '']
addresses_rest = addresses.loc[addresses['long'] == '']

## 1665 hits

###################

address_geocoder(addresses_rest,'address_4') 

addresses_4_geocoded = addresses_rest.loc[addresses_rest['long'] != '']
addresses_4 = addresses_rest.loc[addresses_rest['long'] == '']

## 0 hits
                   
###################

address_geocoder(addresses_4,'address_3')                     
                    
addresses_3_geocoded = addresses_4.loc[addresses_4['long'] != '']
addresses_3 = addresses_4.loc[addresses_4['long'] == '']            

## 0 hits        
                    
##################
                    
address_geocoder(addresses_3,'address_2')                     
                    
addresses_2_geocoded = addresses_3.loc[addresses_3['long'] != '']
addresses_2 = addresses_3.loc[addresses_3['long'] == '']            

## 24 hits          
                    
################### 
                   
address_geocoder(addresses_2,'address_1') 

addresses_1_geocoded = addresses_2.loc[addresses_2['long'] != '']
addresses_1 = addresses_2.loc[addresses_2['long'] == ''] 

## 101 hits  

###################

address_geocoder(addresses_1,'townland') 

addresses_townland_geocoded = addresses_1.loc[addresses_1['long'] != '']
addresses_townland = addresses_1.loc[addresses_1['long'] == ''] 

## 914 hits


## Merging Geocoded addresses into one dataframe

geocoded_1 = pd.concat([addresses_rest_geocoded,addresses_4_geocoded, 
                        addresses_3_geocoded, addresses_2_geocoded, 
                        addresses_1_geocoded, addresses_townland_geocoded ] )


## Dataframe for addresses that still need to be geocoded
   
geocode = addresses_townland  


## Preparing csv files for Stage 2

geocoded_1.to_csv("geocoded_1.csv", index=False,encoding = "utf-8")
geocode.to_csv("geocode.csv", index=False,encoding = "utf-8")  

    








