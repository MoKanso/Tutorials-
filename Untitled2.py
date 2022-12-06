#!/usr/bin/env python
# coding: utf-8

# In[56]:


import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt

import networkx as nx


# In[57]:


G=nx.Graph()


# In[58]:


G


# In[59]:


positions=nx.spring_layout(G)
G


# In[60]:


nx.draw(G,pos=positions)
nx.draw_networkx_labels(G,pos=positions)
plt.draw() 


# In[ ]:





# In[61]:


coauthorshipG=nx.read_graphml("netScience.graphml")


# In[62]:


import networkx as nx
G = nx.Graph()


# In[63]:


G.add_node(1)


# In[64]:


G.add_nodes_from([2, 3])


# In[65]:


G.add_nodes_from([
    (4, {"color": "red"}),
    (5, {"color": "green"}),
])


# In[66]:


G


# In[67]:


H = nx.path_graph(10)
G.add_nodes_from(H)


# In[68]:


G.add_node(H)


# In[69]:


nx.Graph()


# In[70]:


G = nx.path_graph(4)
print(nx.is_connected(G))


# In[72]:


G = nx.path_graph(4)
print(nx.is_biconnected(G))


# In[73]:


G.add_edge(0, 3)
print(nx.is_biconnected(G))


# In[91]:


message = input('Enter a number') #encrypted message

for key in range(len(message)):
   translated = ''
   for symbol in message:
      if symbol in message:
         num = message.find(symbol)
         num = num - key
         if num < 0:
            num = num + len(message)
         translated = translated + message[num]
      else:
         translated = translated + symbol
print('Hacking key #%s: %s' % (key, translated))


# In[92]:


G = nx.complete_graph(message)
nx.draw(G)


# In[94]:


G = nx.complete_graph(42)
nx.draw(G)


# In[95]:


G1=nx.from_numpy_matrix(interactions_characters)


# In[97]:


nx.draw_networkx(G1)


# In[98]:


H1    = nx.relabel_nodes(G1, character_map)


# In[99]:


nx.draw_networkx(H1, node_color=range(numCharacters),font_color='black',width=0.3,alpha=0.7, 
                 font_size=10, cmap=matplotlib.cm.GnBu
                 ,node_size =[40*val for (node,val) in kdeg])


# In[ ]:




