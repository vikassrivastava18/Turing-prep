# Stack
class Stack:
    """
    Collection of items stacked in list with policy of FILO.
    """

    def __init__(self, collection:(None|list) = None) -> None:
        self.collection = collection if collection else []

    def add(self, item) -> None:
        self.collection.append(item)

    def remove(self) -> any:
        return self.collection.pop()
    
    def length(self) -> int:
        return len(self.collection)
    
    def __str__(self):
        return f"Stack collections: {self.collection}"
    

class Queue(Stack):
    """
    Similar to Stack, only difference is it uses FIFO policiy.
    """

    def remove(self) -> any:
        first_item = self.collection[0]
        self.collection = self.collection[1:]
        return first_item
    
    def __str__(self):
        return f"Queue collection: {self.collection}"
    

st = Stack([1,2,3])
qu = Queue([5,5,6])
st.add(0)
qu.add(0)

print(st.remove())
print(qu.remove())

# Undirected graph
def maze_connected(start: int, end: int, connected_pairs: list, util= 'stack') -> bool:
    """
    Given a list of connected pairs in a maze: [(1,2), [2,3), ...]
    Check whether start node is connected to end node
    """
    node = start
    if node == end:
        return True
    
    visited = []
    track_parent = {node: None}
    path = Stack([start]) if util == 'stack' else Queue([start])

    while not node == end and path.length() > 0:
        node = path.remove()
        visited.append(node)
        for item in connected_pairs[node]:
            if not item in visited:
                path.add(item)
                track_parent[item] = node
        # Remove the node
    if node == end:
        parent_list = []
        parent = end        

        while track_parent[parent]:
            parent_list.append(parent)
            parent = track_parent[parent]
        parent_list.append(start)
        print("Path: ", parent_list[::-1])
        return True
    return False

connected_pairs = {1: [4,2], 2: [1], 3: [6], 6: [5, 3], 4: [7, 1], 5:[6], 7: [8, 4], 8:[9, 7], 9:[8]}
print(maze_connected(4,9, connected_pairs=connected_pairs))
print(maze_connected(8,4, connected_pairs=connected_pairs))
print(maze_connected(1,9, connected_pairs=connected_pairs))
print(maze_connected(3,9, connected_pairs=connected_pairs))
print(maze_connected(1,6, connected_pairs=connected_pairs))

print("------------------------")
connected_pairs = {1: [4,2], 2: [1], 3: [6], 6: [5, 3], 4: [7, 1], 5:[6], 7: [8, 4], 8:[9, 7], 9:[8]}
print(maze_connected(4,9, connected_pairs=connected_pairs), 'queue')
print(maze_connected(8,4, connected_pairs=connected_pairs), 'queue')
print(maze_connected(1,9, connected_pairs=connected_pairs), 'queue')
print(maze_connected(3,9, connected_pairs=connected_pairs), 'queue')
print(maze_connected(1,6, connected_pairs=connected_pairs), 'queue')


import random, copy
def min_cuts(graph: list) -> list:
    """
    Reduce the size of graph by collapsing two random nodes.
    Update the graph.
    Return the edges count when the graph has only two nodes.
    """
    _graph = copy.deepcopy(graph)

    while len(_graph) > 2:
        # Select an edge randomly
        a = random.choice(list(_graph.keys()))
        b = random.choice(_graph[a])

        # Append all b's connections to a
        _graph[a].extend(_graph[b])

        # Replace b from all nodes with a
        for node in _graph[b]:
            _graph[node] = [a if x == b else x for x in _graph[node]]

        # Remove self loops in graph
        for node in _graph.keys():
            _graph[node] = [item for item in _graph[node] if not item == node]

        # Remove self loops in a
        # _graph[a] = [node for node in _graph[a] if node != a]

        # Remove b from graph
        del _graph[b]

    # return sum([len(_graph[item]) for item in _graph])
    remaining_nodes = list(_graph.keys())
    return len(_graph[remaining_nodes[0]])  # or len(_graph[remaining_nodes[1]])


# def min_cuts(graph: dict) -> int:
#     """
#     Implements Karger's algorithm to estimate the minimum cut of an undirected graph.
#     Collapses edges randomly until only two supernodes remain.

#     Parameters:
#     - graph: adjacency list of the graph {node: [connected_nodes]}

#     Returns:
#     - Minimum number of crossing edges between the final two nodes
#     """
#     _graph = copy.deepcopy(graph)

