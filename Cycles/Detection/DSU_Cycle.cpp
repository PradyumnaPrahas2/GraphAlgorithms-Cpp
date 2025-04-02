#include "DSU_Cycle.h"

DSU_Cycle::DSU_Cycle(int V) {
    parent.resize(V);
    rank.resize(V, 0);
    for (int i = 0; i < V; i++) parent[i] = i;
}

int DSU_Cycle::find(int node) {
    if (parent[node] != node) parent[node] = find(parent[node]); // Path compression
    return parent[node];
}

void DSU_Cycle::unionSets(int u, int v) {
    int rootU = find(u), rootV = find(v);
    if (rootU != rootV) {
        if (rank[rootU] > rank[rootV]) parent[rootV] = rootU;
        else if (rank[rootU] < rank[rootV]) parent[rootU] = rootV;
        else {
            parent[rootV] = rootU;
            rank[rootU]++;
        }
    }
}

bool DSU_Cycle::detectCycle(const Graph& graph) {
    for (int u = 0; u < graph.getVertices(); u++) {
        for (int v : graph.getAdjList()[u]) {
            if (find(u) == find(v)) return true;
            unionSets(u, v);
        }
    }
    return false;
}
