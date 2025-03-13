import java.util.*;
public class Tarjan {
    static int time=0;
    static List<List<Integer>> scc=new ArrayList<>();
    static void dfs(HashMap<Integer,List<Integer>> graph,int src,int[] dfs_high,int[] dfs_low,boolean[] visited,Stack<Integer> st){
        dfs_high[src]=time;
        dfs_low[src]=time;
        time++;

        visited[src]=true;

        st.add(src);

        for(int child:graph.getOrDefault(src,new ArrayList<>())){
            if(dfs_high[child]==-1){
                dfs(graph,child,dfs_high,dfs_low,visited,st);
                dfs_low[src]=Math.min(dfs_low[src],dfs_low[child]);
            }
            else if(visited[child]==true){
                dfs_low[src]=Math.min(dfs_low[src],dfs_high[child]);
            }
        }

        if(dfs_low[src]==dfs_high[src]){ // head of the tree
            List<Integer> component=new ArrayList<>();
            while(!st.isEmpty()){
                int node=st.pop();
                visited[node]=false;
                component.add(node);

                if(node==src) break;
            }
            scc.add(component);
        }
    }
    static List<List<Integer>> tarjan(int nodes,HashMap<Integer,List<Integer>> graph){

        int[] dfs_high=new int[nodes];
        int[] dfs_low=new int[nodes];

        Arrays.fill(dfs_high,-1);
        Arrays.fill(dfs_low,-1);

        boolean[] visited=new boolean[nodes];
        Stack<Integer> st=new Stack<>();

        for(int i=0;i<nodes;i++){
            if(dfs_high[i]==-1){
                dfs(graph,i,dfs_high,dfs_low,visited,st);
            }
        }

        return scc;
    }
    public static void main(String[] args){
        int nodes=5;
        int[][] edges={{0,1},{1,2},{2,3},{2,4},{3,0},{4,2}};

        HashMap<Integer,List<Integer>> graph=new HashMap<>();

        for(int[] e:edges){
            graph.putIfAbsent(e[0],new ArrayList<>());
            graph.get(e[0]).add(e[1]);
        }

        System.out.println(tarjan(nodes,graph));
    }
}
