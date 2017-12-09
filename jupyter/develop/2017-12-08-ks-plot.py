
# coding: utf-8

# In[2]:


get_ipython().magic('matplotlib notebook')

import matplotlib.pyplot as plt
import numpy as np


# In[3]:


x = np.linspace(-10, 10)
line = plt.plot(x, np.sin(x), '--', linewidth=2)

