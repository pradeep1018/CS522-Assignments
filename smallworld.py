import random
import matplotlib.pyplot as plt

def path_teleportation(n=100):
    gt = []
    tgt = []
    for i in range(2,n+1):
        graph = {}
        teleportgraph = {}
        for j in range(i):
            graph[j] = []
            teleportgraph[j] = []
            if j-1>=0:
                graph[j].append(j-1)
                teleportgraph[j].append(j-1)
            if j+1<i:
                graph[j].append(j+1)
                teleportgraph[j].append(j+1)
        vset = list(range(i))
        while len(vset) > 1:
            u = random.choice(vset)
            vset.remove(u)
            v = random.choice(vset)
            vset.remove(v)
            teleportgraph[u].append(v)
            teleportgraph[v].append(u)
        gs = 0
        tgs = 0
        for j in range(i):
            ll = random.sample(range(i),2)
            source = ll[0]
            destination = ll[1]
            gs += abs(source-destination)
            tgsc = 0
            point = source
            while point != destination:
                y = -1
                l = i + 1
                for x in teleportgraph[point]:
                    if abs(destination-x) < l:
                        y = x
                        l = abs(destination-x)
                point = y
                tgsc += 1
            tgs += tgsc
        gt.append(gs/i)
        tgt.append(tgs/i)
    plt.plot(gt, label='no teleportation links')
    plt.plot(tgt, label='random teleportation links')
    plt.title('Expected distance between two random points in a path')
    plt.xlabel('Number of nodes')
    plt.ylabel('Expected distance between two random points')
    plt.legend()
    plt.show()

def matrix_teleportation(n=100):
    gt = []
    tgt = []
    for i in range(2,n+1):
        graph = {}
        teleportgraph = {}
        vset = []
        for j in range(i):
            for k in range(i):
                vset.append((j,k))
                graph[(j,k)] = []
                teleportgraph[(j,k)] = []
                if j-1>=0:
                    graph[(j,k)].append((j-1,k))
                    teleportgraph[(j,k)].append((j-1,k))
                if j+1<i:
                    graph[(j,k)].append((j+1,k))
                    teleportgraph[(j,k)].append((j+1,k))
                if k-1>=0:
                    graph[(j,k)].append((j,k-1))
                    teleportgraph[(j,k)].append((j,k-1))
                if k+1<i:
                    graph[(j,k)].append((j,k+1))
                    teleportgraph[(j,k)].append((j,k+1))
        while len(vset) > 1:
            u = random.choice(vset)
            vset.remove(u)
            v = tuple(random.choice(vset))
            vset.remove(v)
            teleportgraph[u].append(v)
            teleportgraph[v].append(u)
        gs = 0
        tgs = 0
        for j in range(i*i):
            ll = random.sample(range(i),2)
            mm = random.sample(range(i),2)
            source = (ll[0], mm[0])
            destination = (ll[1], mm[1])
            gs += abs(source[0]-destination[0]) + abs(source[1]-destination[1])
            tgsc = 0
            point = source
            while point != destination:
                y = -1
                l = 2*i + 1
                for x in teleportgraph[point]:
                    if abs(destination[0]-x[0]) + abs(destination[1]-x[1]) < l:
                        y = x
                        l = abs(destination[0]-x[0]) + abs(destination[1]-x[1])
                point = y
                tgsc += 1
            tgs += tgsc
        gt.append(gs/(i*i))
        tgt.append(tgs/(i*i))
    plt.plot(gt, label='no teleportation links')
    plt.plot(tgt, label='random teleportation links')
    plt.title('Expected distance between two random points in a matrix')
    plt.xlabel('Number of nodes')
    plt.ylabel('Expected distance between two random points')
    plt.legend()
    plt.show()

def k_neighbour_graph_analysis(n=100, k=5, p=0.2):
    gt = []
    tgt = []
    for i in range(2*k+1,n+1):
        graph = {}
        teleportgraph = {}
        vset = []
        vbset = []
        for a in range(i):
            graph[a] = []
            teleportgraph[a] = []
            for b in range(1,i):
                vbset.append((a,(a+b)%i))
        for a in range(i):
            for b in range(1,k+1):
                graph[a].append((a+b)%i)
                teleportgraph[a].append((a+b)%i)
                graph[(a+b)%i].append(a)
                teleportgraph[(a+b)%i].append(a)
                if b!=1:
                    vset.append((a,(a+b)%i))
                vbset.remove((a,(a+b)%i))
                vbset.remove(((a+b)%i,a))
        for a in range(int(p*i*(k-1))):
            u = random.choice(vset)
            vset.remove(u)
            teleportgraph[u[0]].remove(u[1])
            teleportgraph[u[1]].remove(u[0])
            vbset.append((u[0],u[1]))
            vbset.append((u[1],u[0]))
        for a in range(int(p*i*(k-1))):
            v = random.choice(vbset)
            vbset.remove((v[0],v[1]))
            vbset.remove((v[1],v[0]))
            teleportgraph[v[0]].append(v[1])
            teleportgraph[v[1]].append(v[0])
        gs = 0
        tgs = 0
        for a in range(i):
            ll = random.sample(range(i),2)
            source = ll[0]
            destination = ll[1]
            gs += min(int((abs(source-destination)-1)/k),int((i-abs(source-destination)-1)/k)) + 1
            tgsc = 0
            point = source
            while point != destination:
                y = -1
                l = i+1
                for x in teleportgraph[point]:
                    if min(abs(destination-x),i-abs(destination-x)) < l:
                        y = x
                        l = min(abs(destination-x),i-abs(destination-x))
                point = y
                tgsc += 1
            tgs += tgsc
        gt.append(gs/i)
        tgt.append(tgs/i)
    plt.plot(gt, label='no teleportation links')
    plt.plot(tgt, label='random teleportation links')
    plt.title('Expected distance between two random points in a circular path')
    plt.xlabel('Number of nodes')
    plt.ylabel('Expected distance between two random points')
    plt.legend()
    plt.show()