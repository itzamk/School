'''
Andrew Kozempel
CMPSC 413
Lab 7
Fall 2023
'''

import heapq

def find(parent, i):

    # if i is its own parent, root found.
    if parent[i] == i:
        return i
    
    # recursively call find on parent
    return find(parent, parent[i])

def union(parent, rank, x, y):

    # attach smaller rank tree to higher rank tree
    if rank[x] < rank[y]:
        parent[x] = y

    elif rank[x] > rank[y]:
        parent[y] = x

    # same rank, x is root, increment rank
    else:
        parent[y] = x
        rank[x] += 1

def kruskals_algo(graph, vertices):

    # store the MST
    result = []

    i = 0 # used to iterate over edges
    e = 0 # used to count added edges

    # sort graph by edge weights
    graph = sorted(graph, key=lambda item: item[2])

    # initialize the parent and ranks of nodes
    parent = [i for i in range(vertices)]
    rank = [0] * vertices

    # loop until there are (vertices-1) edges 
    # (property of MST for connected graph)
    while e < vertices - 1:

        # select edge with next smallest weight + increment i
        source, destination, weight = graph[i]
        i += 1

        # find roots of sets
        x = find(parent, source)
        y = find(parent, destination)

        # if different roots (sets) - does not create a cycle
        if x != y:

            # increment edge counter, add edge to MST, merge sets
            e += 1
            result.append((source, destination, weight))
            union(parent, rank, x, y)

    return result

def prims_algo(vertices, graph):

    # convert graph to adjacency list
    adj_list = {i: [] for i in range(vertices)}
    for u, v, w in graph:
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))

    # flag all vertices as not in MST
    added = [False] * vertices
    
    # prioirty queue to select edge with the min weight
    # initialize with w0, v0, previous placeholder of -1
    pqueue = [(0, 0, -1)]
    
    mst = []  # edges in the MST

    # iterate through all vertices
    while pqueue:

        # get edge with min weight
        weight, u, prev = heapq.heappop(pqueue)

        # if vertex is already in MST, skip
        if added[u]:
            continue

        # mark vertex as added in MST
        added[u] = True  

        # add edge, if its not the starting vertex
        if prev != -1:
            mst.append((prev, u, weight))

        # push neighbors in to priority queue, if theyre not in MST
        for v, w in adj_list[u]:

            if not added[v]:
                heapq.heappush(pqueue, (w, v, u))

    return mst


##### TESTS

# dense graph and vertices count
dense_v = 9
dense = [(0, 1, 4), (0, 7, 8), 
         (1, 2, 8), (1, 7, 11), 
         (2, 3, 7), (2, 5, 4), (2, 8, 2), 
         (3, 4, 9), (3, 5, 14), 
         (4, 5, 10),
         (5, 6, 2), 
         (6, 7, 1), (6, 8, 6), 
         (7, 8, 7)]

# sparse graph and vertices count
sparse_v = 7
sparse = [(0, 1, 7), (0, 3, 5), 
          (1, 2, 8), (1, 3, 9), (1, 4, 7), 
          (2, 4, 5), 
          (3, 4, 15), (3, 5, 6),
          (4, 5, 8), (4, 6, 9), 
          (5, 6, 11)]

# results fo kruskals
mst_dense = kruskals_algo(dense, dense_v)
mst_sparse = kruskals_algo(sparse, sparse_v)

print("MST for the dense graph KRUSKAL'S:")
dense_total = 0
for edge in mst_dense:
    dense_total += edge[2]
    print(f'Edge Added: {edge}\t\t Total: {dense_total}')

print("\nMST for the sparse graph KRUSKAL'S:")
sparse_total = 0
for edge in mst_sparse:
    sparse_total += edge[2]
    print(f'Edge Added: {edge}\t\t Total: {sparse_total}')

# results for prims
mst_edges_dense = prims_algo(dense_v, dense)
mst_edges_sparse = prims_algo(sparse_v, sparse)

print("\nMST for the dense graph PRIM'S:")
dense_total = 0
for edge in mst_edges_dense:
    dense_total += edge[2]
    print(f'Edge Added: {edge}\t\t Total: {dense_total}')

print("\nMST for the sparse graph PRIM'S:")
sparse_total = 0
for edge in mst_edges_sparse:
    sparse_total += edge[2]
    print(f'Edge Added: {edge}\t\t Total: {sparse_total}')