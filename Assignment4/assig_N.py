import pymongo # importing the python-mongoDB connector library
from sqlalchemy import create_engine
connection_url = "mongodb://localhost:27017/" # This is the general link for connecting to the local device.

client = pymongo.MongoClient(connection_url) 
database=client["airline_delayDB3"]
collection=database["flights"] 
import csv
with open('C:\\Users\\ustpython22\\Downloads\\Flights_Delay.csv',"r") as file:
    reader = csv.DictReader(file)
    data = list(reader)
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame(list(database.flights.find()))

alldoc123 = database.flights.aggregate([
   { '$match':{ 'DIVERTED':1}},{'$group' : {'_id':{'Source':"$ORIGIN_AIRPORT", 'Destination':"$DESTINATION_AIRPORT"}, 'count':{'$sum':'$DIVERTED'}
        }},{'$limit': 10}, {'$sort':{'count':-1}}
])
for item in alldoc123:
  print(item)