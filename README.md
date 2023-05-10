# Introduction
This is the repository for the CIS II project:Virtual Reality Simulator for Laminectomy ( data analysis part)
The repository is created and maintained by:

- Yi Wang, M.S.E. in Robotics, Johns Hopkins Unversity

## How to use
The code file contains five sub-files, the GUI contains all the code to create a GUI system, the Data Extraction contains the code needed to extract the corresponding data from hdf5 and store it in a csv file, the Data analysis contains the code needed to calculate the drilling time, drilling Data analysis contains the code needed to calculate drilling time, drilling force, voxel-removed. merge.py is used to merge hdf5 files, can be more convenient for data operations. readhdf5.py shows how to open the hdf5 file and view its structure. 

IMG file contains five images, the first image shows a progression of non-navigated and navigated cases with respect to the types of voxels removed (both being colored) and both with about the same progression (i.e. at 25%, 50%, 75%, and 100% completion times respectively).The third image shows the status of participants' force use in the navigated and non-navigated cases, and the fourth shows the number of voxels (bad area) removed in red. The fifth picture shows the situation of drilling time 


# Installation

This repo is developed and tested on MacOSX and ubuntu 20.04.

Before you start install this repo, please refer to https://jupyter.org/ to install the necessary dependencies

Clone the repo to the local folder

```bash
git clone https://github.com/yiwangj/cis-2-project-data-analysis.git
```

Enter the workspace

```bash
cd cis-2-project-data-analysis
```

Install the necessary dependencies

```bash
pip install ...
```



# User Guide

Fetch the data and copy it to `Data Set` directory.

In the workspace directory, run the following code to get the visualization reuslt

```bash
python -m xxxxxxxxx
```

Or the visualization can be obtained through Jupyter Notebook. In your IDE, xxxx



