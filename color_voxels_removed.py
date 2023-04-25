#!/usr/bin/env python
# coding: utf-8

# In[2]:


import h5py as h5
import numpy as np


# In[3]:


f = h5.File("20230406_095631.hdf5", "r")

print('# 1st layer keys: \n', f.keys())

print('# 2nd layer keys: ')
for key in f.keys():

    print(key, '\n layer contains',f[key].keys())

print('# 3nd layer values: ')
for key in f.keys():
    for key2 in f[key].keys():
        print(f[key][key2])
    


# Now I print all the content of this hdf5 file
# If you want to get access to a certain block, say if you want to get the value of metadata/README
# All the dataset in h5 are stored as a nested dictionary

# In[14]:


dataset = f['metadata']['README'][()].decode('utf-8') # decode bytes to string
print(dataset) # This will give you the README file


# To store all the values in a csv:

# In[18]:


import pandas as pd

df = pd.DataFrame()

# need to check the data type of the values in the h5 file
# but for now, I will just use the following (which is not correct)

for key in f.keys():
    for key2 in f[key].keys():
        df[key2] = f[key][key2][()]

print(df)


# In[4]:


base = f['metadata']['baseline'][()] 
print(base)


# In[5]:


import pandas as pd
data_base={'baseline': [base]}
df = pd.DataFrame(data_base)
print(df)
df.to_csv('baseline.csv', index=False)


# In[6]:


voxel_volume = f['metadata']['voxel_volume'][()] 
print(voxel_volume)


# In[7]:


import pandas as pd
data_voxel={'voxel_volume': [voxel_volume]}
df = pd.DataFrame(data_voxel)
print(df)
df.to_csv('data_voxel.csv', index=False)


# In[8]:


voxel_color= f['voxels_removed']['voxel_color'][()] # decode bytes to string
print(voxel_color) 


# In[9]:


import pandas as pd
df = pd.DataFrame(voxel_color)
print(df)
df.to_csv('data_color.csv', index=False)


# In[10]:


voxel_removed= f['voxels_removed']['voxel_removed'][()] # decode bytes to string
print(voxel_removed) # This will give you the README file


# In[11]:


df = pd.DataFrame(voxel_removed)
print(df)
df.to_csv('voxel_removed.csv', index=False)


# In[12]:


import csv
import pandas as pd
from collections import defaultdict



# Read the .csv files
df_color = pd.read_csv("data_color.csv")
df_voxel = pd.read_csv("voxel_removed.csv")

# Merge the dataframes on the 'index' (0) column
merged_df = pd.merge(df_color, df_voxel, on='0')

# Rename the columns of the merged dataframes
merged_df = merged_df.rename(columns={'0':'index', '1_x':'R', '2_x':'G', '3_x':'B', '4':'alpha',
                                      '1_y':'X', '2_y':'Y', '3_y':'Z'})

# Write the merged dataframe to a new CSV file
merged_df.to_csv('RGBvoxel.csv', index=False)

# Create RGB Voxel matching dictionary
rgb_voxel_dict = defaultdict(list)

# Loop through indexes and append voxel cooridnates with the same RGB value to dict
with open('RGBvoxel.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rgb = (float(row['R']), float(row['G']), float(row['B']))
        coord = (float(row['X']), float(row['Y']), float(row['Z']))
        rgb_voxel_dict[rgb].append(coord)

# Verify Dictionary
print(rgb_voxel_dict)


# In[ ]:




