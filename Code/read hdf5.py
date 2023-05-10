#!/usr/bin/env python
# coding: utf-8

# In[5]:


import h5py


# In[6]:


f = h5py.File('20221109_185044.hdf5', 'r')


# In[7]:


f.keys() 


# In[ ]:


with h5py.File(FILE_NAME, "r") as f:
  data = f['land-names\land-06'][...]
  print(data)


# In[8]:


def readh5(h5_path: str):
    '''Read the h5 file
    Params:
    -------
    h5_path: str
        path to the h5 file
    Returns:
    --------
        None 
      
    '''
    with h5py.File(h5_path, 'r') as f:
        # List all groups
        print("Keys: %s" % f.keys())

        key_list = list(f.keys())

        print(key_list[1])
        data = f['proj-001']
        # data = [0,1]

        print()

    return data


# In[ ]:




