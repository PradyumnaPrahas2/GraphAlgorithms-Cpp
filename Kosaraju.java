import java.util.*;
public class Kosaraju {
    static void dfs(HashMap<Integer,List<Integer>> graph,int n,boolean[] visited,List<Integer> order){
        if(visited[n]) return;

        visited[n]=true;

        
        for(int child:graph.getOrDefault(n,new ArrayList<>())){
            dfs(graph,child,visited,order);
        }
        order.add(n);
    }
    
    static HashMap<Integer,List<Integer>> transpose(HashMap<Integer,List<Integer>> graph,int nodes){
        HashMap<Integer,List<Integer>> modifiedGraph=new HashMap<>();

        for(int i=0;i<nodes;i++){
            for(int child:graph.getOrDefault(i,new ArrayList<>())){
                modifiedGraph.putIfAbsent(child,new ArrayList<>());

                modifiedGraph.get(child).add(i);
            }
        }
        return modifiedGraph;
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int nodes=8;
        int[][] edges={{0,1},{1,2},{2,3},{3,2},{3,7},{7,3},{2,6},{7,6},{5,6},{6,5},{1,5},{4,5},{4,0},{1,4}};
        HashMap<Integer,List<Integer>> graph=new HashMap<>();

        for(int i=0;i<edges.length;i++){
            int src=edges[i][0];
            int dstn=edges[i][1];

            graph.putIfAbsent(src,new ArrayList<>());
            graph.get(src).add(dstn);
        }

        //Step 1 DFS

        List<Integer> order=new ArrayList<>();
        boolean[] visited=new boolean[nodes];

        for(int i=0;i<nodes;i++){
            if(!visited[i]){
                dfs(graph,i,visited,order);
            }
        }

        // System.out.println(order); // Print dfs order
        // System.out.println("Original Graph "+graph);

        graph=transpose(graph,nodes);

        Collections.reverse(order);

        // System.out.print("Modified Graph "+graph);
        visited = new boolean[nodes];

        List<List<Integer>> scc=new ArrayList<>();

        for(int node:order){
            if(!visited[node]){
                List<Integer> component=new ArrayList<>();
                dfs(graph,node,visited,component);
                scc.add(component);
            }
        }

        System.out.println("Strongly Connected Components are:-");
        System.out.println(scc);
    }
}
