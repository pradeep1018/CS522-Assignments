# Name: Pradeep P
# Entry Number: 2019MCB1227
# Instructions: Just run this file. Number of nodes in the graph can be changed at the bottom of the file

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

def create_graph(n):
  G = nx.Graph()
  G.add_nodes_from(range(n))
  return G
  
def add_edges(G, p):
  for i in range(G.number_of_nodes()):
    for j in range(G.number_of_nodes()):
      if i!=j and random.random()<p:
        G.add_edge(i,j)
  return G
  
def num_connected_components(G):
  return nx.number_connected_components(G)
  
def length_shortest_path(G):
  return nx.average_shortest_path_length(G)
  
def time_random_walk(G):
  avg_itr = []
  for _ in range(100):
    v = set()
    current_node = random.choice(list(range(G.number_of_nodes())))
    i = 0
    while len(v) < G.number_of_nodes():
      v.add(current_node)
      i = i+1
      current_node = random.choice(list(G.neighbors(current_node)))
    avg_itr.append(i)
  return np.mean(avg_itr)
  
def highest_degree(G):
  highest_degree = 0
  for i in range(G.number_of_nodes()):
    highest_degree = max(highest_degree, G.degree[i])
  return highest_degree
  
def least_degree(G):
  lowest_degree = G.number_of_nodes()
  for i in range(G.number_of_nodes()):
    lowest_degree = min(lowest_degree, G.degree[i])
  return lowest_degree
  
def diameter_graph(G):
  return nx.diameter(G)
  
def prob_analysis(n):
  n_connected_components = []
  len_shortest_path = []
  t_random_walk = []
  highest_deg = []
  least_deg = []
  diameter = []
  prob = []
  prob_connected = []
  p = 0.01
  
  while p < 1:
    print(p) # to check progress
    G = create_graph(n)
    G = add_edges(G, p)
    prob.append(p)
    n_connected_components.append(num_connected_components(G))
    if num_connected_components(G) == 1:
      prob_connected.append(p)
      len_shortest_path.append(length_shortest_path(G))
      t_random_walk.append((time_random_walk(G)))
      diameter.append(diameter_graph(G))
    highest_deg.append(highest_degree(G))
    least_deg.append(least_degree(G))
    p += 0.05
  
  plt.plot(prob, n_connected_components)
  plt.title('Number of connected components')
  plt.show()

  plt.plot(prob_connected, len_shortest_path)
  plt.title('Average length of the shortest path')
  plt.show()

  plt.plot(prob_connected, t_random_walk)
  plt.title('Time taken for random walk')
  plt.show()

  plt.plot(prob, highest_deg)
  plt.title('Highest degree')
  plt.show()

  plt.plot(prob, least_deg)
  plt.title('Least degree')
  plt.show()

  plt.plot(prob_connected, diameter)
  plt.title('Diameter of the graph')
  plt.show()
  
prob_analysis(100) # number of nodes can be changed
