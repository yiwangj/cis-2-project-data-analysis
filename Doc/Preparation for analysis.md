# Introduction
In the data extraction and data analysis before we first open the hdf5 file, and understand the data structure stored in the hdf5. At the same time, because each laminectomy case contains many hdf5 files (each break in data entry will generate a file), so before analyzing the data we need to merge these data into one file

# How to use
use read hdf5.py open hdf5 file, the output file structure and the size of the matrix corresponding to each data
use merge.py to merge all hdf5 together under one laminectomy case


## Structure of hdf5
### 1st layer keys: 
 <KeysViewHDF5 ['burr_change', 'data', 'drill_force_feedback', 'metadata', 'voxels_removed']>
### 2nd layer keys: 
burr_change 
 layer contains <KeysViewHDF5 []>
data 
 layer contains <KeysViewHDF5 ['depth', 'l_img', 'pose_main_camera', 'pose_mastoidectomy_drill', 'pose_mastoidectomy_volume', 'r_img', 'segm', 'time']>
drill_force_feedback 
 layer contains <KeysViewHDF5 ['time_stamp', 'wrench']>
metadata 
 layer contains <KeysViewHDF5 ['README', 'baseline', 'camera_extrinsic', 'camera_intrinsic', 'voxel_volume']>
voxels_removed 
 layer contains <KeysViewHDF5 ['voxel_color', 'voxel_removed', 'voxel_time_stamp']>
### 3nd layer values: 
<HDF5 dataset "depth": shape (500, 480, 640), type "<f8">
<HDF5 dataset "l_img": shape (500, 480, 640, 3), type "|u1">
<HDF5 dataset "pose_main_camera": shape (500, 7), type "<f8">
<HDF5 dataset "pose_mastoidectomy_drill": shape (500, 7), type "<f8">
<HDF5 dataset "pose_mastoidectomy_volume": shape (500, 7), type "<f8">
<HDF5 dataset "r_img": shape (500, 480, 640, 3), type "|u1">
<HDF5 dataset "segm": shape (500, 480, 640, 3), type "|u1">
<HDF5 dataset "time": shape (500,), type "<f8">
<HDF5 dataset "time_stamp": shape (103503,), type "<f8">
<HDF5 dataset "wrench": shape (104158, 6), type "<f8">
<HDF5 dataset "README": shape (), type "|O">
<HDF5 dataset "baseline": shape (), type "<f8">
<HDF5 dataset "camera_extrinsic": shape (4, 4), type "<i8">
<HDF5 dataset "camera_intrinsic": shape (3, 3), type "<f8">
<HDF5 dataset "voxel_volume": shape (), type "<f8">
<HDF5 dataset "voxel_color": shape (20547, 5), type "<f8">
<HDF5 dataset "voxel_removed": shape (20547, 4), type "<f8">
<HDF5 dataset "voxel_time_stamp": shape (8498,), type "<f8">

