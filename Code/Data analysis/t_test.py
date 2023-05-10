#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from scipy.stats import ttest_ind
import numpy as np

# generate two samples of scores
 # mean 7, standard deviation 1, 50 samples

# perform t-test on the two samples
t_statistic, p_value = ttest_ind(mags, mags_non)

# print the results
print("t-statistic:", t_statistic)
print("p-value:", p_value)

