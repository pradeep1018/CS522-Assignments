import networkx as nx
import matplotlib.pyplot as plt

def select_edge_to_remove(G):
    dict1 = nx.edge_betweenness_centrality(G)
    dict1 = sorted(dict1.items(), key=lambda kv:(kv[1], kv[0]))
    print('The edge removed is ', dict1[-1][0])
    return dict1[-1][0]

def girvan_newman(G):
    l = nx.number_connected_components(G)
    while(l==1):
        G.remove_edge(*select_edge_to_remove(G))
        l = nx.number_connected_components(G)
    return [G.subgraph(c).copy() for c in nx.connected_components(G)]

print('Barbell Graph\n')    

G1 = nx.barbell_graph(6, 0)
nx.draw(G1, with_labels=True)
plt.show()

c1 = girvan_newman(G1)
nx.draw(G1, with_labels=True)
plt.show()

print('\n')

for i in c1:
    print(i.nodes)

print('\n')

print('Karate Club Graph\n')

G2 = nx.karate_club_graph()
nx.draw(G2, with_labels=True)
plt.show()

c2 = girvan_newman(G2)
nx.draw(G2, with_labels=True)
plt.show()

print('\n')

for i in c2:
    print(i.nodes)

