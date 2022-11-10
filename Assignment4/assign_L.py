#K,Calculating mean and standard deviation of departure delay for all flights in minutes
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



alldoc = database.flights.aggregate([{'$group': {'_id':"$FLIGHT_NUMBER", 'stdDev':{'$stdDevPop':"$DEPARTURE_DELAY"}, 'Mean':{'$avg':"$DEPARTURE_DELAY"}}},{'$limit': 5}])
#for item in alldoc:
  #print(item)

#[Create a suitable plot using matplotlib/seaborn]
scores =[]
for score in list(database.flights.aggregate( 
            [
                #{'$group': { "_id": { 'DAY_OF_WEEK': "$DAY_OF_WEEK" } } }
               {'$group': {'_id':"$FLIGHT_NUMBER", 'stdDev':{'$stdDevPop':"$ARRIVAL_DELAY"}, 'Mean':{'$avg':"$ARRIVAL_DELAY"}}},{'$limit': 5}
            ]
        )):
    scores.append(score)

    #print(scores)

scores_data = pd.DataFrame(scores, index=None)
print(scores_data)
scores_data.plot(kind = 'bar', x = 0, y = 1)

#plt.show() 

