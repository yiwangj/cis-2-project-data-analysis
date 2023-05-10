#!/usr/bin/env python
# coding: utf-8

# In[47]:


from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import h5py
import numpy as np

from mergehdf51 import DataMerger

params = {
    "legend.fontsize": "x-large",
    "figure.figsize": (9, 5),
    "axes.labelsize": "large",
    "axes.titlesize": "x-large",
    "xtick.labelsize": "medium",
    "ytick.labelsize": "medium",
}

plt.rcParams.update(params)

def rgb_to_hex(r, g, b,alpha):
    alpha_new=(alpha / 255).round(2)
    if alpha_new==0.1 or alpha_new==0.2:
        r=255
        g=0
        b=0
    elif alpha_new == 0.3:
        r = 255
        g = 255
        b = 0
    elif alpha_new == 1:
        r = 0
        g = 255
        b = 0 
    return '#%02x%02x%02x' % (int(r), int(g), int(b))
    

files = []
file.append(['name','https://github.com/yiwangj/cis-2-project-data-analysis/tree/main/Data%20Set')
#files.append(['C_P2_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/tbpq_P4_L1_no_color/2023-04-06 11:18:42'])





data_merger = DataMerger()
count=0


for lab, f in files:
    data = data_merger.get_merged_data(f, False)
    count=count+1
    vrm = data['voxels_removed']['voxel_removed'][()]
    vcol = data['voxels_removed']['voxel_color'][()]
    
    colors = [None for _ in range(vcol.shape[0])]

    for i, c in enumerate(vcol):
        colors[i] = rgb_to_hex(c[1], c[2], c[3],c[4])
        #colors[i] = rgb_to_hex(c[1], c[2], c[3])
         
    
    #colors=colors[:len(colors)//2]
    
    print(len(colors))
    #vrm=vrm[:len(vrm)//2,:]
    print(len(vrm))
    #fig, axs = plt.subplots(2, 1)
    #fig, axs = plt.subplots(4, 2, figsize=(10, 20))
    #fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')
    fig = plt.figure()
    axs = [fig.add_subplot(2, 2, i+1, projection='3d') for i in range(4)]


# set the completion percentages
    pct_complete = [25, 50, 75, 100]
    #ax.scatter(vrm[:, 0], vrm[:, 1], vrm[:, 2], alpha=.3, c=colors)
    for i, ax in enumerate(axs):
    # set the completion time for this subplot
        idx = int(pct_complete[i] / 100 * len(vrm))
        print(idx)
    # create a scatter plot for the non-navigated case
        ax.scatter(vrm[:idx, 1], vrm[:idx, 2], vrm[:idx, 3], c=colors[:idx])
        #.scatter(vrm[:idx, 0], vrm[:idx, 1], vrm[:idx, 2], c=colors[:idx])
    

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
    # plt.legend(["Dura", "Tegmen"])
        plt.title('Removed Voxels  '+ lab)
    plt.tight_layout()

    plt.show()


# In[ ]:




# In[ ]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# create some random 3D data
x = np.random.normal(size=100)
y = np.random.normal(size=100)
z = np.random.normal(size=100)

# set up a list of hex codes to represent colors
colors_hex = ['#FF0000', '#00FF00'] * 50

# set up a grid of subplots with 2 rows and 2 columns
fig = plt.figure(figsize=(12, 12))
axs = [fig.add_subplot(2, 2, i+1, projection='3d') for i in range(4)]

# set the completion percentages
pct_complete = [25, 50, 75, 100]

# create a scatter plot for each completion percentage
for i, ax in enumerate(axs):
    # subset the data based on the completion percentage
    idx = int(pct_complete[i] / 100 * len(x))
    x_sub = x[:idx]
    y_sub = y[:idx]
    z_sub = z[:idx]
    colors_sub = colors_hex[:idx]

    # create the scatter plot with colored points
    ax.scatter(x_sub, y_sub, z_sub, c=colors_sub)

    # set the axis labels and title
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title(f'Completion: {pct_complete[i]}%')

# adjust the layout of the subplots and show the plot
fig.tight_layout()
plt.show()


# In[ ]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# create some random 3D data
x = np.random.normal(size=100)
y = np.random.normal(size=100)
z = np.random.normal(size=100)
colors = ['r' if xi < 0 else 'g' for xi in x]  # set colors based on x values

# set up a grid of subplots with 2 rows and 2 columns
fig = plt.figure(figsize=(12, 12))
axs = [fig.add_subplot(2, 2, i+1, projection='3d') for i in range(4)]

# set the completion percentages
pct_complete = [25, 50, 75, 100]

# create a scatter plot for each completion percentage
for i, ax in enumerate(axs):
    # subset the data based on the completion percentage
    idx = int(pct_complete[i] / 100 * len(x))
    x_sub = x[:idx]
    y_sub = y[:idx]
    z_sub = z[:idx]
    colors_sub = colors[:idx]

    # create the scatter plot with colored points
    ax.scatter(x_sub, y_sub, z_sub, c=colors_sub)

    # set the axis labels and title
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title(f'Completion: {pct_complete[i]}%')

# adjust the layout of the subplots and show the plot
fig.tight_layout()
plt.show()


# In[ ]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# create some data
x = np.random.normal(size=100)
y = np.random.normal(size=100)
z = np.random.normal(size=100)
colors = ['r' if xi < 0 else 'g' for xi in x]  # set colors based on x values

# create a grid of subplots with 4 rows and 2 columns
fig, axs = plt.subplots(4, 2, figsize=(10, 20))

# set up a loop to create each subplot
for i, ax in enumerate(axs.flat):
    # set the completion time for this subplot
    pct_complete = (i + 1) * 25

    # create a scatter plot for the non-navigated case
    ax.scatter(x[:pct_complete], y[:pct_complete], z[:pct_complete], c=colors[:pct_complete], marker='o')
    ax.set_title(f'Non-navigated, {pct_complete}% complete')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    # create a scatter plot for the navigated case
    ax = axs.flat[i+1]
    ax.scatter(x[:pct_complete], y[:pct_complete], z[:pct_complete], c=colors[:pct_complete], marker='o')
    ax.set_title(f'Navigated, {pct_complete}% complete')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

# adjust the layout of the subplots
plt.tight_layout()

# show the plot
plt.show()

