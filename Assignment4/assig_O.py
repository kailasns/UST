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
alldoc1234 = database.flights.aggregate( 
            [
                #{'$group': { "_id": { 'DAY_OF_WEEK': "$DAY_OF_WEEK" } } }
                {'$group': {'_id':"$DAY_OF_WEEK", 'AVG_ARRIVAL_DELAY':{'$avg':"$ARRIVAL_DELAY"}}}, {'$sort':{'AVG_ARRIVAL_DELAY':-1}},{'$limit':1}
            ]
            
        )

for item in alldoc1234:
  print(item)