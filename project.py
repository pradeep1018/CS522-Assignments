import bz2
import wikitextparser as wtp
import random
import re

def display_topk_pages(path, k):
    """
    for a given bz2 file path containing wikipedia articles and a positive integer k,
    this function returns the top k pages visited when random walk is done on wikigraph
    """

    """ Graph G is the wikigraph in the form of adjacency list """
    G = dict()

    """ frequency stores the number of times a page is visited during random walk """
    frequency = []

    """
    str_to_ind stores the name of the wikipedia article as key and its unique id as value
    ind_to_str stores the unique id of a wikipedia article as key and its name as value
    """
    str_to_ind = dict()
    ind_to_str = dict()

    """ 
    ind is used to generate unique id for every wikipedia article
    ind keeps getting incremented whenever a page which is not present in str_to_ind is encountered
    """
    ind = 0

    """ regular expression of title of a wikipedia article """
    reg_title = '<title>(.*?)</title>'
    curr_title = None

    with bz2.open(path, "rt", encoding="utf8") as file:
        for line in file:
            title = re.findall(reg_title, line)

            """ whenever there is a title in a line, a new wikipedia article starts from there """
            if len(title) > 0:
                curr_title = title[0]

                """ unique id is assigned if the title is not present in str_to_ind """
                if curr_title not in str_to_ind.keys():
                    str_to_ind[curr_title] = ind
                    ind_to_str[ind] = curr_title
                    frequency.append([ind, 0])
                    ind += 1

                """ adjacency list initiated for the given title with empty list """
                if str_to_ind[curr_title] not in G.keys():
                    G[str_to_ind[curr_title]] = []

            """ gets all the wikilinks in a line """
            links = wtp.parse(line).wikilinks
            for link in links:

                """ extracts the article name of the article to which the link is directed """
                neighbour = link.title

                """ unique id is assigned if the article name is not present in str_to_ind """
                if neighbour not in str_to_ind.keys():
                    str_to_ind[neighbour] = ind
                    ind_to_str[ind] = neighbour
                    frequency.append([ind, 0])
                    ind += 1
                
                """ a directed edge from the title of the article to the link is stored """
                if curr_title is not None:
                    G[str_to_ind[curr_title]].append(str_to_ind[neighbour])

    """ starting random walk from a random node """
    current_node = random.randint(0,ind-1)

    """ random walk performed 1 million times """
    for _ in range(int(1e6)):
        frequency[current_node][1] += 1
        
        """ choosing a node randomly from its neighbours"""
        current_node = random.choice(G[current_node])

    """ sorting by frequency in descending order"""
    frequency = sorted(frequency, key = lambda x: x[1], reverse=True)

    print('The top k pages are')

    """ prints top k frequent pages """

    for i in range(k):
        print(ind_to_str[frequency[i][0]])