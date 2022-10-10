def count(string):
 str1 = string.split()
 str2 = []
 dict1= {}


 for i in str1:
     if i not in str2:
      str2.append(i)


 for i in range (0,len(str2)):
     dict1.update({str2[i]:str1.count(str2[i])})
 return dict1



print(count(str1))
  
