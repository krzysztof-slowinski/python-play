
# coding: utf-8

# In[1]:


get_ipython().magic('matplotlib notebook')

import matplotlib.pyplot as plt
import numpy as np


# In[4]:


x = np.linspace(0, 10)
line = plt.plot(x, np.sin(x), '--', linewidth=2)

