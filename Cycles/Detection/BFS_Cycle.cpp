#include "BFS_Cycle.h"

bool BFS_Cycle::detectCycle(const Graph& graph) {
    int V = graph.getVertices();
    std::vector<int> inDegree(V, 0);

    // Compute in-degrees of all vertices
    for (int u = 0; u < V; u++) {
        for (int v : graph.getAdjList()[u]) {
            inDegree[v]++;
        }
    }

    std::queue<int> q;
    for (int i = 0; i < V; i++) {
        if (inDegree[i] == 0) q.push(i);
    }

    int visitedCount = 0;
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        visitedCount++;

        for (int neighbor : graph.getAdjList()[node]) {
            if (--inDegree[neighbor] == 0) q.push(neighbor);
        }
    }

    return (visitedCount != V); // If not all nodes are visited, a cycle exists
}
