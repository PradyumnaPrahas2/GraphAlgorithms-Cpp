#include "BacktrackingDFS.h"

BacktrackingDFS::BacktrackingDFS(int V) {
    this->V = V;
    adj.resize(V);
}

void BacktrackingDFS::addEdge(int u, int v) {
    adj[u].push_back(v);
    adj[v].push_back(u); // Since the graph is undirected
}

void BacktrackingDFS::dfs(int node, int parent, std::unordered_set<int>& visited, std::vector<int>& path) {
    visited.insert(node);
    path.push_back(node);

    for (int neighbor : adj[node]) {
        if (neighbor == parent) continue; // Ignore edge to parent
        if (visited.count(neighbor)) {
            // Cycle detected
            auto it = std::find(path.begin(), path.end(), neighbor);
            if (it != path.end()) {
                std::vector<int> cycle(it, path.end());
                std::sort(cycle.begin(), cycle.end()); // Normalize cycle
                
                std::lock_guard<std::mutex> lock(mtx);
                uniqueCycles.insert(cycle);
            }
        } else {
            dfs(neighbor, node, visited, path);
        }
    }

    // Backtrack
    path.pop_back();
    visited.erase(node);
}

void BacktrackingDFS::findAllCycles() {
    std::vector<std::thread> threads;
    std::unordered_set<int> visited;

    for (int i = 0; i < V; i++) {
        threads.emplace_back([this, i]() {
            std::unordered_set<int> visited_local;
            std::vector<int> path;
            this->dfs(i, -1, visited_local, path);
        });
    }

    for (auto& thread : threads) {
        thread.join();
    }

    // Print all unique cycles
    for (const auto& cycle : uniqueCycles) {
        for (int node : cycle) {
            std::cout << node << " ";
        }
        std::cout << std::endl;
    }
}
