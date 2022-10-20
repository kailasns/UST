import matplotlib.pyplot as plt

file = open("test.txt", "r")   
test_str = file.read()  
all_freq = {}
  
for i in test_str:

    if (i in all_freq) and (i.isalpha()):
     
        all_freq[i] += 1
    elif (i not in all_freq) and (i.isalpha()):
        all_freq[i] = 1
  
# printing result 
print ("Count of all characters in GeeksforGeeks is :\n "
                                        +  str(all_freq))

keysList = list(all_freq.keys())
valueList = list(all_freq.values())
#print(valueList)

plt.bar(keysList, valueList)
plt.title('Letter Vs Frequency')
plt.xlabel('keysList')
plt.ylabel('valueList')
plt.show()