#     while len(_graph) > 2:
#         # Step 1: Pick a random edge (u, v)
#         u = random.choice(list(_graph.keys()))
#         v = random.choice(_graph[u])

#         # Step 2: Merge node v into node u
#         _graph[u].extend(_graph[v])

#         # Step 3: Replace all occurrences of v with u in the graph
#         for node in _graph[v]:
#             _graph[node] = [u if x == v else x for x in _graph[node]]

#         # Step 4: Remove self-loops from u's list
#         _graph[u] = [x for x in _graph[u] if x != u]

#         # Step 5: Delete node v from the graph
#         del _graph[v]

#     # Return the number of edges between the two remaining supernodes (undirected => divide by 2)
#     remaining_nodes = list(_graph.keys())
#     return len(_graph[remaining_nodes[0]])  # or len(_graph[remaining_nodes[1]])

print("!@##$%$####---------")
g = {1: [2,3], 2: [1,4], 3: [1,6], 4: [2,5], 5: [4,6], 6:[3,5]}
print(min_cuts(g))

g2 = {
    1: [2, 3, 4],
    2: [1, 3],
    3: [1, 2, 4],
    4: [1, 3]
}
print(min_cuts(g2))
        
g3 = {
    1: [2],
    2: [1, 3],
    3: [2, 4],
    4: [3]
}
print(min_cuts(g3))


g4 = {
    1: [2, 3, 4],
    2: [1, 3, 4],
    3: [1, 2, 4],
    4: [1, 2, 3]
}

print(min_cuts(g4))


def min_cuts_gpt(graph: dict) -> int:
    """
    Implements Karger's algorithm to estimate the minimum cut of an undirected graph.
    Collapses edges randomly until only two supernodes remain.

    Parameters:
    - graph: adjacency list of the graph {node: [connected_nodes]}

    Returns:
    - Minimum number of crossing edges between the final two nodes
    """
    _graph = copy.deepcopy(graph)

    while len(_graph) > 2:
        # Step 1: Pick a random edge (u, v)
        u = random.choice(list(_graph.keys()))
        v = random.choice(_graph[u])

        # Step 2: Merge node v into node u
        _graph[u].extend(_graph[v])

        # Step 3: Replace all occurrences of v with u in the graph
        for node in _graph[v]:
            _graph[node] = [u if x == v else x for x in _graph[node]]

        # Step 4: Remove self-loops from u's list
        _graph[u] = [x for x in _graph[u] if x != u]

        # Step 5: Delete node v from the graph
        del _graph[v]

    # Return the number of edges between the two remaining supernodes (undirected => divide by 2)
    remaining_nodes = list(_graph.keys())
    return len(_graph[remaining_nodes[0]])  # or len(_graph[remaining_nodes[1]])

g = {1: [2,3], 2: [1,4], 3: [1,6], 4: [2,5], 5: [4,6], 6:[3,5]}
print(min_cuts_gpt(g))

g2 = {
    1: [2, 3, 4],
    2: [1, 3],
    3: [1, 2, 4],
    4: [1, 3]
}
print(min_cuts_gpt(g2))
        
g3 = {
    1: [2],
    2: [1, 3],
    3: [2, 4],
    4: [3]
}
print(min_cuts_gpt(g3))


g4 = {
    1: [2, 3, 4],
    2: [1, 3, 4],
    3: [1, 2, 4],
    4: [1, 2, 3]
}

print(min_cuts_gpt(g4))


def dikstra(graph: dict, start, end) -> int:
    """
    Paramenters: adjacent list for the graph
    Update distance while traversing from start node to end
    """
    # Initialize all distances to a very large number (infinity), except the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    node = start
    visited = [node]

    while not node == end:
        for item in graph[node]:
            distances[item[0]] = min(distances[item[0]], distances[node] + item[1])
        # Find the next node
        _min = float('inf')
        for item in graph[node]:
            if not item[0] in visited:
                if distances[item[0]] < _min:
                    next_node = item[0]
                    _min = distances[item[0]]
        node = next_node
        visited.append(node)
    print("Distances: ", distances)
    return distances[end]

#     (A)
#    /   \
#  1/     \4
#  /       \
# (B)----2--(C)
#   \       /
#    \3    /1
#     \   /
#      (D)


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 3)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 3), ('C', 1)]
}

print(dikstra(graph=graph, start='A', end='D'))


