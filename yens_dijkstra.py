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
