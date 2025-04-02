#ifndef BACKTRACKING_DFS_H
#define BACKTRACKING_DFS_H

#include <iostream>
#include <vector>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <mutex>
#include <thread>

class BacktrackingDFS {
private:
    int V;  // Number of vertices
    std::vector<std::vector<int>> adj; // Adjacency list
    std::set<std::vector<int>> uniqueCycles;
    std::mutex mtx; // Mutex for thread safety

    void dfs(int node, int parent, std::unordered_set<int>& visited, std::vector<int>& path);

public:
    BacktrackingDFS(int V);
    void addEdge(int u, int v);
    void findAllCycles();
};

#endif
