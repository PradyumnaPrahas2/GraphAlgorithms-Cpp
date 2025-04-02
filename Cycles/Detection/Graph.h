#ifndef GRAPH_H
#define GRAPH_H

#include <vector>

class Graph {
private:
    int V;
    std::vector<std::vector<int>> adj;

public:
    Graph(int V);
    void addEdge(int u, int v);
    const std::vector<std::vector<int>>& getAdjList() const;
    int getVertices() const;
};

#endif
