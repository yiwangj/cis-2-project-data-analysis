# Data Extraction
Extract relevant data from hdf5 and generate csv file
# How to use
## force data extraction
Calculate the average force value of each stroke according to each stroke, and after averaging all the strokes in a Laminectomy case, get the average force value of each case. 10 cases (5 color/5 noncolor) of 11 participants are calculated in this way, and stored into csv file according to name and case name

## voxel time extraction
According to the first time stamp and the last time stamp recorded in hdf5 to calculate the drilling time required for each case, a total of 110 times for 11 participants will be stored in a csv file according to the names of the participants and the cases

## voxel removed data
After traversing all the voxels recorded under each case, we can find out the color of the voxel according to the value of alpha, and after traversing all the voxels, we can find out how many voxels are in green/red/yellow in one case, and enter the name of the case into the csv file according to the name of the participant, totaling 330 groups of data.
