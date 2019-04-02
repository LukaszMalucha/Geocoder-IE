import os
import csv
from pymongo import MongoClient


## Set up DB Connection
mongo_uri = os.environ.get("MONGO_URI")
mongo_db = os.environ.get("MONGO_DBNAME")

client = MongoClient(mongo_uri)
db = client[mongo_db]
geocodes = db["geocodes"]


## Read CSV  file
csvfile = open('localities_full.csv', 'r')
reader = csv.DictReader( csvfile )
header= [ "X","Y","county","townland"]


## Upload to DB
for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    geocodes.insert_one(row)

