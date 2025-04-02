#ifndef TARJAN_CYCLE_H
#define TARJAN_CYCLE_H

#include "Graph.h"
#include <vector>
#include <stack>

class Tarjan_Cycle {
private:
    int timer;
    std::vector<int> disc, low;
    std::vector<bool> onStack;
    std::stack<int> sccStack;

    void tarjanDFS(int node, const Graph& graph, bool &hasCycle);

public:
    bool detectCycle(const Graph& graph);
};

#endif
