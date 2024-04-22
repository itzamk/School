'''
Andrew Kozempel
CMPSC 413
Lab 7/8
Fall 2023
'''

from collections import deque
import heapq
import random

class Graph:
    def __init__(self, graph_dict=None):
        self.graph_dict = graph_dict

    def generate_edges(self):

        # create empty list to store edges
        edges = []

        # for each node in the graph
        for node in self.graph_dict:

            # for each neighbor of node, add pair to edges
            for neighbour in self.graph_dict[node]:
                edges.append((node, neighbour))

        # return edges list
        return edges

    def find_isolated_nodes(self):

        # create empty list to store isolated nodes
        isolated = []

        # for each node in the graph
        for node in self.graph_dict:

            # if no neighbors (values), add node (key)
            if not self.graph_dict[node]:
                isolated.append(node)

        # return isolated list
        return isolated

    def find_path(self, start_vertex, end_vertex, path=None):

        # initialize path (first pass)
        if path is None:
            path = []

        # add current vertex
        path = path + [start_vertex]

        # recursion base case, full path found
        if start_vertex == end_vertex:
            return path

        # return none if invalid start vertex        
        if start_vertex not in self.graph_dict:
            return None

        # for each neighbor of current vertex
        for vertex in self.graph_dict[start_vertex]:

            # if neighbor is not in current path
            if vertex not in path:

                # recursivley try to add nodes to path until end node
                extended_path = self.find_path(vertex, end_vertex, path)

                # return path if found
                if extended_path: 
                    return extended_path

        # if no path is found    
        return None

    def find_all_paths(self, start_vertex, end_vertex, path=[]):

        # add current vertex
        path = path + [start_vertex]

        # recursion base case, full path found
        if start_vertex == end_vertex:
            return [path]

        # return none if invalid start vertex        
        if start_vertex not in self.graph_dict:
            return []

        # list to store paths
        paths = []

        # for each neighbor of current vertex
        for vertex in self.graph_dict[start_vertex]:

            # if neighbor not in path
            if vertex not in path:

                # recursivley try to add nodes to path until end node
                extended_paths = self.find_all_paths(vertex, end_vertex, path)

                # for paths found, add to list
                for p in extended_paths: 
                    paths.append(p)

        # return paths
        return paths

    def is_connected(self, vertices_encountered=None, start_vertex=None):
        
        # convert to set
        if vertices_encountered is None:
            vertices_encountered = set()

        # get list of vertices
        vertices = list(self.graph_dict.keys())

        # get starting vertex
        if not start_vertex:
            start_vertex = vertices[0]

        # add starting vertices to visited
        vertices_encountered.add(start_vertex)

        # if all nodes not visited
        if len(vertices_encountered) != len(vertices):

            # for neighbors of current starting vertex
            for vertex in self.graph_dict[start_vertex]:

                # visit unvisited vertices
                if vertex not in vertices_encountered:

                    # recursively check new vertex
                    if self.is_connected(vertices_encountered, vertex):
                        return True
        
        # all nodes visited
        else:
            return True
        
        # not all vertices visited
        return False
    
# TESTS

graph = { "a" : ['b','c'],
            "b" : ['c', 'd'],
            "c" : ['d'],
            "d" : ['c'],
            "e" : ['f'],
            "f" : []
            }

graph1 = { "a" : ["d","f"],
            "b" : ["c"],
            "c" : ["b", "c", "d", "e"],
            "d" : ["a", "c"],
            "e" : ["c"],
            "f" : ["a"]
            }
graph2 = { "a" : ["d","f"],
            "b" : ["c","b"],
            "c" : ["b", "c", "d", "e"],
            "d" : ["a", "c"],
            "e" : ["c"],
            "f" : ["a"]
            }

# create graphs
g = Graph(graph)
g1 = Graph(graph1)
g2 = Graph(graph2)

graphs = [g, g1, g2]

for i, graph in enumerate(graphs):

    start_vertex, end_vertex = random.sample(list(graph.graph_dict.keys()), 2) 

    print(f"Testing Graph {i+1}:")
    print("Edges:", graph.generate_edges())
    print("Isolated nodes:", graph.find_isolated_nodes())
    print(f"Path from {start_vertex} to {end_vertex}:", graph.find_path(start_vertex, end_vertex))
    print(f"All paths from {start_vertex} to {end_vertex}:", graph.find_all_paths(start_vertex, end_vertex))
    print("Is graph connected:", graph.is_connected())
    print()

#### PART 3

def BFS(graph, node):

    # create queue and add starting node
    queue = deque()
    queue.append(node)

    # create visited set, add starting node
    visited = set()
    visited.add(node)

    # while nodes in queue
    while queue:

        # pop and print node
        node = queue.popleft()
        print(node, end = ' -> ')

        # for each adjacent/connected node to current node
        for adj, _ in graph[node]:

            # if connected node has not been visited, add to queue/visited
            if adj not in visited:
                visited.add(adj)
                queue.append(adj)    

def DFS(graph, node):

    # create stack and add starting node
    stack = []
    stack.append(node)

    # create visited set, add starting node
    visited =  set()
    visited.add(node)

    # while nodes in stack
    while stack:

        # pop and print node
        node = stack.pop()
        print(node, end = ' -> ')

        # for each adjacent/connected node to current node
        for adj, _ in graph[node]:

            # if connected node has not been visited, add to stack/visited
            if adj not in visited:
                visited.add(adj)
                stack.append(adj)  
                
def dijkstra(graph, start):

    # create priority queue, push start node and dist 0
    pqueue = [(0, start)]
    
    # dict to track min distances to nodes
    distances = {node: float('infinity') for node in graph}

    # starting node is dist 0
    distances[start] = 0
    
    # iterate through nodes
    while pqueue:

        # pop node with min dist
        curr_dist, curr_node = heapq.heappop(pqueue)
        
        # skip current path if longer than previous
        if curr_dist > distances[curr_node]:
            continue
        
        # calculate distances to neighbors
        for neighbor, weight in graph[curr_node]:
            dist = curr_dist + weight
            
            # if new distance is shorter
            if dist < distances[neighbor]:

                # update distance and push
                distances[neighbor] = dist
                heapq.heappush(pqueue, (dist, neighbor))
    
    # return distances
    return distances

# TEST

graph = {
    1: [(2, 10), (3, 15), (6, 5)],
    2: [(1, 10), (3, 7)],
    3: [(1, 15), (2, 7), (4, 7), (6, 10)],
    4: [(3, 7), (5, 7), (6, 5)],
    5: [(4, 7), (6, 13)],
    6: [(1, 5), (3, 10), (4, 5), (5, 13)]
}

print("BFS:")
BFS(graph, 1)

print("\n\nDFS:")
DFS(graph, 1)

print("\n\nDijkstra's algorithm:")
print(dijkstra(graph, 1))