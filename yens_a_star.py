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
