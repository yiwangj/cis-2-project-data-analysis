#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import numpy.linalg as la

from mergehdf5 import DataMerger
import matplotlib.pyplot as plt

data_merger = DataMerger()
files = []
files.append(['C_P0_L3_color', '/Users/wangyi/Downloads/Source_Data/cxoxe_P0_L3_color/2023-04-13 10:51:15'])
files.append(['K_P0_L3_color', '/Users/wangyi/Downloads/Source_Data/klobo_P0_L3_color/2023-04-06 10:24:32'])
files.append(['P_P0_L3_color', '/Users/wangyi/Downloads/Source_Data/pexvxk_P0_L3_color/2023-04-06 09:34:53'])
files.append(['T_P0_L3_color', '/Users/wangyi/Downloads/Source_Data/tbpq_P0_L3_color/2023-04-06 11:12:43'])


files.append(['C_P2_L2_color', '/Users/wangyi/Downloads/Source_Data/cxoxe_P2_L2_color/2023-04-13 10:38:13'])
files.append(['K_P2_L2_color', '/Users/wangyi/Downloads/Source_Data/klobo_P2_L2_color/2023-04-06 10:11:54'])
files.append(['P_P2_L2_color', '/Users/wangyi/Downloads/Source_Data/klobo_P2_L2_color/2023-04-06 10:11:54'])
files.append(['T_P2_L2_color', '/Users/wangyi/Downloads/Source_Data/tbpq_P2_L2_color/2023-04-06 11:34:55'])



files.append(['C_P4_L2_color', '/Users/wangyi/Downloads/Source_Data/cxoxe_P4_L2_color/2023-04-13 10:08:49'])
files.append(['K_P4_L2_color', '/Users/wangyi/Downloads/Source_Data/klobo_P4_L2_color/2023-04-06 10:08:32'])
files.append(['P_P4_L2_color', '/Users/wangyi/Downloads/Source_Data/pexvxk_P4_L2_color/2023-04-06 09:18:08'])
files.append(['T_P4_L2_color', '/Users/wangyi/Downloads/Source_Data/tbpq_P4_L2_color/2023-04-06 11:44:29'])

files.append(['C_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/cxoxe_P7_L1_color/2023-04-13 10:48:22'])
files.append(['K_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/klobo_P7_L1_color/2023-04-06 10:05:35'])
files.append(['P_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/pexvxk_P7_L1_color/2023-04-06 09:03:13'])
files.append(['T_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/tbpq_P7_L1_color/2023-04-06 10:58:37'])

files.append(['C_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/cxoxe_P7_L1_color/2023-04-13 10:48:22'])
files.append(['K_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/klobo_P7_L1_color/2023-04-06 10:05:35'])
files.append(['P_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/pexvxk_P7_L1_color/2023-04-06 09:03:13'])
files.append(['T_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/tbpq_P7_L1_color/2023-04-06 10:58:37'])


mags = []
avg=[]

import pandas as pd

my_list = []
for lab, fl in files:
    data = data_merger.get_merged_data(fl)
    force_data = data['drill_force_feedback']['wrench'][:, :3]
    m = np.zeros([force_data.shape[0]])
    for i, force_data in enumerate(force_data):
        m[i] = la.norm(force_data)
    average = sum(m) / len(m)    
    mags.append(average)
    
    
    
for i in range(0, len(mags), 4):
    mean = sum(mags[i:i+4])/4
    avg.append(mean)
    
    


    
    
    
    
    
    
    
    


# In[10]:


data_merger = DataMerger()
files = []
files.append(['C_P1_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/cxoxe_P1_L1_no_color/2023-04-13 10:44:15'])
files.append(['K_P1_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/klobo_P1_L1_no_color/2023-04-06 10:21:48'])
files.append(['P_P1_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/pexvxk_P1_L1_no_color_v2/2023-04-06 08:52:32'])
files.append(['T_P1_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/tbpq_P1_L1_no_color/2023-04-06 11:26:28'])

files.append(['C_P1_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/cxoxe_P1_L3_no_color/2023-04-13 10:32:25'])
files.append(['K_P1_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/klobo_P1_L3_no_color/2023-04-06 09:59:55'])
files.append(['P_P1_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/pexvxk_P1_L3_no_color/2023-04-06 09:14:06'])
files.append(['T_P1_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/tbpq_P1_L3_no_color/2023-04-06 11:39:26'])

files.append(['C_P2_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/cxoxe_P2_L1_no_color/2023-04-13 10:23:43'])
files.append(['K_P2_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/klobo_P2_L1_no_color/2023-04-06 10:17:49'])
files.append(['P_P2_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/pexvxk_P2_L1_no_color/2023-04-06 09:22:09'])
files.append(['T_P2_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/tbpq_P2_L1_no_color/2023-04-06 11:07:07'])

files.append(['C_P4_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/cxoxe_P4_L1_no_color/2023-04-13 10:19:26'])
files.append(['K_P4_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/klobo_P4_L1_no_color/2023-04-06 09:53:16'])
files.append(['P_P4_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/pexvxk_P4_L1_no_color/2023-04-06 08:57:24'])
files.append(['T_P4_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/tbpq_P4_L1_no_color/2023-04-06 11:18:42'])

files.append(['C_P7_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/cxoxe_P7_L3_no_color/2023-04-13 10:28:22'])
files.append(['K_P7_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/klobo_P7_L3_no_color/2023-04-06 10:15:10'])
files.append(['P_P7_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/pexvxk_P7_L3_no_color/2023-04-06 09:31:26'])
files.append(['T_P7_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/tbpq_P7_L3_no_color/2023-04-06 11:31:01'])

mags_non = []
avg_non=[]

import pandas as pd

my_list = []
for lab, fl in files:
    data = data_merger.get_merged_data(fl)
    force_data = data['drill_force_feedback']['wrench'][:, :3]
    m = np.zeros([force_data.shape[0]])
    for i, force_data in enumerate(force_data):
        m[i] = la.norm(force_data)
    average = sum(m) / len(m)    
    mags_non.append(average)
    
    
    
for i in range(0, len(mags_non), 4):
    mean = sum(mags_non[i:i+4])/4
    avg_non.append(mean)
    


# In[11]:


data = [avg, avg_non]

fig, ax = plt.subplots()

# Creating axes instance
bp = ax.boxplot(data)

# Adding labels to x-axis
ax.set_xticklabels(['color', 'non_color'])

# Adding title to the plot
plt.title('Force Magnitude(N)')

# Displaying the plot
plt.show()


# In[ ]:




