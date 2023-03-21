import networkx as nx
import random
import matplotlib.pyplot as plt

def full_random_walk(n,p,t):
    G = nx.Graph()
    G.add_nodes_from(list(range(n)))
    for i in range(n):
        for j in range(n):
            if i != j:
                if random.random() < p:
                    G.add_edge(i,j)
    steps=[]
    for i in range(t):
        #performing random walk on biggest component of the graph
        s = set()
        current_node = random.choice(list(sorted(nx.connected_components(G), key=len, reverse=True)[0]))
        step = 1
        s.add(current_node)
        while len(s) < len(sorted(nx.connected_components(G), key=len, reverse=True)[0]):
            current_node = random.choice(list(G.neighbors(current_node)))
            step += 1
            s.add(current_node)
        steps.append(step)
    return sum(steps)/len(steps)

def plot_steps_vs_p(n,t):
    steps = []
    p=0
    while(p<1):
        p += 0.01
        steps.append(full_random_walk(n,p,t))
    plt.plot(steps)
    plt.show()