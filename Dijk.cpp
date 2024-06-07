#include<iostream>
#include<list>
#include<vector>
#include<stack>
#include<queue>
#include<algorithm>
#include<climits>
using namespace std;
class Graph{
    public:
    int n;
    vector<vector<int>>graph;
    vector<vector<int>>weights;
    Graph(int s){
        this->n=s;
        graph.resize(n);
        weights.resize(n);
        for(int i=0;i<n;i++){
            weights[i].resize(n,100000);
        }
    }
    void addEgde(int i,int j,int w){
        graph[i].push_back(j);
        weights[i][j]=w;
    }
    vector<int> getweight(int i){
        return weights[i];
    }
    void compute(vector<int>&arr,vector<bool>&selected){
        if(count(selected.begin(),selected.end(),true)==selected.size()){
            return;
        }
        for(int i=0;i<selected.size();i++){
            if(selected[i]==true){
                int x=arr[i];
                vector<int>duplicate;
                duplicate=getweight(i);
                // cout<<"Weight achieved"<<endl;
                for(int j=0;j<arr.size();j++){
                    if(selected[j]==false){
                        if(arr[j]>x+duplicate[j]){
                            arr[j]=x+duplicate[j];
                        }
                    }
                }
            }
        }
        // for(int val:arr){
        // cout<<val<<" ";
        // }
        int index=0,min_val=100000;
        for(int i=0;i<arr.size();i++){
            if(selected[i]==false){
            if(arr[i]<min_val){
                min_val=arr[i];
                index=i;
            }
            }
        }
        if(index==0){
            cout<<"Nothing selected infinite loop encountered!"<<endl;
            return;
        }
        selected[index]=true;
        cout<<"Selected index "<<index<<" with value"<<arr[index]<<endl;
        // compute(arr,selected);
    }
};
int main(){
    int n=3,i=0;
    Graph g(n);
    g.addEgde(0,1,20);
    g.addEgde(1,0,20);
    // g.addEgde(1,3,40);
    // g.addEgde(3,0,10);
    // g.addEgde(3,4,5);
    // g.addEgde(2,4,65);
    vector<int>arr(n,100000);
    cout<<"Enter source vertex:- i=0\n";
    // cin>>i;
    arr[i]=0;
    vector<bool>selected(n,false);
    selected[i]=true;
    g.compute(arr,selected);
    g.compute(arr,selected);
    g.compute(arr,selected);
    for(int val:arr){
        cout<<val<<" ";
    }
}