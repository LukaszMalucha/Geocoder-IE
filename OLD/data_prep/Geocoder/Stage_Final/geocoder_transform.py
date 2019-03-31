# -*- coding: utf-8 -*-


import pandas as pd 

## Uploading Geocoded addresses from each stage

geocoded_1 = pd.read_csv("geocoded_1.csv")
geocoded_2 = pd.read_csv("geocoded_2.csv")
geocoded_3 = pd.read_csv("geocoded_3.csv")
geocoded_4 = pd.read_csv("geocoded_4.csv")
geocoded_5 = pd.read_csv("geocoded_5.csv")


## Create single dataframe

geocoded_all = pd.concat([geocoded_1, geocoded_2, geocoded_3, geocoded_4, geocoded_5])
geocoded_all.replace(to_replace = "None", value = "", inplace = True)


## Saving Dataframe

geocoded_all.to_csv("geocoded_all.csv", index=False, encoding = "utf-8")    









