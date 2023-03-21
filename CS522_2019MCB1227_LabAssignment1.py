import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

def create_graph(n):
  G = nx.Graph()
  G.add_nodes_from(range(n))
  return G

# 0 denotes negative edge
# 1 denotes positive edge
def add_edges_with_weights(G):
  for i in range(G.number_of_nodes()):
    for j in range(i+1, G.number_of_nodes()):
        G.add_edge(i,j,weight=random.choice(list(range(2))))
  return G

def get_triangles(G):
    triangles = []
    for i in range(G.number_of_nodes()):
        for j in range(i+1, G.number_of_nodes()):
            for k in range(j+1, G.number_of_nodes()):
                triangles.append([i, j, k])
    return triangles

def get_triangle_edge_weights(G, triangles):
    triangle_edge_weights = []
    for triangle in triangles:
        e1 = G[triangle[0]][triangle[1]]['weight']
        e2 = G[triangle[1]][triangle[2]]['weight']
        e3 = G[triangle[2]][triangle[0]]['weight']
        triangle_edge_weights.append([e1, e2, e3])
    return triangle_edge_weights

def count_unstable_triangles(triangle_edge_weights):
    count = 0
    for inst in triangle_edge_weights:
        if sum(inst)%2 == 0:
            count += 1
    return count

def check_stability(triangle_edge_weights):
    for inst in triangle_edge_weights:
        if sum(inst)%2 == 0:
            return False
    return True


def make_triangle_stable(G, triangles, triangle_edge_weights):
    unstable_triangle_idx = -1
    for i in range(len(triangles)):
        if sum(triangle_edge_weights[i])%2 == 0:
            unstable_triangle_idx = i
            break

    if unstable_triangle_idx==-1:
        return G, triangle_edge_weights

    edge_choice = random.choice(list(range(3)))

    if triangle_edge_weights[unstable_triangle_idx][edge_choice] == 0:
        G[triangles[unstable_triangle_idx][(edge_choice)%3]][triangles[unstable_triangle_idx][(edge_choice+1)%3]]['weight'] = 1
    
    else:
        G[triangles[unstable_triangle_idx][(edge_choice)%3]][triangles[unstable_triangle_idx][(edge_choice+1)%3]]['weight'] = 0

    return G

def balanced_state_time_analysis(n):
    itrs = []
    for _ in range(20):
        G = create_graph(n)
        G = add_edges_with_weights(G)
        triangles = get_triangles(G)
        triangle_edge_weights = get_triangle_edge_weights(G, triangles)

        itr = 0
        n_unstable_triangles = []
        n_unstable_triangles.append(count_unstable_triangles(triangle_edge_weights))
        while(check_stability(triangle_edge_weights)==False):
            itr += 1
            G = make_triangle_stable(G, triangles, triangle_edge_weights)
            triangle_edge_weights = get_triangle_edge_weights(G, triangles)
            n_unstable_triangles.append(count_unstable_triangles(triangle_edge_weights))
        itrs.append(itr)
    plt.plot(itrs)
    plt.ylabel('Number of Iterations')
    plt.show()

def unstable_triangles_analysis(n):
    G = create_graph(n)
    G = add_edges_with_weights(G)
    triangles = get_triangles(G)
    triangle_edge_weights = get_triangle_edge_weights(G, triangles)

    itr = 0
    n_unstable_triangles = []
    n_unstable_triangles.append(count_unstable_triangles(triangle_edge_weights))
    while(check_stability(triangle_edge_weights)==False):
        itr += 1
        G = make_triangle_stable(G, triangles, triangle_edge_weights)
        triangle_edge_weights = get_triangle_edge_weights(G, triangles)
        n_unstable_triangles.append(count_unstable_triangles(triangle_edge_weights))
    plt.plot(n_unstable_triangles)
    plt.ylabel('Number of Unstable Triangles')
    plt.xlabel('Time')
    plt.show()

#balanced_state_time_analysis(10)
#unstable_triangles_analysis(10)