#include<iostream>
#include<list>
#include<unordered_map>
#include<vector>
#include<climits>
using namespace std;
class Graph{
    protected:
    int si;
    vector<vector<int>>graph;
    vector<int>indegree;
    vector<bool>visited;
    public:
        vector<int>Topo;
    Graph(int s){
        this->si=s;
        graph.resize(s);
        indegree.resize(s,0);
        visited.resize(s,false);
    }
    void addEdge(int i,int j){
        graph[i].push_back(j);
        indegree[j]++;
    }
    void TopoSort(){
        if(Topo.size()==si){
            cout<<"TopoSort() completed"<<endl;
            return;
        }
        int MINIMUM=INT_MAX;
        int target=-1;
        for(int i=0;i<si;i++){
            if(indegree[i]<MINIMUM && visited[i]==false){
                MINIMUM=indegree[i];
                target=i;
            }
        }
        if(target==-1){
            cout<<"Error occured in TopoSort() function"<<endl;
            return;
        }
        visited[target]=true;
        for(int v:graph[target]){
            indegree[v]--;
        }
        Topo.push_back(target);
        TopoSort();
    }
};
int main(){
    Graph g(8);
    g.addEdge(7,6);
    g.addEdge(7,5);
    g.addEdge(6,4);
    g.addEdge(5,4);
    g.addEdge(5,2);
    g.addEdge(2,1);
    g.addEdge(6,3);
    g.addEdge(3,1);
    g.addEdge(1,0);
    g.TopoSort();
    for(int i:g.Topo){
        cout<<i<<" ";
    }
}