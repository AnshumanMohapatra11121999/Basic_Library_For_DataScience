#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
a1=np.array([1,2,3,4,5])
print(a1)


# In[5]:


a1=np.arange(10)
print(a1)


# In[6]:


a2=a1.reshape(2,5)
print(a2)
print(a2.shape)
print(a2.dtype.name)
print(a2.ndim)


# In[7]:


#List to numpy array
months=['jan','feb','mar','apr']
month_arr=np.array(months)
print(month_arr)


# In[8]:


import numpy as np

# Nested list
mo = ['jan', 'feb', 'mar', 'apr', ['sep', 'aug', 'Nov']]

# Create a NumPy array
#As numpy allows arrays of same datatype,we converted the list inside list and every other data to the type object from string and list.
mont = np.array(mo, dtype=object)

# Print the array
print(mont)



# In[9]:


#zero,unity and identity array
array2=np.zeros(100)
array2=array2.reshape(10,10)
print(array2)

array2=np.ones(100)
array2=array2.reshape(10,10)
print(array2)

array3=np.eye(6)
array3=array3.reshape(6,6)
print(array3)


# In[10]:


#Empty and full array(we can fill the array with any element we want)
arr=np.empty((3,2))
print(arr)

arrf=np.full((3,3),'x')
print(arrf)


# In[18]:


#Numpy multi dimensional array
import numpy as npp
ar1=npp.arange(100)
print(ar1)
#Reshape to 2d array
ar1=ar1.reshape(5,20)
print(ar1)

#Accessing a special element in a 2d array
print(ar1[3,5])
print(ar1[3][5])
#Both of the above statement will accesssame element..


# In[22]:


#Reshape the array into a 3d array
ar1=ar1.reshape(5,4,5)
print(ar1)
#Accessing element in 3D Array
print(ar1[3,2])
print(ar1[3,2,4])



# In[24]:


#Array operation
arr1=np.arange(100)
arr1.reshape(5,4,5)
arr2=np.arange(100)
arr2.reshape(5,4,5)
#addition
arr3=np.add(arr1,arr2)
print(arr3)
#subtraction
arr4=np.subtract(arr1,arr2)
print(arr4)
#multiplication
arr5=np.multiply(arr1,arr2)
print(arr5)
#minimum
arr6=np.minimum(arr1,arr2)
print(arr6)





# In[27]:


#Transpose_of_an_Array
#In transpose row converts to column and column converts to rows
arrx=np.arange(10)
print("The actual array is:",arrx)
arrx=arrx.reshape(5,2)
print("The reshaped array is:",arrx)
print("The transpose of the above array is:",arrx.transpose())


# In[36]:


#Mathematical/statistical operation on element of numpy array...
print("The sum of all the elements in the array is",arrx.sum())
print("The mean of all the elements in the array is",arrx.mean())
print("The variance of all the elements in the array is",arrx.var())
print("The standard deviation of all the elements in the array is",arrx.std())
#applying a condition on elements on numpy array to change it to another element
arry=np.where(arrx<5,0,arrx)#this means where the element of array arrx is less than five return 0 else return the same value
print("After apply the above condition the new numpy array is",arry)


# In[ ]:




