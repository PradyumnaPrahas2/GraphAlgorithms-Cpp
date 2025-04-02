#ifndef VERTEXCOLORING_CYCLE_H
#define VERTEXCOLORING_CYCLE_H

#include "Graph.h"
#include <vector>

class VertexColoring_Cycle {
private:
    bool dfs(int node, std::vector<int>& color, const Graph& graph);

public:
    bool detectCycle(const Graph& graph);
};

#endif
