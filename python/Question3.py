#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Read and view, View the dataset shape
import pandas as pd 
# read text file into pandas DataFrame
df = pd.read_csv("faa_ai_prelim.csv")
  
# display DataFrame
print(df)
display(df.shape)


# In[9]:


#D>> print(df.columns)

print(df.columns)


# In[12]:


#E>> read specific columns of csv file using Pandas
df = pd.read_csv("faa_ai_prelim.csv", usecols = ['ACFT_MAKE_NAME', 'LOC_STATE_NAME', 'ACFT_MODEL_NAME', 'RMK_TEXT', 'FLT_PHASE', 'EVENT_TYPE_DESC', 'FATAL_FLAG'])
print(df)


# In[14]:


#F>> count of missing values in each column
df = pd.read_csv("faa_ai_prelim.csv")
df.isnull().sum()


# In[21]:


#G>> Clean the dataset and replace the fatal flag NaN with “No”
df = pd.read_csv("faa_ai_prelim.csv", usecols = [ 'FATAL_FLAG'])
df['FATAL_FLAG'].fillna('',inplace=True)

print(df)


# In[27]:


#G,H>>Clean the dataset and replace the fatal flag NaN with “No”

df = pd.read_csv("faa_ai_prelim.csv", usecols = [ 'FATAL_FLAG'])
#df = df.dropna()
df['FATAL_FLAG'] = df['FATAL_FLAG'].fillna("NO")
print(df)


# In[43]:


#df = pd.read_csv("faa_ai_prelim.csv")
#df['ACFT_MAKE_NAME'].dropna()
# Method 1 - Filter dataframe
#df = df[df['ACFT_MAKE_NAME'] == 0]
# Method 2 - Using the drop() function
#df.drop(df.index[df['ACFT_MAKE_NAME'] == 0], inplace=True)
#print(df)

df.drop(df.loc[df['ACFT_MAKE_NAME']== ""].index, inplace=True)
print(df)


# In[46]:


#I>>Remove all the observations where aircraft names (ACFT_MAKE_NAME) are not available

df.drop(df[df['ACFT_MAKE_NAME'] == ""].index, inplace=True)
print(df)


# In[47]:


#J>>Find the aircraft types and their occurrences in the dataset

df.groupby(['ACFT_MODEL_NAME']).size()


# In[57]:


#K>>Display the observations where fatal flag is “Yes”.
#df.query('FATAL_FLAG' == 'Yes')
df.query('FATAL_FLAG == "Yes"')
     


# In[74]:


#I>>Show the accidents with fatality.

df = pd.read_csv("faa_ai_prelim.csv", usecols = [ 'EVENT_TYPE_DESC', 'FATAL_FLAG'])
print(df)

#rslt_df = df[(df['EVENT_TYPE_DESC'] == 'Accident') & 
          #df['FATAL_FLAG'].isin(options)] 

#df[(df['EVENT_TYPE_DESC']=='Accident')  
  
   
 


# In[ ]:





# In[ ]:




