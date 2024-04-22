'''
Andrew Kozempel
CMPSC 413
Lab 9
Fall 2023
'''

import heapq

def dijkstra(graph, start, end):

    # create priority queue, push start node and dist 0
    pqueue = [(0, start)]
    
    # dict to track min distances to nodes
    distances = {node: float('infinity') for node in graph}

    # starting node is dist 0
    distances[start] = 0

    # dict to store previous nodes (to create full path later)
    previous_nodes = {vertex: None for vertex in graph}
    
    # iterate through nodes in pqueue
    while pqueue:

        # pop node with min dist
        curr_dist, curr_node = heapq.heappop(pqueue)
        
        # if end node is reached, return  distance and path
        if curr_node == end:

            #initalize path list
            path = []

            # loop through "previous nodes" to create full path
            while curr_node:
                path.insert(0, curr_node)
                curr_node = previous_nodes[curr_node]

            return curr_dist, path
        
        # calculate distances to neighbors
        for neighbor, weight in graph[curr_node].items():
            dist = curr_dist + weight
            
            # if new distance is shorter
            if dist < distances[neighbor]:

                # update distance and push
                distances[neighbor] = dist
                heapq.heappush(pqueue, (dist, neighbor))
                
                # keep track of previous node
                previous_nodes[neighbor] = curr_node
    
    # if no path, return None
    return None

def floyd_warshall(graph):

    # get list of nodes
    nodes = graph.keys()

    # initalize distance matrix
    distance_matrix = {node: {other: float('infinity') for other in nodes} for node in nodes}

    # iterate through nodes
    for node in nodes:

        # set distance from and to itself to 0
        distance_matrix[node][node] = 0

        # set distance from and to its immediate neighbors to their distances
        for neighbor, distance in graph[node].items():
            distance_matrix[node][neighbor] = distance

    # check distance between i and j, compare to (i to k) + (k to j)
    for k in nodes: # middle node
        for i in nodes: # start node
            for j in nodes: # end node
                
                # if path through k is shorter, update the distance
                if distance_matrix[i][k] + distance_matrix[k][j] < distance_matrix[i][j]:
                    distance_matrix[i][j] = distance_matrix[i][k] + distance_matrix[k][j]

    return distance_matrix

# print driving instructions
def print_navigation_instructions(path):

    instructions = ""

    for i in range(len(path) - 1):
        instructions += f"\tDrive from {path[i]} to {path[i+1]}.\n"

    return instructions

## TESTS

# create graph
graph = {
    'A': {'B': 6, 'C': 10, 'D': 2},
    'B': {'A': 6, 'C': 4, 'E': 5},
    'C': {'A': 10, 'B': 4, 'D': 8, 'F': 6},
    'D': {'A': 2, 'C': 8, 'E': 7},
    'E': {'B': 5, 'D': 7, 'F': 9},
    'F': {'C': 6, 'E': 9, 'G': 3},
    'G': {'F': 3}
}

# print dijkstras algo
time, path = dijkstra(graph, 'A', 'G')
print(f"\nShortest path from A to G:\n\n\tTime: {time} minutes\n\n{print_navigation_instructions(path)}")

# print floyd-warshall algo
fw_distances = floyd_warshall(graph)
print("\nFloyd-Warshall distances:\n")
for source, times in fw_distances.items():
    print('')
    for dest, time in times.items():
        if dest != source:
            print(f"\tFrom {source} to {dest}: {time} min")