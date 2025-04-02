#ifndef DFS_CYCLE_H
#define DFS_CYCLE_H

#include "Graph.h"
#include <vector>

class DFS_Cycle {
private:
    bool dfs(int node, int parent, std::vector<bool>& visited, const Graph& graph);

public:
    bool detectCycle(const Graph& graph);
};

#endif
