#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Read data from csv files
df_voxel = pd.read_csv('voxel_removed.csv')
df_color = pd.read_csv('data_color.csv')
df_color = df_color.drop_duplicates()
df_voxel = df_voxel.drop_duplicates()
df_voxel = df_voxel.rename(columns={
    '0': 'Stamp',
    '1': 'X',
    '2': 'Y',
    '3': 'Z'
})
df_color = df_color.rename(columns={
    '0': 'Stamp',
    '1': 'R',
    '2': 'G',
    '3': 'B',
    '4': 'Alpha'
})

# Count the number of rows for each 'Stamp' value in df_voxel
rows_per_stamp = df_voxel.groupby('Stamp').size()

# Group df_color by 'Stamp' and keep only the last n rows for each group, where n is the number of rows per 'Stamp' value in df_voxel
def keep_last_n_rows(group, n):
    return group.head(n)

df_color = df_color.groupby('Stamp').apply(lambda group: keep_last_n_rows(group, rows_per_stamp.get(group.name, 0))).reset_index(drop=True)

# Merge the two dataframes based on the 'Stamp' column
merged_df = pd.merge(df_voxel, df_color, on='Stamp', how='inner')

merged_df = merged_df.drop_duplicates()
merged_df['Alpha_warnings'] = (merged_df['Alpha'] / 255).round(2)

# Save the cleaned and merged data to a new CSV file
merged_df.to_csv('merged_data.csv', index=False)

# Load the cleaned and merged data from the CSV file
clean_data = pd.read_csv('merged_data.csv')

# Print the cleaned and merged data
print(clean_data)


# In[85]:


import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the data
data = pd.read_csv('merged_data.csv')

def update_rgb(row):
    new_alpha = row['Alpha_warnings']
    if new_alpha == 0.1 or new_alpha == 0.2:
        row['R'] = 255
        row['G'] = 0
        row['B'] = 0
    elif new_alpha == 0.3:
        row['R'] = 255
        row['G'] = 255
        row['B'] = 0
    elif new_alpha == 1:
        row['R'] = 0
        row['G'] = 255
        row['B'] = 0
    return row

merged_df = merged_df.apply(update_rgb, axis=1)
print(merged_df)
merged_df.to_csv('merged_data.csv', index=False)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the plot data
x = data['X']
y = data['Y']
z = data['Z']
r = data['R'] / 255
g = data['G'] / 255
b = data['B'] / 255
alpha = data['Alpha'] / 255
colors = [(r[i], g[i], b[i]) for i in range(len(r))]

# Plot the data with facecolors and edgecolors parameters
ax.scatter(x, y, z, facecolors=colors, edgecolors=colors)

# Set the plot labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Scatter Plot')
fig.savefig('scatter_plot.png')

# Show the plot
plt.show()
fig.savefig('scatter_plot.png')


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Load the data
data = pd.read_csv('merged_data.csv')

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the plot data
x = data['X']
y = data['Y']
z = data['Z']
r = data['R'] / 255
g = data['G'] / 255
b = data['B'] / 255
alpha = data['Alpha']/255
colors = [(r[i], g[i], b[i]) for i in range(len(r))]

# Set the plot labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Scatter Plot Animated')

# Initialize the scatter plot with empty data
sc = ax.scatter(x, y, z, c=colors)

# Define the function that will update the plot for each frame
def update(frame):
    stamp_data = data[data['Stamp'] <= frame]
    x = stamp_data['X']
    y = stamp_data['Y']
    z = stamp_data['Z']
    r = stamp_data['R'] / 255
    g = stamp_data['G'] / 255
    b = stamp_data['B'] / 255
    alpha = data['Alpha']/255
    colors = [(r[i], g[i], b[i]) for i in range(len(r))]
    
    # Update the offsets and colors
    sc._offsets3d = (x, y, z)
    sc.set_facecolors(colors)
    sc.set_edgecolors(colors)  # Also update edgecolors to avoid white edges

# Define the frames for the animation
unique_stamps = np.unique(data['Stamp'])
n_frames = len(unique_stamps)
frames = np.linspace(unique_stamps[0], unique_stamps[-1], n_frames).astype(int)

# Create the animation object
ani = FuncAnimation(fig, update, frames=frames, interval=2, blit=False)

# Save the animation as an mp4 file (optional)
ani.save('3d_scatter_animation_200_framesnew.mp4', writer='ffmpeg', fps=30)

# Show the plot
plt.show()


# In[ ]:




