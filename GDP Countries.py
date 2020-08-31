#!/usr/bin/env python
# coding: utf-8

# In[52]:


import pandas as pd

data = pd.read_fwf('https://raw.githubusercontent.com/qureshiaa/GDP-Countries/master/Countries%20with%20GDP.txt')


# In[53]:


data


# In[54]:


data = pd.DataFrame(data)


# In[55]:


data2 = data.drop(data.index[1])


# In[56]:


data2


# In[57]:


data3 = data2.T


# In[58]:


data3.info()


# In[59]:


data3.columns = ['Countries', 'GDP Numbers']
data3


# In[60]:


data3['GDP Numbers'].value_counts()


# In[61]:


#data3['Countries'] = data3['Countries'].str.replace("'", '')


# In[62]:


data3


# In[63]:


import numpy as np

countries = np.array(['Algeria','Angola','Argentina','Australia','Austria','Bahamas','Bangladesh',
                     'Belarus','Belgium','Bhutan','Brazil','Bulgaria','Cambodia','Cameroon','Chile','China',
                     'Colombia','Cyprus','Denmark','El Salvador','Estonia','Ethiopia','Fiji','Finland','France',
                     'Georgia','Ghana','Grenada','Guinea','Haiti','Honduras','Hungary','India','Indonesia','Ireland',
                     'Italy','Japan','Kenya', 'South Korea','Liberia','Malaysia','Mexico', 'Morocco','Nepal','New Zealand',
                     'Norway','Pakistan', 'Peru','Qatar','Russia','Singapore','South Africa','Spain','Sweden',
                     'Switzerland','Thailand', 'United Arab Emirates',
                     'United Kingdom','United States','Uruguay','Venezuela','Vietnam','Zimbabwe'])

gdp_numbers = np.array([2255.225482,629.9553062,11601.63022,25306.82494,27266.40335,19466.99052,
                        588.3691778,2890.345675,24733.62696,1445.760002,4803.398244,2618.876037,
                        590.4521124,665.7982328,7122.938458,2639.54156,3362.4656,15378.16704,30860.12808,
                        2579.115607,6525.541272,229.6769525,2242.689259,27570.4852,23016.84778,1334.646773,
                        402.6953275,6047.200797,394.1156638,385.5793827,1414.072488,5745.981529,837.7464011,
                        1206.991065,27715.52837,18937.24998,39578.07441,478.2194906,16684.21278,279.2204061,
                        5345.213415,6288.25324,1908.304416,274.8728621,14646.42094,40034.85063,672.1547506,
                        3359.517402,36152.66676,3054.727742,33529.83052,3825.093781,15428.32098,33630.24604,
                        39170.41371,2699.123242,21058.43643,28272.40661,37691.02733,9581.05659,5671.912202,
                        757.4009286,347.7456605])


# In[64]:


max_gdp = gdp_numbers.argmax()
max_gdp


# In[65]:


country_with_max_gdp = countries[max_gdp]
country_with_max_gdp


# In[66]:


min_gdp = gdp_numbers.argmin()
min_gdp


# In[67]:


country_with_min_gdp = countries[min_gdp]
country_with_min_gdp


# In[68]:


mean_gdp_numbers = gdp_numbers.mean()
mean_gdp_numbers


# In[69]:


sum_gdp_numbers = gdp_numbers.sum()
sum_gdp_numbers


# In[70]:


std_gdp_numbers = gdp_numbers.std()
std_gdp_numbers


# In[71]:


together = np.concatenate([countries,gdp_numbers])
together


# In[72]:


for numbers in gdp_numbers:
    gdp_numbers_new = numbers
    print (gdp_numbers_new)


# In[73]:


for i in range(len(countries)):
    country = countries[i]
    country_gdp = gdp_numbers[i]
    print(i + 1,country,'is',country_gdp)

