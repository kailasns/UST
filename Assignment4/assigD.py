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
   # collection.insert_many(data)
#alldoc = collection.find({'MONTH':2},{'_id':0,'MONTH':1, 'DAY':1,'CANCELLED':1}).sort("CANCELLED", -1)

#for item in alldoc:
  #print("hello",item)
import pandas as pd
# importing matplotlib library
import matplotlib.pyplot as plt
df = pd.DataFrame(list(database.flights.find()))
#print(df)


#for item in alldoc:
  #print("hello",item)

alldoc2 = database.flights.aggregate([{'$group': {'_id':"$DAY_OF_WEEK", 'avg_val':{'$avg':"$ARRIVAL_DELAY"}}}])
alldoclist = []
alldoclist = [database.flights.aggregate([{'$group': {'_id':"$DAY_OF_WEEK", 'avg_val':{'$avg':"$ARRIVAL_DELAY"}}}])]

#for item in alldoc2:
 # print("hello",item)

#Plotting
#df2 = pandas.read_sql("SELECT * FROM flights, engine)
scores =[]
for score in list(database.flights.aggregate( 
            [
                #{'$group': { "_id": { 'DAY_OF_WEEK': "$DAY_OF_WEEK" } } }
                {'$group': {'_id':"$DAY_OF_WEEK", 'AVG_ARRIVAL_DELAY':{'$avg':"$ARRIVAL_DELAY"}}}
            ]
        )):
    scores.append(score)

    print(scores)

scores_data = pd.DataFrame(scores, index=None)
print(scores_data)
scores_data.plot(kind = 'bar', x = 0, y = 1)

plt.show() 



