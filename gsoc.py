from flask import Flask, request, jsonify
from flask_cors import CORS
import heapq
import concurrent.futures
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict, deque
import os
import networkx as nx
import matplotlib.pyplot as plt
from flask import send_from_directory
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

INF = float('inf')

def preprocess_input(data):
    """Preprocess input by converting string values to integers."""
    try:
        nodes = int(data.get('nodes', 0))
        source = int(data.get('source'))
        destination = int(data.get('destination'))
        k = int(data.get('k', 1))
        algorithm = data.get('algorithm', 'yens')

        edges = [
            (int(edge['from']), int(edge['to']), int(edge['cost']))
            for edge in data.get('edges', [])
        ]

        return {
            'nodes': nodes,
            'edges': edges,
            'source': source,
            'destination': destination,
            'k': k,
            'algorithm': algorithm
        }
    except Exception as e:
        return {'error': str(e)}

def dijkstra(graph, source, target):
    """Find the shortest path using Dijkstra's algorithm."""
    try:
        n = len(graph)
        dist = {node: INF for node in graph}
        prev = {node: None for node in graph}
        dist[source] = 0
        pq = [(0, source)]

        while pq:
            cost, node = heapq.heappop(pq)
            if node == target:
                break
            for neighbor, weight in graph.get(node, []):
                new_cost = cost + weight
                if new_cost < dist[neighbor]:
                    dist[neighbor] = new_cost
                    prev[neighbor] = node
                    heapq.heappush(pq, (new_cost, neighbor))

        path, curr = [], target
        while curr is not None:
            path.append(curr)
            curr = prev[curr]
        path.reverse()

        return path if path[0] == source else []
    except Exception as e:
        return str(e)

def a_star_algorithm(edges, source, target):
    """Find the shortest path using A* algorithm."""
    try:
        graph = {}
        for u, v, w in edges:
            graph.setdefault(u, []).append((v, w))
            graph.setdefault(v, []).append((u, w))

        pq = [(0, source, [])]
        visited = set()

        while pq:
            cost, node, path = heapq.heappop(pq)
            if node in visited:
                continue
            path = path + [node]
            if node == target:
                return path
            visited.add(node)
            for neighbor, weight in graph.get(node, []):
                heapq.heappush(pq, (cost + weight, neighbor, path))

        return []
    except Exception as e:
        return str(e)

def yen_k_shortest_paths(edges, source, target, k):
    """Find the K shortest paths using Yen's algorithm."""
    try:
        graph = {}
        for u, v, w in edges:
            graph.setdefault(u, []).append((v, w))
            graph.setdefault(v, []).append((u, w))

        shortest_paths = []
        base_path = dijkstra(graph, source, target)
        if not base_path:
            return []

        shortest_paths.append(base_path)

        candidates = []
        for _ in range(1, k):
            for i in range(len(base_path) - 1):
                spur_node = base_path[i]
                root_path = base_path[:i + 1]
                modified_graph = {node: neighbors[:] for node, neighbors in graph.items()}

                for path in shortest_paths:
                    if path[:i + 1] == root_path and len(path) > i + 1:
                        modified_graph[path[i]].remove(
                            (path[i + 1], next(w for v, w in graph[path[i]] if v == path[i + 1]))
                        )

                spur_path = dijkstra(modified_graph, spur_node, target)
                if spur_path:
                    total_path = root_path[:-1] + spur_path
                    if total_path not in shortest_paths:
                        heapq.heappush(candidates, (len(total_path), total_path))

            if candidates:
                _, new_path = heapq.heappop(candidates)
                shortest_paths.append(new_path)
            else:
                break

        return shortest_paths
    except Exception as e:
        return str(e)

