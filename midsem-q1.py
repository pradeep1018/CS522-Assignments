import networkx as nx
import random

def preprocess_words(x):
    # splits by sentence
    x = x.split('.')
    
    # removes space
    y = []
    for i in x:
        y.append(i.split(' '))

    # removes \n
    k = []
    for i in y:
        l = []
        for j in i:
            l.extend(j.split('\n'))
        k.append(l)
    y = k

    # removes ,
    k = []
    for i in y:
        l = []
        for j in i:
            l.extend(j.split(','))
        k.append(l)
    y = k

    # removes ?
    k = []
    for i in y:
        l = []
        for j in i:
            l.extend(j.split('?'))
        k.append(l)
    y = k

    # removes empty strings
    k = []
    for i in y:
        l = []
        for j in i:
            if len(j) > 0:
                l.append(j.lower())
        if len(l) > 0:
            k.append(l)
    
    return k

def create_graph(filename):
    f = open(filename,"r",encoding="utf8")
    words = f.read()
    f.close()
    sentences = preprocess_words(words)
    G = nx.Graph()
    for sentence in sentences:
        for i, word in enumerate(sentence):
            G.add_node(word)
            for j in range(i+1,len(sentence)):
                G.add_edge(word, sentence[j])

    return G

def word_rank(G):
    # performs word rank on the largest component since there might be cases where a set of words are disconnected from the rest of the graph
    vis = {}
    current_node = random.choice(list(sorted(nx.connected_components(G), key=len, reverse=True)[0]))
    vis[current_node] = 0
    for i in range(100000):
        if (current_node in vis) == True:
            vis[current_node] += 1
        else:
            vis[current_node] = 0
        current_node = random.choice(list(G.neighbors(current_node)))
    l = []
    for x in vis:
        l.append([x, vis.get(x)])

    # algorithm to sort by value    
    for i in range(len(vis)):
        for j in range(i+1,len(vis)):
            if l[i][1] < l[j][1]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
    return l