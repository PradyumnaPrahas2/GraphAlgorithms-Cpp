#include "Graph.h"
#include "DSU_Cycle.h"
#include "DFS_Cycle.h"
#include "VertexColoring_Cycle.h"
#include "Tarjan_Cycle.h"
#include "BFS_Cycle.h"
#include<iostream>
using namespace std;
int main() {
    int V = 6;
    Graph graph(V);

    graph.addEdge(0, 1);
    graph.addEdge(1, 2);
    graph.addEdge(2, 3);
    graph.addEdge(3, 4);
    graph.addEdge(4, 5);
    graph.addEdge(5, 1); 

    DSU_Cycle dsuCycle(V);
    std::cout << "Cycle detected using DSU: " << (dsuCycle.detectCycle(graph) ? "Yes" : "No") << std::endl;

    DFS_Cycle dfsCycle;
    std::cout << "Cycle detected using DFS: " << (dfsCycle.detectCycle(graph) ? "Yes" : "No") << std::endl;

    VertexColoring_Cycle vertexColoring;
    std::cout << "Cycle detected using Vertex Coloring: " << (vertexColoring.detectCycle(graph) ? "Yes" : "No") << std::endl;

    Tarjan_Cycle tarjan;
    std::cout << "Cycle detected using Tarjan's SCC: " << (tarjan.detectCycle(graph) ? "Yes" : "No") << std::endl;

    BFS_Cycle bfsCycle;
    std::cout << "Cycle detected using BFS: " << (bfsCycle.detectCycle(graph) ? "Yes" : "No") << std::endl;

    return 0;
}
