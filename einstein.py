import random

def get_neighbours(node):
    """
    returns the neighbours of a particular node in which the neighbours have one 1 more than the node
    we are considering only the neighbours that have one 1 more than the node and 
    not the neighbours that have one 1 less than the node to avoid repetition 
    """

    neighbours = []

    for i in range(len(node)):
        """ if there is 0 at a particular index, then the node containing 1 at that index should be its neighbour """
        if node[i] == 0:
            node[i] = 1
            neighbours.append(node.copy())
            node[i] = 0

    return neighbours

def change_node(node):
    """
    changes the node by considering the list in binary form
    here the list is taken as reverse of a binary number
    for instance node = [1, 0, 0] represents 1 not 4
    this is done to simplify the operations 
    """

    i = 0
    while node[i] == 1:
        node[i] = 0
        i += 1
    node[i] = 1
    return node

def convert_to_number(l):
    """
    function to convert a list used for representing vertex into number form
    here the list is taken as reverse of a binary number
    for instance if l = [1, 0, 0], then it is converted to 1 not 4
    this is done to simplify the operations 
    """
    n = 0
    for i in range(len(l)):
        n += l[i]*(2**i)
    return n

def get_edge_list(G):
    """
    function to get edge list from a graph represented in tuple form
    """

    l_node = len(G[0][0])
    n_node = 2**l_node

    """ dictionary to store the neighbours of each edge"""
    G_ = dict()
    for i in range(n_node):
        G_[i] = []
    
    """ all the tuples are stored in the edge list after converting the lists into numbers """
    for edge in G:
        u = convert_to_number(edge[0])
        v = convert_to_number(edge[1])
        G_[u].append(v)
        G_[v].append(u)

    return G_

def find_node(l, n):
    """ function to find if vertex n is part of neighbours of another vertex represented as l"""

    for i in range(len(l)):
        if l[i]==n:
            return True
    return False

def convert_to_list(n, l_node):
    """
    the number representing the vertex is represented in a list by taking the reverse of its binary form
    """

    l = [0]*l_node
    for i in range(l_node):
        l[i] = n%2
        n  = int(n/2)
    return l

def dfs(G, u, vis):
    """
    function to perform dfs
    """

    vis[u] = 1
    for v in G[u]:
        """ only the vertices that are not already visited are visited again """
        if vis[v] == 0:
            dfs(G, v, vis)

def shortest_path(G, u, v, n_node):
    """
    function to find shortest path
    bfs is performed to find the shortest path between u and v
    """

    """ stores the path from vertex u to every vertex """
    paths = dict()
    for i in range(n_node):
        paths[i] = []

    queue = []
    vis = [0]*n_node
    queue.append(u)
    vis[u] = 1
    paths[u].append(u)

    """ loop runs until all the vertices are visited """
    while len(queue) > 0:

        """ this loop makes sure that the exploration happens level by level """
        for _ in range(len(queue)):

            """ front element of the queue is explored"""
            node = queue[0]
            queue.remove(node)
            for neighbour in G[node]:

                """ if a neighbour is not visited, it is added to the queue for exploration """
                if vis[neighbour] == 0:
                    queue.append(neighbour)
                    vis[neighbour] = 1
                    new_path = paths[node].copy()
                    new_path.append(neighbour)
                    paths[neighbour].extend(new_path)
                
    return paths[v]


def create_einstein_graph(n):
    """This should create what we are going to call - an Einstein Graph.
    Which will have 2**n nodes.
    Vertices should be of the form [0,0,0]...[1,1,1] if n=3. Two
    vertices are adjacent if they differ in exactly one position. For
    example, [1,0,1] and [1,0,0] are adjacent, but [1,0,1] and [0,1,1] are
    not adjacent. Note that if the input is n, you will have 2^n nodes and
    each node will have degree n. 

    This function should return the graph in the form of a list of tuples:
    [(a,b),(c,d),...] where a and b are adjacent. Note that we are not
    supposed to use networkx or any other api for graph theoretic analysis. 
    """

    graph = []

    """ 
    the variable node stores the vertex in the form of list of length n
    node initalized as [0, 0, ... , 0] 
    """ 
    node = n*[0]
    
    """ loop runs until node becomes [1, 1, ... , 1] """
    while sum(node) < n:
        """ neighbours has all the vertices which has one 1 more than node """
        neighbours = get_neighbours(node) 
        
        """ the node and its corresponding neighbours are appended as a tuple to the graph """
        for neighbour in neighbours:
            graph.append((node.copy(),neighbour.copy()))

        """ node is changed by taking the next number of current node when represented in binary form """
        node = change_node(node)
    return graph

