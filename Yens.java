import java.util.*;
public class Yens{
    static int INF=Integer.MAX_VALUE;
    public static void main(String[] args){

        int nodes = 100;
        int[][] graph = new int[nodes][nodes]; // Adjacency matrix representation
        for(int i = 0; i < nodes; i++) Arrays.fill(graph[i], INF);

        int[][] edges = {
            {0, 1, 5},   {0, 2, 8},   {1, 3, 7},   {2, 4, 3},   {3, 5, 6},
            {4, 6, 9},   {5, 7, 4},   {6, 8, 5},   {7, 9, 2},   {8, 10, 7},
            {9, 11, 1},  {10, 12, 8}, {11, 13, 3}, {12, 14, 6}, {13, 15, 9},
            {14, 16, 4}, {15, 17, 5}, {16, 18, 7}, {17, 19, 2}, {18, 20, 8},
            {19, 21, 6}, {20, 22, 5}, {21, 23, 3}, {22, 24, 9}, {23, 25, 7},
            {24, 26, 2}, {25, 27, 6}, {26, 28, 4}, {27, 29, 5}, {28, 30, 8},
            {29, 31, 3}, {30, 32, 6}, {31, 33, 7}, {32, 34, 5}, {33, 35, 2},
            {34, 36, 8}, {35, 37, 9}, {36, 38, 6}, {37, 39, 4}, {38, 40, 7},
            {39, 41, 3}, {40, 42, 5}, {41, 43, 6}, {42, 44, 2}, {43, 45, 7},
            {44, 46, 8}, {45, 47, 5}, {46, 48, 6}, {47, 49, 9}, {48, 50, 3},
            {49, 51, 7}, {50, 52, 5}, {51, 53, 6}, {52, 54, 8}, {53, 55, 9},
            {54, 56, 4}, {55, 57, 5}, {56, 58, 7}, {57, 59, 3}, {58, 60, 6},
            {59, 61, 2}, {60, 62, 8}, {61, 63, 9}, {62, 64, 5}, {63, 65, 7},
            {64, 66, 3}, {65, 67, 6}, {66, 68, 4}, {67, 69, 5}, {68, 70, 8},
            {69, 71, 3}, {70, 72, 6}, {71, 73, 7}, {72, 74, 5}, {73, 75, 2},
            {74, 76, 8}, {75, 77, 9}, {76, 78, 6}, {77, 79, 4}, {78, 80, 7},
            {79, 81, 3}, {80, 82, 5}, {81, 83, 6}, {82, 84, 2}, {83, 85, 7},
            {84, 86, 8}, {85, 87, 5}, {86, 88, 6}, {87, 89, 9}, {88, 90, 3},
            {89, 91, 7}, {90, 92, 5}, {91, 93, 6}, {92, 94, 8}, {93, 95, 9},
            {94, 96, 4}, {95, 97, 5}, {96, 98, 7}, {97, 99, 3}, {98, 99, 6},
            
            {0, 50, 10}, {1, 51, 9}, {2, 52, 8}, {3, 53, 7}, {4, 54, 6},
            {5, 55, 5}, {6, 56, 4}, {7, 57, 3}, {8, 58, 2}, {9, 59, 1},
            {10, 60, 10}, {11, 61, 9}, {12, 62, 8}, {13, 63, 7}, {14, 64, 6},
            {15, 65, 5}, {16, 66, 4}, {17, 67, 3}, {18, 68, 2}, {19, 69, 1},
            {20, 70, 10}, {21, 71, 9}, {22, 72, 8}, {23, 73, 7}, {24, 74, 6},
            {25, 75, 5}, {26, 76, 4}, {27, 77, 3}, {28, 78, 2}, {29, 79, 1},
            {30, 80, 10}, {31, 81, 9}, {32, 82, 8}, {33, 83, 7}, {34, 84, 6},
            {35, 85, 5}, {36, 86, 4}, {37, 87, 3}, {38, 88, 2}, {39, 89, 1},
            {40, 90, 10}, {41, 91, 9}, {42, 92, 8}, {43, 93, 7}, {44, 94, 6},
            {45, 95, 5}, {46, 96, 4}, {47, 97, 3}, {48, 98, 2}, {49, 99, 1},
            
            {25, 50, 6}, {35, 55, 7}, {45, 65, 8}, {55, 75, 9}, {65, 85, 10},
            {75, 95, 11}, {85, 99, 12}, {10, 85, 7}, {20, 95, 8}, {30, 99, 9}
        };

        int k = 10; // Find the 10 shortest paths
        int start = 0; // Start node
        int end = 99;  // Destination node



        for (int[] edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            graph[u][v] = w;
            graph[v][u] = w;
        }
        

        TreeSet<Dijkstra> pq=new TreeSet<>((a,b)->a.cost-b.cost);
        for(int[] edge:edges){
            graph[edge[0]][edge[1]]=INF;
            graph[edge[1]][edge[0]]=INF;

            Dijkstra dij=new Dijkstra(graph,start,end);
            pq.add(dij);
            graph[edge[0]][edge[1]]=edge[2];
            graph[edge[1]][edge[0]]=edge[2];
        }
        int one=1;
        System.out.println(pq);
    }
}
class Dijkstra{
    protected int cost;
    protected String path;
    protected int[][] graph;
    static int INF=Integer.MAX_VALUE;
    public Dijkstra(int[][] graph,int start,int end){
        this.graph=graph;
        simulate(start,end);
    }
    protected void simulate(int startNode, int endNode) {
        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a.cost));
        int[] distance = new int[this.graph.length];
        Arrays.fill(distance, INF);

        distance[startNode] = 0;
        pq.add(new Node(startNode, 0, ""));

        while (!pq.isEmpty()) {
            Node top = pq.poll();
            int node = top.id;
            int wt = top.cost;
            String seq = top.path + node + "->";

            if (node == endNode) {
                this.cost = wt;
                this.path = seq + "end";
                return;
            }

            for (int i = 0; i < this.graph.length; i++) {
                if (graph[node][i] != INF) {
                    int nextCost = graph[node][i];
                    if (distance[i] > distance[node] + nextCost) {
                        distance[i] = distance[node] + nextCost;
                        pq.add(new Node(i, distance[i], seq));
                    }
                }
            }
        }
    }
    @Override
    public int hashCode(){
        return Objects.hash(this.path,this.cost);
    }
    @Override
    public String toString(){
        return this.path+"\n costs:- "+this.cost+"\n";
    }
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Dijkstra dijkstra = (Dijkstra) obj;
        return cost == dijkstra.cost && Objects.equals(path, dijkstra.path);
    }
    static class Node {
        int id, cost;
        String path;

        Node(int id, int cost, String path) {
            this.id = id;
            this.cost = cost;
            this.path = path;
        }
    }
}