@app.route('/k_shortest_paths', methods=['POST'])
def k_shortest_paths():
    """API endpoint to compute K shortest paths or A* path."""
    try:
        data = request.get_json()
        print(data)
        processed_data = preprocess_input(data)

        if 'error' in processed_data:
            return jsonify({'error': processed_data['error']}), 400

        algorithm = processed_data['algorithm'].lower()
        edges = processed_data['edges']
        source = processed_data['source']
        destination = processed_data['destination']
        k = processed_data['k']

        if algorithm == "yens":
            paths = yen_k_shortest_paths(edges, source, destination, k)
            return jsonify({'k_shortest_paths': paths})
        elif algorithm == "a_star":
            path = a_star_algorithm(edges, source, destination)
            return jsonify({'a_star_path': path})
        else:
            return jsonify({'error': 'Invalid algorithm choice'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
def find_all_cycles_parallel(edges, num_nodes):
    """The task is to find all unique cycles in a graph using multithreading DFS + Backtracking."""
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # I am Generating A graph in form of an Adjacency List

    unique_cycles = set() # set to store all cycles
    visited = set() # keeping track of visited Nodes in dfs

    def dfs(node, parent, path):
        visited.add(node)
        path.append(node)

        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if neighbor in path:
                cycle = tuple(sorted(path[path.index(neighbor):]))  # Normalizing cycle
                unique_cycles.add(cycle)
            else:
                dfs(neighbor, node, path)

        path.pop()
        visited.remove(node)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        #Since i am starting dfs from every node to find all cycles  
        #I can execute the function in parallel instead of sequentially and it wouldnt effect other function calls.  

        #Additionally, since all paths are stored in a set
        #duplicate results are automatically eliminated, ensuring a unique output

        #Parallelization enhances the efficiency of this approach  
        #compared to traditional backtracking and dfs methods.  
        futures = [executor.submit(dfs, i, -1, []) for i in range(num_nodes) if i not in visited]
        concurrent.futures.wait(futures)

    return list(map(list, unique_cycles)) # i return the list of all paths

@app.route('/find_all_cycles', methods=['POST'])
def find_all_cycles():
    """API to detect all cycles in a graph."""
    try:
        data = request.get_json()
        edges = [(int(edge['from']), int(edge['to'])) for edge in data.get('edges', [])]
        num_nodes = int(data.get('nodes', 0))
        
        cycles = find_all_cycles_parallel(edges, num_nodes)
        return jsonify({"cycles": cycles})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def dfs_cycle_detection(graph, V):
    visited = set()
    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if neighbor in visited or dfs(neighbor, node):
                return True
        return False
    
    for node in range(V):
        if node not in visited:
            if dfs(node, -1):
                return True
    return False

def union_find_cycle_detection(edges, V):
    parent = list(range(V))
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    for u, v in edges:
        pu, pv = find(u), find(v)
        if pu == pv:
            return True
        parent[pu] = pv
    return False

def vertex_coloring_cycle_detection(graph, V):
    color = [0] * V
    def dfs(node):
        color[node] = 1
        for neighbor in graph[node]:
            if color[neighbor] == 1 or (color[neighbor] == 0 and dfs(neighbor)):
                return True
        color[node] = 2
        return False
    
    for node in range(V):
        if color[node] == 0 and dfs(node):
            return True
    return False

def bfs_cycle_detection(graph, V):
    # Initialize in_degree for all nodes (even those without edges)
    in_degree = {i: 0 for i in range(V)}

    # Compute in-degree for each node
    for node in graph:
        for neighbor in graph[node]:
            if neighbor not in in_degree:
                in_degree[neighbor] = 0  # Ensure existence
            in_degree[neighbor] += 1  # Increment in-degree
    
    # Queue to store nodes with in-degree 0
    queue = deque([node for node in in_degree if in_degree[node] == 0])

    visited = 0
    while queue:
        node = queue.popleft()
        visited += 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If all nodes are not visited, there is a cycle
    return visited != V

def tarjan_scc_cycle_detection(graph, V):
    index = [-1] * V  # Ensure it covers all nodes
    lowlink = [-1] * V
    stack = []
    on_stack = [False] * V
    current_index = [0]
    has_cycle = [False]

    def strong_connect(node):
        if index[node] != -1:  # Already visited
            return
        index[node] = lowlink[node] = current_index[0]
        current_index[0] += 1
        stack.append(node)
        on_stack[node] = True

        for neighbor in graph.get(node, []):  # Ensure valid access
            if neighbor >= V:  # Prevent out-of-range errors
                continue
            if index[neighbor] == -1:
                strong_connect(neighbor)
                lowlink[node] = min(lowlink[node], lowlink[neighbor])
            elif on_stack[neighbor]:
                lowlink[node] = min(lowlink[node], index[neighbor])

        # If node is a root SCC
        if lowlink[node] == index[node]:
            scc = []
            while stack:
                v = stack.pop()
                on_stack[v] = False
                scc.append(v)
                if v == node:
                    break
            if len(scc) > 1:  # More than 1 node means a cycle
                has_cycle[0] = True

    for node in range(V):
        if index[node] == -1:
            strong_connect(node)

    return has_cycle[0]


@app.route('/detect_cycles', methods=['POST'])
def detect_cycles():
    data = request.json

    # Extract nodes and edges, ensuring they are valid
    edges = [(int(edge['from']), int(edge['to'])) for edge in data.get('edges', []) if 'from' in edge and 'to' in edge]
    print(edges)
    # Extract unique nodes
    unique_nodes = set()
    for u, v in edges:
        unique_nodes.add(u)
        unique_nodes.add(v)
    
    V = len(unique_nodes)  # Update V based on actual unique nodes
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # Assuming undirected graph

    # Run cycle detection algorithms in parallel
    with ThreadPoolExecutor() as executor:
        results = executor.map(lambda func: func(graph, V) if func != union_find_cycle_detection else func(edges, V),
                               [dfs_cycle_detection, union_find_cycle_detection, vertex_coloring_cycle_detection, bfs_cycle_detection, tarjan_scc_cycle_detection])
    
    return jsonify({
        'DFS_Backtracking': next(results),
        'Union_Find': next(results),
        'Vertex_Coloring': f"{next(results)} (works for directed Graphs)",
        'BFS_Kahn': f"{next(results)} (works for directed Graphs)",
        'Tarjan_SCC': f"{next(results)} (works for directed Graphs)",
    })

@app.route('/process-graph',methods=['POST'])
def process_graph():
    data = request.json
    node_count = data.get("nodeCount")
    edges = data.get("edges", [])
    try:
    # Convert edges list to an adjacency matrix
        adj_matrix = [[0] * node_count for _ in range(node_count)]

        for edge in edges:
            from_node, to_node = edge["from"], edge["to"]
            adj_matrix[from_node][to_node] = 1  # Marking edge existence
            adj_matrix[to_node][from_node] = 1
        
        # Save graph as image
        result = plot_graph_from_adjacency(adj_matrix, filename="graph.png")
    except:
        result=1
    if(result==1):
        return jsonify({"message":"Incorrect Input","image_path":"error.jpg"})
    else:
        return jsonify({"message": "Graph processed successfully", "image_path": "graph.png"})

SAVE_DIR = "saved_graphs"
os.makedirs(SAVE_DIR, exist_ok=True)

def plot_graph_from_adjacency(matrix, filename="graph.png"):
    try:
        G = nx.DiGraph()  # Create a Directed Graph
        
        # Add edges based on adjacency matrix
        num_nodes = len(matrix)
        G.add_nodes_from(range(num_nodes))

        for i in range(num_nodes):
            for j in range(num_nodes):
                if matrix[i][j] == 1:  # If there is an edge from i → j
                    G.add_edge(i, j)
        
        # Create figure and axis
        fig, ax = plt.subplots(figsize=(6, 6))
        pos = nx.spring_layout(G)  # Layout for visualization

        nx.draw(G, pos, with_labels=True, node_color="skyblue", edge_color="black", arrows=True, ax=ax)
        
        # Save image instead of showing
        filepath = os.path.join(SAVE_DIR, filename)
        plt.savefig(filepath)
        plt.close()
        return 0
    except:
        return 1
@app.route('/saved_graphs/<filename>')
def get_image(filename):
    return send_from_directory(SAVE_DIR, filename)

@app.route('/testing')
def test():
    return jsonify({"message":"hello"})
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
