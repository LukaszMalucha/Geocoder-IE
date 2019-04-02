# Geocoder IE



####[Visit the App](https://ireland-geocoder.herokuapp.com/)

<br>

![1](https://user-images.githubusercontent.com/26208598/55428834-e4d7c980-5581-11e9-991a-da9bf0a1a9f5.JPG)

<br>


## ASSIGNMENT

We received list of approx. 3000 Irish addresses from one of our Customers. Dataset came in form of CSV file, where each row corresponds with one address.
With having quick look we can determine that addresses will require preprocessing.

##### So what's our Task?

Our customer wants those addresses to be geocoded. They expect that each address will have corresponding longitude/latitude. 
Regarding accuracy they expect each geocode to be accurate at least at county level. Customer explicitly mentioned that Geocoding applications shouldn't be used (OSM, GM).

<br>

## PROJECT OVERVIEW

### THE APPROACH

First step will be to organize some good source of geocode data. 
Customer mentioned Ordnance Survey Ireland’s publicly available data and after quick look it looks promising. 
Second task will be matching both datasets - Customer Addresses and Geocode Data so we can easily compare them. 
We'll divide geocoding process into separate stages for better control and easier debugging.
After matching both datasets, we'll build publicly accessible web application.


### DATA PREPARATION


#### Ordnance Survey Ireland data(OSI)

There is 5 useful datasets available [here](https://data.gov.ie/data/search?q=gazetteer). After brief look we can determine that only 4 columns will have use for us - <br> | X | Y | County | English_Name |. 
Only exception is townlands dataset where additionally we'll use | Alternative Name | column.

Beside column separation we'll apply standard housekeeping duties (ex. str.title() ) and we'll save results to csv files.

##### Files

[Datasets](https://github.com/LukaszMalucha/Help-Me-Geocoder/tree/master/data_prep/Datasets/Data_OSI)<br>
[Dataset Cleaner](https://github.com/LukaszMalucha/Help-Me-Geocoder/blob/master/data_prep/Datasets/datasets_cleaner.py)

#### Customer's Dataset

After visual inspection we can already determine that this dataset need some standard housekeeping. Keen eye can also spot some spelling mistakes (that we are going to fix on flight).
In order to compare those addresses with OSI we'll divide each address on 5 columns. Coma will be our separator. We'll start by separating county then we'll separate remaining string starting from the end 
where we should find smallest administrative unit:

###### Address Before:

![4](https://user-images.githubusercontent.com/26208598/49391738-6af31900-f724-11e8-956f-d22b370418d8.PNG)

<br>

###### Address After:

![5](https://user-images.githubusercontent.com/26208598/49391739-6c244600-f724-11e8-9a61-1f70765a798e.PNG)

<br>

##### Files

[Address Cleaner](https://github.com/LukaszMalucha/Help-Me-Geocoder/blob/master/data_prep/Datasets/address_cleaner.py)



##### Tools Used

Pandas | Excel for visual checks  



### GEOCODER ARCHITECTURE 

#### Stage 1 - Townlands

Having our addresses separated on five parts, we'll start comparing them against our biggest OSI dataset - "townlands".
Our procedure is to start with the last column of an address ('rest' - smallest administrative unit). We'll compare it with OSI data. 
Once Address['rest'] matches OSI['townland'] it will append address row with OSI[X] and OSI[Y] column. 
After function application we'll divide our addresses into two separate dataframes - rows with appended geocode(X,Y) and those that were not match.

For unmatched rows we'll apply same function, but this time we move to 'address_4', so one stop higher in administrative hierarchy. Again we create two separate dataframes. 
Again we store geocoded rows and then try unmatched ones using 'address_3' and so on.... until we come to ['county'] column where we are going to stop for now.

<br>

![6](https://user-images.githubusercontent.com/26208598/49391742-6d557300-f724-11e8-9ae9-089b4d2082bd.PNG)



At the end we merge all geocoded dataframes into one csv file, and we proceed with unmatched addresses into next stage.


#### Stage 2 - Other Localities

Same procedure, but this time we check our addresses against other localities(parishes, baronies, centres of population) datasets. Still omiting counties column.

#### Stage 3 - Spelling Errors

Now as there is not that many address unmatched left let's try to fix some minor spelling errors match addresses again. No counties yet.

#### Stage 4 - Alternative Names

Matching against alternative townlands column. 

#### Stage 5 - Counties

For stubborn addresses that haven't found their perfect match yet (less that 10%), we are forced to apply county level geocode. In the future we may investigate an root cause of permanent mismatch.

#### Stage Final

Assembling our final document with all geocoded addresses. 


##### Files

[Geocoder](https://github.com/LukaszMalucha/Help-Me-Geocoder/tree/master/data_prep/Geocoder)


##### Tools Used

Pandas | Excel for visual checks  




### WEB APPLICATION


#### Structure

It's a Python Flask application, as that framework satisfies or needs in 100%. Web App is hosted on free Heroku server and it's publicly accessible.
App consits of two views and two databases.

#### Views

<br>


##### Manage User

<br>

![3](https://user-images.githubusercontent.com/26208598/55428837-e6a18d00-5581-11e9-97cd-562f81ce408a.JPG)

<br>



##### Geocoder
<br>

![1](https://user-images.githubusercontent.com/26208598/55428834-e4d7c980-5581-11e9-991a-da9bf0a1a9f5.JPG)

<br>

Main page of an application. Allows user to query address against geocode database. 
One can think about as an budget approach to our assignment, as it allows to retrive geocode for given address. But it's an really visually appealing, bonus addon.

<br>

##### Addresses
<br>

![2](https://user-images.githubusercontent.com/26208598/55428835-e5706000-5581-11e9-916c-2f0e3766d045.JPG)

<br>

Table of addresses from Customer assignment. Easily searchable, expandable and responsive. Pin icon can easily take us to Google Maps to verify geocode accuracy.


##### REST API Endpoints

<br>

![4](https://user-images.githubusercontent.com/26208598/55428844-eef9c800-5581-11e9-955c-5f6ddf251292.JPG)

<br>

#### Databases

To retrive geocoder data we use MongoDB database hosted on mLab. Easily expandable, with reasonably fast querries.
Full Irish localities data was uploaded with [mongo loader](https://github.com/LukaszMalucha/Help-Me-Geocoder/blob/master/data_prep/db_loader/mongo_loader.py).

Customer addresses are stored in sqlite3 local database, as we are not expecting large data expansion in a nearest future.
Addresses were uploaded with sqlite3 import csv command.


#### Additional Elements

Geocoder map was built with leaflet.js and mapbox layer.<br>
Addresses table was built with DataTables.js.<br>
There are various elements from Materialize & FontAwesome.<br>


#### Responsivity

Web App is Bootstrapped and fully responsive. 


## TOOLS, MODULES & TECHNIQUES:

##### Travis CI
[![Build Status](https://travis-ci.com/LukaszMalucha/Help-Me-Geocoder.svg?branch=master)](https://travis-ci.com/LukaszMalucha/Help-Me-Geocoder)

##### Python – web development:
Flask | CSS | Bootstrap | Materialize | Leaflet | DataTables | Heroku | Docker
##### Database:
Sqlite3 | Mongo DB 
##### Data Preprocessing:
Pandas



<br>
<br>
Enjoy,
<br>
Lukasz Malucha











