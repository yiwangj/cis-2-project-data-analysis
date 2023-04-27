#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np
import numpy.linalg as la

from mergehdf5 import DataMerger
import matplotlib.pyplot as plt

data_merger = DataMerger()
files = []
files.append(['C_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/cxoxe_P7_L1_color/2023-04-13 10:48:22'])
files.append(['K_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/klobo_P7_L1_color/2023-04-06 10:05:35'])
files.append(['P_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/pexvxk_P7_L1_color/2023-04-06 09:03:13'])
files.append(['T_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/tbpq_P7_L1_color/2023-04-06 10:58:37'])


mags = []


import pandas as pd

my_list = []
for lab, fl in files:
    data = data_merger.get_merged_data(fl)
    voxel_time_stamp1 = data['voxels_removed']['voxel_time_stamp'][()] 
    df = pd.DataFrame(voxel_time_stamp1)
    start_time1 = voxel_time_stamp1[0]
    end_time1 = voxel_time_stamp1[-1] 
    total_time1 = end_time1 - start_time1

    my_list.append(total_time1)
    print(my_list)
    
    


















# In[17]:


P0_L1_color =[208.7133800983429, 135.62777972221375, 179.78176403045654, 111.06691122055054]
P0_L3_color =[176.0993115901947, 99.61482524871826, 188.2633171081543, 227.80447912216187]
P2_L2_color=[318.3990969657898, 100.72965598106384, 100.72965598106384, 209.26376914978027]
P4_L2_color=[311.51833939552307, 133.87119722366333, 172.95134735107422, 179.59322476387024]
P7_L1_color=[127.9039978981018, 119.80234909057617, 199.87805271148682, 402.4983067512512]
mean_color=[]
mean1 = sum(P0_L1_color) / len(P0_L1_color)
mean_color.append(mean1)
mean2 = sum(P0_L3_color) / len(P0_L3_color)
mean_color.append(mean2)
mean3 = sum(P2_L2_color) / len(P2_L2_color)
mean_color.append(mean3)
mean4 = sum(P4_L2_color) / len(P4_L2_color)
mean_color.append(mean4)
mean5 = sum(P7_L1_color) / len(P7_L1_color)
mean_color.append(mean5)
print(mean_color)


# In[18]:


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

mags = []


import pandas as pd

my_list = []
for lab, fl in files:
    data = data_merger.get_merged_data(fl)
    voxel_time_stamp1 = data['voxels_removed']['voxel_time_stamp'][()] 
    df = pd.DataFrame(voxel_time_stamp1)
    start_time1 = voxel_time_stamp1[0]
    end_time1 = voxel_time_stamp1[-1] 
    total_time1 = end_time1 - start_time1

    my_list.append(total_time1)
    print(my_list)
    


# In[20]:


lists = [140.2928466796875, 112.80537939071655, 142.16640090942383, 223.26786708831787, 280.6443614959717, 199.2194118499756, 160.4031503200531, 167.27761912345886, 166.06362199783325, 108.67385268211365, 170.69138360023499, 248.9096176624298, 178.2396388053894, 99.13160490989685, 252.64483904838562, 262.7026698589325, 172.5461709499359, 101.58276963233948, 116.51613211631775, 160.02915811538696]
for i in range(0, len(lists), 4):
    mean = sum(lists[i:i+4])/4
    print(mean)


# In[22]:


mean_nocolor=[154.63312351703644, 201.8861356973648 ,173.58461898565292 ,198.1796881556511 ,137.66855770349503]


# In[23]:


data = [mean_color, mean_nocolor]

fig, ax = plt.subplots()

# Creating axes instance
bp = ax.boxplot(data)

# Adding labels to x-axis
ax.set_xticklabels(['color', 'non_color'])

# Adding title to the plot
plt.title('voxel_remove_time')

# Displaying the plot
plt.show()


# In[ ]:




