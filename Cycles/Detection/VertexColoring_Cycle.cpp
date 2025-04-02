#include "VertexColoring_Cycle.h"

bool VertexColoring_Cycle::dfs(int node, std::vector<int>& color, const Graph& graph) {
    color[node] = 1; // Grey (Processing)

    for (int neighbor : graph.getAdjList()[node]) {
        if (color[neighbor] == 1) return true;
        if (color[neighbor] == 0 && dfs(neighbor, color, graph)) return true;
    }

    color[node] = 2; // Black (Processed)
    return false;
}

bool VertexColoring_Cycle::detectCycle(const Graph& graph) {
    std::vector<int> color(graph.getVertices(), 0);
    for (int i = 0; i < graph.getVertices(); i++) {
        if (color[i] == 0 && dfs(i, color, graph)) return true;
    }
    return false;
}
