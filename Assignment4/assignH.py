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
#Finding airlines that make the minimum number of cancellations.


alldoc = database.flights.aggregate([{'$group' : {'_id':"$AIRLINE", 'MIN CANCELLED COUNT':{'$sum':"$CANCELLED"}}},{'$sort':{"MIN CANCELLED COUNT":1}},{'$limit': 1}])
for item in alldoc:
  print(item)
 #Finding airlines that make the maximum number of cancellations.
alldoc2 = database.flights.aggregate([{'$group' : {'_id':"$AIRLINE", 'MAX CANCELLED COUNT':{'$sum':"$CANCELLED"}}},{'$sort':{"MAX CANCELLED COUNT":-1}},{'$limit': 1}])
for item in alldoc2:
  print(item)
