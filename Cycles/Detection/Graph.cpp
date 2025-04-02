#include "Graph.h"

Graph::Graph(int V) {
    this->V = V;
    adj.resize(V);
}

void Graph::addEdge(int u, int v) {
    adj[u].push_back(v);
}

const std::vector<std::vector<int>>& Graph::getAdjList() const {
    return adj;
}

int Graph::getVertices() const {
    return V;
}
