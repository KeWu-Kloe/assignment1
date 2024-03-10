#!/usr/bin/env python
# coding: utf-8

# In[67]:


import networkx as nx
import pandas as pd
import numpy as np

#read local data
def loadnetwork(file_path, isdirectedGraph=False):
    if isdirectedGraph:
        Graph = nx.DiGraph()
    else:  Graph = nx.Graph()
    with open(file_path,'r') as data:
        for n in data:
            node =n.strip().split()
            Graph.add_edge(int(node[0]), int(node[1]))
    return Graph
GraphA = loadnetwork('Desktop/data/worm.txt')  
print(GraphA)
GraphB = loadnetwork('Desktop/data/email-Eu-core.txt') 
print(GraphB )

#method that is used to calculate all values
def generate_table(Graph):
    table = {}
    table['number_of_nodes'] = Graph.number_of_nodes()
    table['number_of_edges'] = Graph.number_of_edges()
    degree_list = [i for _, i in Graph.degree()]
    table['average_degree'] = np.mean(degree_list)
    table['average_clustering_coefficient'] = nx.average_clustering(Graph)
    table['transitivity'] = nx.transitivity(Graph)
    table['maxi_degree'] = np.max(degree_list)
    table['min_degree'] = np.min(degree_list)
    if nx.is_connected(Graph):
        table['diameter'] = nx.diameter(Graph)
        table['radius'] = nx.radius(Graph)
    else:
        table['diameter'] = None 
        table['radius'] = None 
    table['maxi_closeness_centrality'] = np.max(list(nx.closeness_centrality(Graph).values()))
    table['maxi_betweenness_centrality'] = np.max(list(nx.betweenness_centrality(Graph).values()))
    return table
# A
tableA =generate_table(GraphA)

#B
tableB= generate_table(GraphB)
print(tableA)
print(tableB)

df_metrics = pd.DataFrame([compute_metrics(GraphA)])


# In[51]:


Nodes_of_A =tableA['number_of_nodes']
average_degree_of_A = tableA['average_degree']
GraphC = nx.erdos_renyi_graph(Nodes_of_A, average_degree_of_A /(Nodes_of_A-1))
Nodes_of_B =tableB['number_of_nodes']
average_degree_of_B = tableB['average_degree']
GraphD= nx.erdos_renyi_graph(Nodes_of_B, average_degree_of_B/ (Nodes_of_B-1))

m = int(average_degree_of_A) if average_degree_of_A%2 ==0 else int(average_degree_of_A)- 1 
GraphE = nx.watts_strogatz_graph(Nodes_of_A, m, 0.1)
#C
tableC =generate_table(GraphC)
#D
tableD= generate_table(GraphD)
#E
tableE= generate_table(GraphE)
print(tableC)
print(tableD)
print(tableE)


# In[64]:


# small world property
# Modify graph B
# average_clustering_coefficient is higher than the output of table B
n = int(average_degree_of_B) if average_degree_of_B%2 ==0 else int(average_degree_of_B)- 1 
GraphG = nx.watts_strogatz_graph(Nodes_of_B,n, 0.1)
tableG =generate_table(GraphG)
print(tableG)



# In[ ]:




