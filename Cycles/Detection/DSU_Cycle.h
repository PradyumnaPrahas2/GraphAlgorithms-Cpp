#ifndef DSU_CYCLE_H
#define DSU_CYCLE_H

#include "Graph.h"
#include <vector>

class DSU_Cycle {
private:
    std::vector<int> parent, rank;
    int find(int node);
    void unionSets(int u, int v);

public:
    DSU_Cycle(int V);
    bool detectCycle(const Graph& graph);
};

#endif
