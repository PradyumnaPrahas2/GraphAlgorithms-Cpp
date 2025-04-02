#include "BacktrackingDFS.h"

int main() {
    std::cout << "Multi-threaded Backtracking + DFS Algorithm:\n";
    
    int V = 10; // Petersen Graph has 10 vertices
    BacktrackingDFS graph(V);

    // Petersen Graph edges (10 vertices, 15 edges)
    int edges[][2] = {
        {0, 1}, {1, 2}, {2, 3}, {3, 4}, {4, 0}, // Outer pentagon
        {5, 6}, {6, 7}, {7, 8}, {8, 9}, {9, 5}, // Inner pentagon
        {0, 5}, {1, 6}, {2, 7}, {3, 8}, {4, 9}  // Connecting edges
    };

    // Add edges to the graph
    for (auto& edge : edges) {
        graph.addEdge(edge[0], edge[1]);
    }

    std::cout << "Graph generated with " << V << " vertices.\n";
    std::cout << "Finding cycles...\n";

    graph.findAllCycles();

    return 0;
}
