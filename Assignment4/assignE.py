import pymongo # importing the python-mongoDB connector library

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
#df = pd.DataFrame(data)
# plotting a bar graph
#xdoc = collection.find([{'MONTH':2},{'MONTH':1, '_id':0}])
xdoc = []
ydoc = []
xdoc = [collection.find({'MONTH':1},{'_id':0,'DAY':1}).sort("CANCELLED", -1)]
ydoc = [collection.find({'MONTH':1},{'_id':0,'CANCELLED':1})]
#for x in range(len(xdoc)):
   # print (xdoc[x])
#xdoc.values() == xdoc1

#xdoc1 = list(xdoc).values()
#ydoc1 = list(ydoc)

#for item in xdoc1:
  #print("hello",item)


#plt.scatter(xdoc, ydoc)
#plt.show()
ab = df.CANCELLED
abc = df.DAY
#print(abc)
#sorted_df=abc.sort_index()
#sorted = abc.sort_values(ab)
#print(sorted.head())
scores = []
scores1 = []

for score in list(collection.find({'MONTH':1},{'_id':0,'DAY':1}).sort("CANCELLED", -1)):
    scores.append(score)

    #print(scores)
scores_data = pd.DataFrame(scores, index=None)
print(scores_data)

for score1 in list(collection.find({'MONTH':1},{'_id':0,'CANCELLED':1})):
    scores1.append(score1)

    #print(scores)
scores_data1 = pd.DataFrame(scores1, index=None)
print(scores_data1)
plt.scatter(scores_data, scores_data1)
plt.show()