import heapq
def dijkstra_gpt(graph, start):
    # Step 1: Initialize
    min_heap = [(0, start)]  # (distance, node)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        # Skip nodes already visited
        if current_node in visited:
            continue

        visited.add(current_node)

        # Step 2: Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If found a shorter path to neighbor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 3)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 3), ('C', 1)]
}

print(dijkstra_gpt(graph=graph, start='A'))


# DAG
# A → C ← B -> F
# ↓            ↓
# D            E


# Output (one possible)
# A, B, C, D, E


graph = {'A':[], 'B': [], 'C':['A', 'B'], 'D': ['A'], 'E': ['F'], 'F': ['B']}

def dag_topo_sort(graph: dict) -> list:
    """
    Given a DAG (directed acyclic graph), find a possible topological order
    Return a list of a possible solution  
    """
    # Find all the nodes with zero incoming nodes
    _graph = copy.deepcopy(graph)
    zeros = [node for node in _graph if len(_graph[node]) == 0]

    queue = Queue(zeros)
    result = []

    while len(queue.collection) > 0:
        # Remove one node from queue
        node = queue.remove()
        # Add to the result list
        result.append(node)
        # Update the graph
        for item in _graph:
            if node in _graph[item]:
                _graph[item] = [n for n in _graph[item] if n != node]

        # Add zeros
        new_zeros = [node for node in _graph if len(_graph[node]) == 0 and node not in queue.collection and node not in result]
        queue.collection.extend(new_zeros)

    return result

print(dag_topo_sort(graph=graph))


# Count components
def count_components(graph: dict) -> int:
    comp_count = 1
    # queue = Queue([random.choice(graph.keys())])
    queue = Queue([random.choice(list(graph.keys()))])
    visited = []

    while len(visited) < len(list(graph.keys())):
        if not len(queue.collection) == 0:
            node = queue.remove()
        else:
            comp_count +=1
            node = random.choice([n for n in graph.keys() if n not in visited])
        visited.append(node)
        neighbors = graph[node]
        # Add only neighbors not already visited
        for neighbor in neighbors:
            if not neighbor in visited and neighbor not in queue.collection:
                queue.add(neighbor)

    return comp_count


# assert count_components(g) == 3, f"Components count not correct, should be 3"


# Largest component size
def largest_component(graph: dict) -> list:
    """
    Params: graph is an adjacency list of nodes
    Returns the largest component in the graph
    """
    comp_count = 1
    # queue = Queue([random.choice(graph.keys())])
    queue = Queue([random.choice(list(graph.keys()))])
    visited = set()
    # Keep track of global max
    max_count = 0
    # Keep track of component max
    comp_count = 0
    while len(visited) <= len(list(graph.keys())):
        if len(visited) == len(list(graph.keys())):
            max_count = max(max_count, comp_count)
            return max_count
        if len(queue.collection) == 0:
            # Keep track of global count
            max_count = max(max_count, comp_count)
            comp_count = 0
            node = random.choice([n for n in graph.keys() if n not in visited])
        else:
            node = queue.remove()
            comp_count += 1
        visited.add(node)
        neighbors = graph[node]
        # Add only neighbors not already visited
        for neighbor in neighbors:
            if not neighbor in visited and neighbor not in queue.collection:
                queue.add(neighbor)

    return max_count

from collections import deque

def largest_component_gpt(graph: dict) -> int:
    """
    Params:
        graph: dict representing an adjacency list
    Returns:
        Size of the largest connected component
    """
    visited = set()
    max_count = 0

    for node in graph:
        if node not in visited:
            size = 0
            queue = deque([node])

            while queue:
                current = queue.popleft()
                if current in visited:
                    continue
                visited.add(current)
                size += 1
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)

            max_count = max(max_count, size)

    return max_count

g1 = {0: [1,2], 1: [0,2], 2: [0,1], 3: [4,5,-1], 4: [3,6,-2], -1: [3], -2: [4],
      5: [3,6], 6: [4,5], 7: [], 8: [9], 9: [8], 10: [11,12], 11: [10,12], 12: [10,11]} 
print("Largest component GPT: ", largest_component_gpt(g1))
g2= {0: [1,2], 1: [0,2], 2: [0,1]} 
print("Largest component GPT: ", largest_component_gpt(g2))


print("Largest component: ", largest_component(g1))
print("Largest component: ", largest_component(g2))

def islands_count(graph) -> int:
    pass
    
    
def minimum_island_size(graph) -> int:
    """
    ???
    """
    pass


# Directed Graph
def nodes_connected(graph: dict, start: int, end: int) -> bool:
    pass




