#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


#Read and write csv file
dataframe1=pd.read_csv('iris_dataset.csv')
dataframe1


# In[4]:


dataframe1.head()


# In[5]:


#if separator between data is space instead of comma and you need first 10 data rows
dataframe1=pd.read_csv('iris_dataset.csv',header=None,sep=',',nrows=10)
dataframe1


# In[6]:


print(dataframe1[5:])


# In[7]:


#Writing in  CSV File 
Popularity={"character":['Naruto','Naruto','Luffy','Luffy','Sasuke','Sasuke','Vegeta','Vegeta','Zoro','Zoro','Goku','Goku'],
            'popularity':['First',"Second","Third","Fourth","Fifth","Sixth",'First',"Second","Third","Fourth","Fifth","Sixth"],
            "score1":[57,46,59,47,60,57,46,59,47,99,100,101],
             "score2":[57,46,59,47,60,57,46,59,47,99,100,101]}
dataframe2=pd.DataFrame(Popularity)
dataframe2.to_csv('popularity.csv')


# In[8]:


#Change the separator to space from comma
dataframe2.to_csv('popularityspaceseparatedvalue.csv',sep=" ")


# In[9]:


#Remove index from the data
dataframe2.to_csv('popularityindexremovedvalue.csv',index=False)


# In[ ]:


#Pandas JSON FILE READ AND WRITE OPERATION
#JSON MEANS JAVA SCRIPT OBJECT NOTATION
#In Json file values are in key value pair separated by comma nad every row is enclosed in a curly bracket similar to dictionary in python
dataframejson=pd.read_json("file.json")
dataframejson
#all other features are same for dataframe after conversion from json



# In[10]:


#write to json file
Popularity={"character":['Naruto','Naruto','Luffy','Luffy','Sasuke','Sasuke','Vegeta','Vegeta','Zoro','Zoro','Goku','Goku'],
            'popularity':['First',"Second","Third","Fourth","Fifth","Sixth",'First',"Second","Third","Fourth","Fifth","Sixth"],
            "score1":[57,46,59,47,60,57,46,59,47,99,100,101],
             "score2":[57,46,59,47,60,57,46,59,47,99,100,101]}
dataframe3=pd.DataFrame(Popularity)
dataframe3.to_json('popularity.json')


# In[ ]:




