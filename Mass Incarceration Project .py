#!/usr/bin/env python
# coding: utf-8

# In[234]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[235]:


def read_and_preprocess(file_name, columns_to_drop, crucial_na_columns):
 df = pd.read_csv(file_name)
 df.dropna(subset = crucial_na_columns, inplace=True)
 df = df.drop(columns=columns_to_drop)
 return df


# In[236]:


data = pd.read_csv("incarceration_data.csv")
plt.figure(figsize=(18,10))
plt.title("Global Prison Populations")

place= ['U.S.','INDIA','CHINA','INDONESIA','PAKISTAN','NIGERIA','BRAZIL','BANGLADESH','RUSSIA','MEXICO',
        'THAILAND','TURKEY','IRAN','PHILIPPINES']
prispop= [2121600/1000, 466084/1000, 1710000/1000, 230755/1000, 77275/1000, 62781/1000, 
          755274/1000, 88084/1000, 501476/1000, 198384/1000, 376499/1000, 
          286000/1000, 240000/1000, 215000/1000]

plt.bar(place, prispop)
plt.xlabel("COUNTRY")
plt.ylabel("PRISONS POPULATIONS (in thousands)")


# In[237]:


data = pd.read_excel("race_ethnicity_gender_2010.xlsx", sheet_name= "Total")
plt.figure(figsize=(10,5))
plt.title("Adult Incarceration in the U.S. Based on Race and Ethnicity (2010)")
race= ['WHITE','BLACK','NATIVE AMERICAN','ASAIN','PACIFIC ISLANDER','OTHER']
number = [1139749/1000,897875/1000,37854/1000,16928/1000,5494/1000,142908/1000]
plt.bar(race, number)
plt.xlabel("RACE/EHTNICITY")
plt.ylabel("PRISON POPULATION (in thounsands)")


# In[238]:


data = pd.read_csv("incarceration_data.csv")
plt.figure(figsize=(18,10))
plt.title("Global Populations")

place= ['U.S.','INDIA','CHINA','INDONESIA','PAKISTAN','NIGERIA','BRAZIL','BANGLADESH','RUSSIA','MEXICO',
        'THAILAND','TURKEY','IRAN','PHILIPPINES']
totalpop= [329893959/10000, 1380159707/10000, 1439404024/10000, 273547739/10000, 
           220920226/10000, 206158244/10000, 212578788/10000, 164708057/10000, 
           145934462/10000, 128944098/10000, 69802624/10000, 84346550/10000, 83992949/10000, 109595187/10000]

plt.bar(place, totalpop) 
plt.xlabel("COUNTRY")
plt.ylabel("POPULATIONS (in millions)")


# In[239]:


data = pd.read_csv("raceper100000.csv")
plt.figure(figsize=(10,5))
plt.title("Rate of Incarceration in the U.S. Based on Race and Ethnicity (2010)")
raceS= ['WHITE','BLACK','NATIVE AMERICAN','ASAIN','PACIFIC ISLANDER','OTHER']
numberS = [450, 2306, 1291, 115, 1017, 831]
plt.bar(raceS, numberS)
plt.xlabel("RACE/EHTNICITY")
plt.ylabel("RATE INCARCERATED (in thounsands)")


# In[ ]:





# In[ ]:




