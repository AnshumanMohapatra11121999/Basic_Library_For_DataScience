#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
#formore we can check official documentation of pandas merge,join,and concatenate


# In[3]:


#Concatenation of DataFrames
df1=pd.DataFrame({'A':['A0','A1','A2','A3'],
                 'B':['B0','B1','B2','B3'],
                 'C':['C0','C1','C2','C3'],
                 'D':['D0','D1','D2','D3']},
                 index=[0,1,2,3])
df2=pd.DataFrame({'A':['A4','A5','A6','A7'],
                 'B':['B4','B5','B6','B7'],
                 'C':['C4','C5','C6','C7'],
                 'D':['D4','D5','D6','D7']},
                 index=[4,5,6,7])
df3=pd.DataFrame({'A':['A8','A9','A10','A11'],
                 'B':['B8','B9','B10','B11'],
                 'C':['C8','C9','C10','C11'],
                 'D':['D8','D9','D10','D11']},
                 index=[8,9,10,11])

Result1 = pd.concat([df1,df2,df3])#Normal Concatenation
Result1 = pd.concat([df1,df2,df3],axis=1)#Column wise concatenation
Result1


# In[7]:


#Merging of DataFrames
left=pd.DataFrame({
    'key':['K0','K1','K2','K3'],
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3']
})
right=pd.DataFrame({
    'key':['K0','K1','K2','K3'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3']})
resultmerge=pd.merge(left,right,on='key')
print(resultmerge)


# In[3]:


#Joining 2 DataFrames where there is uncommon columns are present in 2 data frames
import pandas as pd

left = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2', ]
}, index=['K0', 'K1', 'K2'])

right = pd.DataFrame({
    'C': ['C0', 'C2', 'C3'],
    'D': ['D0', 'D2', 'D3']
}, index=['K0', 'K2', 'K3'])

print(left)
print(right)
resultl=left.join(right)
#result2=right.join(left)
resultl



# In[5]:


#Pandas Stacking and pivoting of dataframe
#Stacking:Means arranging dataframe in row index or column index
Popularity={"character":['Naruto','Naruto','Luffy','Luffy','Sasuke','Sasuke','Vegeta','Vegeta','Zoro','Zoro','Goku','Goku'],
            'popularity':['First',"Second","Third","Fourth","Fifth","Sixth",'First',"Second","Third","Fourth","Fifth","Sixth"],
            "score1":[57,46,59,47,60,57,46,59,47,99,100,101],
             "score2":[57,46,59,47,60,57,46,59,47,99,100,101]}
dataframest=pd.DataFrame(Popularity)
dataframest





#pivoting:


# In[6]:


dataframest.stack()


# In[8]:


#unstack the dataframe
dataframeunst=dataframest.unstack()
dataframeunst


# In[9]:


dataframest=dataframeunst.unstack(0)
dataframest


# In[12]:


#Pivoting:means 
dataframest.pivot_table(index=['character','popularity'],aggfunc="first")


# In[14]:


dataframest.pivot_table(index=['character','popularity'],aggfunc="count")


# In[ ]:




