'''
Andrew Kozempel
CMPSC 413
Lab 6
Fall 2023
'''

from collections import deque

# O(V + E)
# O(V) - visits every node/vertex
# O(E) - iterates through each edge for each vertex     
def BFS(graph, node):

    # create queue and add starting node
    queue = deque()
    queue.append(node)

    # create visited set
    visited = set()

    # while nodes in queue
    # O(V)
    while queue:

        # pop and print node, then mark as visited
        node = queue.popleft()
        print(node, end = ' -> ')
        visited.add(node)

        # for each adjacent/connected node to current node
        # total: O(E)
        for adj in graph[node]:

            # if connected node has not been visited, add to queue
            if adj not in visited:
                queue.append(adj)    

# O(V + E)
# O(V) - visits every node/vertex
# O(E) - iterates through each edge for each vertex                
def DFS(graph, node):

    # create stack and add starting node
    stack = []
    stack.append(node)

    # create visited set
    visited =  set()

    # while nodes in stack
    # O(V)
    while stack:

        # pop and print node, then mark as visited
        node = stack.pop()
        print(node, end = ' -> ')
        visited.add(node)

        # for each adjacent/connected node to current node
        # total: O(E)
        for adj in graph[node]:

            # if connected node has not been visited, add to stack
            if adj not in visited:
                stack.append(adj)     

# TESTS

graph1 = {
    "a": ["d", "f"],
    "b": ["c"],
    "c": ["b", "c", "d", "e"],
    "d": ["a", "c"],
    "e": ["c"],
    "f": ["a"]
}

graph2 = {
    "a": ["d", "f"],
    "b": ["c", "b"],
    "c": ["b", "c", "d", "e"],
    "d": ["a", "c"],
    "e": ["c"],
    "f": ["a"]
}

# BFS on graph1 and graph2
print("\n\nGraph 1 BFS:")
BFS(graph1, 'a')
print("\n\nGraph 2 BFS:")
BFS(graph2, 'a')

# DFS on graph1 and graph2
print("\n\nGraph 1 DFS:")
DFS(graph1, 'a')
print("\n\nGraph 2 DFS:")
DFS(graph2, 'a')