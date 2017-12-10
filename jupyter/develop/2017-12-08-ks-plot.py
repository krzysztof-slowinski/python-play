
# coding: utf-8

# In[1]:


import pandas as pd

pd.read_csv('olympics.csv')


# In[2]:


get_ipython().magic('matplotlib notebook')

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 20)
line = plt.plot(x, np.sin(x), '--', linewidth=2)

