#ifndef BFS_CYCLE_H
#define BFS_CYCLE_H

#include "Graph.h"
#include <vector>
#include <queue>

class BFS_Cycle {
public:
    bool detectCycle(const Graph& graph);
};

#endif