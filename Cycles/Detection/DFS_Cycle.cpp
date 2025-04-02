#include "DFS_Cycle.h"

bool DFS_Cycle::dfs(int node, int parent, std::vector<bool>& visited, const Graph& graph) {
    visited[node] = true;

    for (int neighbor : graph.getAdjList()[node]) {
        if (!visited[neighbor]) {
            if (dfs(neighbor, node, visited, graph)) return true;
        } else if (neighbor != parent) {
            return true;
        }
    }
    return false;
}

bool DFS_Cycle::detectCycle(const Graph& graph) {
    std::vector<bool> visited(graph.getVertices(), false);
    for (int i = 0; i < graph.getVertices(); i++) {
        if (!visited[i] && dfs(i, -1, visited, graph)) return true;
    }
    return false;
}