def find_path_in_einsteingraph(G,u,v):
    """ Given an Einstein graph G in the list of tuples format as described in
    the above function create_einstein_graph, given two vertices u and v, we
    need to return the sequence of vertices [u,a1,a2,...,v] which represent the
    shortest path from u to v. Note that this is a very easy and straight
    forward."""

    """ stores the path from u to v """
    path = []
    """ 
    current node travels from u to v by progressively removing 
    all 1's which are not there in v at that index and then progressively adding 1's 
    at the index where 1 is present in v 
    """
    current_node = u
    path.append(current_node.copy())

    """ this loop converts all 1's in u which are 0 at the same index of v to 0 """
    for i in range(len(current_node)):
        if current_node[i] == 1 and v[i] == 0:
            current_node[i] = 0
            path.append(current_node.copy())

    """ this loop converts all 0's in current which are 1 at the same index of v to 1 """
    for i in range(len(current_node)):
        if current_node[i] == 0 and v[i] == 1:
            current_node[i] = 1
            path.append(current_node.copy())

    return path

def einstein_graph_create_smallworld(G,alpha):
    """We will create what is called the modified Einstein graph. This will consider 
    the input graph G, which is assumed to be an Einstein
    graph and remove alpha proportion of edges,uniformly at random. Note that, alpha is a number
    between 0 and 1. if alpha=0.5, it means you are removing half the edges. 

    After removing alpha proportion of edges, you need to add alpha proportion
    of edges back to the graph uniformly at random. In other words, you are
    misplacing a few edges and disturbing the otherwise regular structure of
    the graph (exactly the same way you generated the small world graphs in the
    course). Note that you can only add edges between nodes that do not have
    edges. Your program should take care of this. 

    You may want to note that, many things about the graph may change, for instance, the
    otherwise uniform degree is now disturbed, it is not easy to find a path
    between two nodes as before, if alpha is not small, this may disconnect the
    graph, in that case, you should repeat the experiment and return a
    resulting graph which is connected. You should write a check_connected function as
    given below.

    """
    
    """ length of the vertex list """
    l_node = len(G[0][0])

    """ number of vertices """
    n_node = 2**l_node

    l_graph = len(G)

    """ the modified graph after removing alpha proportion of edges """
    G_new = random.sample(G, int(l_graph*(1-alpha)))

    nodes_added = 0
    l_graph_new = len(G_new)

    """ representing the new graph in edge list form for efficiency """
    G_new_edge_list = get_edge_list(G_new)

    """ the loop runs until all the edges are added """
    while nodes_added < l_graph - l_graph_new:
        edge_nodes = random.sample(list(range(0,n_node)), 2)

        """ the randomly sampled nodes should be unequal and not present in the edge list """
        if edge_nodes[0] != edge_nodes[1] and find_node(G_new_edge_list[edge_nodes[0]], edge_nodes[1]) == False:
            G_new_edge_list[edge_nodes[0]].append(edge_nodes[1])
            G_new_edge_list[edge_nodes[1]].append(edge_nodes[0])
            nodes_added += 1

    """ the edge list is converted to tuple form after all the edges are added randomly """        
    G_new = []
    for i in range(len(G_new_edge_list)):
        for node in G_new_edge_list[i]:

            """ to avoid repetition """
            if node > i:
                u = convert_to_list(i, l_node)
                v = convert_to_list(node, l_node)
                G_new.append((u,v))

    """ 
    checks for connnectedness
    if the graph is not connected, then the same process is repeated
    """
    if check_connected(G_new) == False:
        einstein_graph_create_smallworld(G, alpha)

    return G_new

def check_connected(G):
    """Checks if the graph G is connected or not. The format of the graph is in
    the form of list of tuples as defined above. You can use BFS or any other
    technique that you know of, but you cannot use any graph/networkx libraries."""

    """
    connectedness is checked by performing dfs
    """
    
    l_node = len(G[0][0])
    n_node = 2**l_node

    """ graph represented in the form of edge list """
    G = get_edge_list(G)

    """ stores information about the nodes visited during dfs """
    vis = [0]*n_node

    """ dfs performed from node 0 i.e [0, 0, ... , 0] """
    dfs(G, 0, vis)

    """ True is returned if all nodes are visited during dfs"""
    if sum(vis) == n_node:
        return True
    return False
    

def find_path_in_modified_einsteingraph(G,u,v):
    """ Given the modified Einstein graph G, find a path from u to v. Your
    program should run for a very big graph G and should be as efficient as
    possible. Please note that we are not expecting a shortest path here. Any
    path that connects u to v should be fine, but keep it as optimal in length
    as possible."""

    l_node = len(G[0][0])
    n_node = 2**l_node

    """ graph represented in the form of edge list """
    G = get_edge_list(G)

    """ vertices represented in number form """
    u = convert_to_number(u)
    v = convert_to_number(v)

    """ function to compute shortest path"""
    path = shortest_path(G, u, v, n_node)

    """ the vertices along the path which are represented as numbers are converted to lists """
    for i in range(len(path)):
        path[i] = convert_to_list(path[i], l_node)

    return path