#Find the busiest airports with respect to day of week. 
# Create a suitable plot using matplotlib/seaborn.


import pymongo # importing the python-mongoDB connector library
from sqlalchemy import create_engine
connection_url = "mongodb://localhost:27017/" # This is the general link for connecting to the local device.

client = pymongo.MongoClient(connection_url) 

database=client["airline_delayDB3"] #Connecting to existing Sales database or creating a new Sales database
collection=database["flights"] #connecting to the product collection in the Sales database
import csv
with open('C:\\Users\\ustpython22\\Downloads\\Flights_Delay.csv',"r") as file:
    reader = csv.DictReader(file)
    data = list(reader)
import pandas as pd
# importing matplotlib library
import matplotlib.pyplot as plt
df = pd.DataFrame(list(database.flights.find()))
#Find the busiest airports with respect to day of week. 
alldoc2 = database.flights.aggregate([{'$group': {'_id':"$DAY_OF_WEEK", 'avg_val':{'$avg':"$TAXI_OUT"}}}])
for item in alldoc2:
  print(item)

#[Create a suitable plot using matplotlib/seaborn]
scores =[]
for score in list(database.flights.aggregate( 
            [
                #{'$group': { "_id": { 'DAY_OF_WEEK': "$DAY_OF_WEEK" } } }
               #{'$group': {'_id':"$DAY", 'avg_val':{'$avg':"$ARRIVAL_DELAY"}}}
               {'$group': {'_id':"$DAY_OF_WEEK", 'Busy index':{'$avg':"$TAXI_OUT"}}}

            ]
        )):
    scores.append(score)

    print(scores)

scores_data = pd.DataFrame(scores, index=None)
print(scores_data)
scores_data.plot(kind = 'bar', x = 0, y = 1)

plt.show() 
