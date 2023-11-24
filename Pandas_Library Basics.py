#!/usr/bin/env python
# coding: utf-8

# In[3]:


#PANDAS LIBRARY IS MOSTLY USED FOR SERIES AND DATAFRAME DATASTRUCTURE. 
import pandas as pd
#Series Example
series1=pd.Series([10,20,'apple',5.2,7.999995])
print(series1)


# In[4]:


print(type(series1))


# In[7]:


#inorder to give different serial number or index other than 1,2,3
series1=pd.Series([10,20,'apple',5.2,7.999995], index=['a','b','c','d','e'])
print(series1)


# In[13]:


#Another way to give different index in pandas series
series2=pd.Series({'april':4,'may':5,"june":6})
print(series2)
#Accessing a single element in series
print(series2['april'])
#Applying condition on series
print(series2[series2>4])


# In[18]:


#Data_Frame use cases of pandas(just looks like Excel spreadsheet)
import pandas as pd
import numpy as np
array1=np.array([[1,2,3,4],[5,6,7,8]])
dataframe1=pd.DataFrame(array1)
print(dataframe1)
dataframe1
#Access the 3rd column
dataframe1[3]
#Access the column's serial number and details only
dataframe1.columns


# In[25]:


#Change the name of the index of the dataframe
dataframe1=pd.DataFrame(array1,columns=['one','two','three','four'])
print(dataframe1)


# In[26]:


dataframe1['three']


# In[16]:


#Python dataframe conversion and drop
import numpy as np
import pandas as pd
ser1=pd.Series(np.random.randn(5),index=['one','two','three','four','five'])
ser1
#conversion to df
ser1.to_frame()
ser2=pd.Series(np.random.randn(5),index=['one','two','three','four','five'])
ser2.to_frame()

#join 2 series to single data frame
dataframe11=pd.concat([ser1,ser2],axis=1).reset_index()
print(dataframe11)


# In[21]:


dataframe11.iloc[1][1]


# In[27]:


#Reconstructing by using reshape function
dataframe12=pd.DataFrame(np.random.randn(25).reshape(5,5),index=['one','two','three','four','five'],columns=['1st','2nd','3rd','4th','5th'])
dataframe12


# In[28]:


#Drop any row
dataframe12.drop('two')


# In[31]:


#Drop any column
dataframe12.drop('2nd',axis=1)


# In[34]:


#the following command permanantely deletes the column or row specified
dataframe12.drop('3rd',axis=1,inplace=True)


# In[35]:


dataframe12


# In[36]:


#Summary of dataframe and selection
dataframe13=pd.DataFrame(np.random.randn(25).reshape(5,5),index=['one','two','three','four','five'],columns=['1st','2nd','3rd','4th','5th'])
dataframe13


# In[37]:


dataframe13.describe()


# In[40]:


dataframe13.transpose().describe()


# In[41]:


dataframe13.sum()


# In[42]:


dataframe13.sum(axis=1) #every row sum


# In[45]:


dataframe13.cumsum()


# In[47]:


#get index of maximum and minimum value
dataframe13.idxmax()
dataframe13.idxmin()


# In[5]:


import pandas as pd
#Create a dataframe from dictionary and select element
Popularity={"character":['Naruto','Goku','Luffy','Sasuke','Vegeta','Zoro'],'popularity':["First","Second","Third","Fourth","Fifth","Sixth"],"score":[99,95,94,93,92,91]}
#Now convert the dictionary to dataframe
dataframe14=pd.DataFrame(Popularity,index=['A',"B","C","D","E","F"])
dataframe14


# In[13]:


#Accessing elements
dataframe14.iloc[3][2]


# In[21]:


#Accessing Out of the way
dataframe14.loc['C']['character']
dataframe14.at['C','character']
dataframe14.iat[2,0]


# In[20]:


#accessing range of rows
dataframe14[1:3]


# In[23]:


#Missing data management and Sorting in Pandas
import pandas as pd
import numpy as np
popularity={"Exam1":[50,47,44,53,42],
            "Exam2":[60,57,46,59,47],
            "Exam3":[80,77,65,72,63],
            "Exam4":[81,83,75,79,87]}
dataframe15=pd.DataFrame(popularity,index=["School A","School B","School C","School D","School E"])
dataframe15


# In[32]:


dataframe16 = dataframe15[dataframe15<70]
print(dataframe16)


# In[28]:


#How to remove the missing number in dataframe16
dataframe16.dropna()


# In[29]:


dataframe16.dropna(axis=1)
#It will remove all the column with missing value


# In[30]:


dataframe16.dropna(axis=1,how='all')
#This method will remove the column where every value is missing


# In[33]:


dataframe16.dropna(axis=1,how='any')
#This method will remove the column where even a single value is missing


# In[47]:


dataframe16.dropna(axis=1,thresh=2)

#the above line implies if the data frame has atleast 2 non missing value then only it can retained other wise it will be dropped from the data frame


# In[48]:


dataframe16


# In[51]:


#In the above cell as we saw no change is applied to datafram 16 so
#inorder to make actual change we have to use attribur Inpalce =true
dataframe16.dropna(axis=1,thresh=2,inplace=True)


# In[52]:


#Now when we print the same dataframe the changes will be stored and visible
dataframe16


# In[69]:


#Sort Methods in dataFrame
dataframe15.sort_values("Exam1")
#by default exam 1 column is sorted in ascending order


# # 

# In[68]:


dataframe15.sort_values("School A",axis=1)
#by default School A row is sorted in ascending order


# In[70]:


#Sort in different order
dataframe15.sort_values("School A",axis=1,ascending=False)


# In[11]:


#Pandas Hierarchial-Multi Indexing
import pandas as pd
import numpy as np
#Indexing means representing multiple data values in a particular field.
#Create a dataframe from dictionary and select element
Popularity={"character":['Naruto','Naruto','Luffy','Luffy','Sasuke','Sasuke','Vegeta','Vegeta','Zoro','Zoro','Goku','Goku'],
            'popularity':['First',"Second","Third","Fourth","Fifth","Sixth",'First',"Second","Third","Fourth","Fifth","Sixth"],
            "score1":[57,46,59,47,60,57,46,59,47,99,100,101],
             "score2":[57,46,59,47,60,57,46,59,47,99,100,101]}

dataframe17=pd.DataFrame(Popularity)
dataframe17
dataframe17.set_index(["character","popularity"],drop=False)


# In[ ]:




