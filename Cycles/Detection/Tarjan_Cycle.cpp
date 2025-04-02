#include "Tarjan_Cycle.h"

void Tarjan_Cycle::tarjanDFS(int node, const Graph& graph, bool &hasCycle) {
    disc[node] = low[node] = timer++;
    sccStack.push(node);
    onStack[node] = true;

    for (int neighbor : graph.getAdjList()[node]) {
        if (disc[neighbor] == -1) { // Not visited
            tarjanDFS(neighbor, graph, hasCycle);
            low[node] = std::min(low[node], low[neighbor]);
        } else if (onStack[neighbor]) { // Back edge found
            low[node] = std::min(low[node], disc[neighbor]);
            hasCycle = true;
        }
    }

    // If node is SCC root
    if (low[node] == disc[node]) {
        while (!sccStack.empty()) {
            int v = sccStack.top();
            sccStack.pop();
            onStack[v] = false;
            if (v == node) break;
        }
    }
}

bool Tarjan_Cycle::detectCycle(const Graph& graph) {
    int V = graph.getVertices();
    timer = 0;
    disc.assign(V, -1);
    low.assign(V, -1);
    onStack.assign(V, false);
    
    bool hasCycle = false;
    for (int i = 0; i < V; i++) {
        if (disc[i] == -1) tarjanDFS(i, graph, hasCycle);
        if (hasCycle) return true;
    }
    return false;
}
