# Lab exam 2
# Code wrriten by Pradeep

# Page Rank

import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

A = np.array([[1, 2], [3, 4]]) # 2*2 matrix A

m = np.array([[0, 0, 0, 1/2, 1/2, 1, 1, 1],
        [1/2, 0, 0, 0, 0, 0, 0, 0],
        [1/2, 0, 0, 0, 0, 0, 0, 0],
        [0, 1/2, 0, 0, 0, 0, 0, 0],
        [0, 1/2, 0, 0, 0, 0, 0, 0],
        [0, 0, 1/2, 0, 0, 0, 0, 0],
        [0, 0, 1/2, 0, 0, 0, 0, 0],
        [0, 0, 0, 1/2, 1/2, 0, 0, 0]]) # adjacency matrix of the graph
    
def q1():
    v = np.array([[1], [1]]) # 2*1 vector v
    v = v/np.linalg.norm(v,2) # normalize vector v
    error = 1
    epsilon = 0.0001
    while error>epsilon:
        v_new = np.matmul(A,v)
        v_new = v_new/np.linalg.norm(v_new,2)
        error = abs(v_new[0][0]-v[0][0]) + abs(v_new[1][0]-v[1][0])
        v = v_new
    print('The vector v converges to ',v)

def q2():
    eigenvalue, eigenvector = np.linalg.eig(A)  
    print('Eigenvalues: ',eigenvalue)
    print('Eigenvetor: ',eigenvector)  

def q3():
    v = np.array([[1], [1], [1], [1], [1], [1], [1], [1]])
    v = v/np.linalg.norm(v,2) 
    error = 1
    epsilon = 0.0001
    while error>epsilon:
        v_new = np.matmul(m,v)
        v_new = v_new/np.linalg.norm(v_new,2)
        error = np.mean(np.absolute(v-v_new))
        v = v_new
    print('Values at the respective nodes are in this proportion: ',np.squeeze(v))

def q4():
    G = nx.DiGraph()
    G.add_nodes_from([0,1,2,3,4,5,6,7])
    G.add_edges_from([(0,1),(0,2)])
    G.add_edges_from([(1,3),(1,4)])
    G.add_edges_from([(2,5),(2,6)])
    G.add_edges_from([(3,0),(3,7)])
    G.add_edges_from([(4,0),(4,7)])
    G.add_edges_from([(5,0)])
    G.add_edges_from([(6,0)])
    G.add_edges_from([(7,0)])

    step = 0
    vis = [0 ,0 ,0, 0, 0, 0, 0, 0]
    current_node = 0
    while step < 100000:
        vis[current_node] += 1
        current_node = random.choice(list(G.neighbors(current_node)))
        step += 1

    node_list = ['A','B','C','D','E','F','G','H']
    plt.plot(node_list, vis)
    plt.title('Visit Distribution when random walk is applied')
    plt.show()

def q6():
    eigenvalue, eigenvector = np.linalg.eig(m)  
    print('Principal eigenvector is ',eigenvector[:,np.argmax(eigenvalue)])  
