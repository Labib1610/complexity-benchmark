import sys
import heapq
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    
    critical = set()
    for _ in range(t):
        critical.add(int(data[idx]) - 1)  # Convert to 0-based
        idx += 1
    
    # Build graph
    graph = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u = int(data[idx]) - 1
        idx += 1
        v = int(data[idx]) - 1
        idx += 1
        w = int(data[idx])
        idx += 1
        graph[u].append((v, w))
        graph[v].append((u, w))
        edges.append((w, u, v))
    
    # If there's only one or zero critical substations, cost is 0
    if len(critical) <= 1:
        print(0)
        return
    
    # Function to compute MST cost connecting all critical nodes using Steiner tree approach
    # We use a dynamic programming approach over subsets of critical nodes
    # State: dp[mask] = minimum cost to connect the subset of critical nodes represented by mask
    # We also maintain which nodes are connected in the component
    
    # Since t <= 10, we can use bitmasks up to 2^10 = 1024
    INF = float('inf')
    dp = [INF] * (1 << t)
    
    # Map each critical node to its index in the bitmask
    crit_list = list(critical)
    crit_index = {node: i for i, node in enumerate(crit_list)}
    
    # Precompute shortest paths from each node to all other nodes using Dijkstra
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
        pq = [(0, i)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[i][u]:
                continue
            for v, w in graph[u]:
                if dist[i][v] > d + w:
                    dist[i][v] = d + w
                    heapq.heappush(pq, (dist[i][v], v))
    
    # Initialize: for each critical node, the cost to connect just itself is 0
    # But we need to think of this differently. We want to find the minimum spanning tree
    # that connects all critical nodes, possibly using other nodes as Steiner points.
    
    # A better approach: for each subset of critical nodes, find the minimum cost to connect them
    # This is the Steiner tree problem, which can be solved with DP and MST
    
    # Let's use the Dreyfus-Wagner algorithm for Steiner tree
    # dp[mask][u] = minimum cost to connect the subset mask and also include node u
    # But to simplify, we'll compute for each subset of critical nodes, 
    # the minimum cost to connect them (as a tree), which is the Steiner tree weight
    
    # Actually, let's think of it this way:
    # We want the minimum cost to make all critical nodes connected.
    # This is exactly the Steiner tree problem.
    
    # For small t (<=10), we can solve it with DP over subsets.
    # Let dp[mask] = minimum cost to connect all nodes in the mask
    # We also need to track which actual nodes are used to connect them
    
    # But a simpler DP: 
    # dp[mask] = minimum cost to connect the subset of critical nodes in mask
    # To compute dp[mask], we split mask into two non-empty subsets s and mask^s
    # and take dp[s] + dp[mask^s] + cost of cheapest edge connecting them
    # But this requires computing the cost of connecting two subsets
    
    # Better approach:
    # 1. For each pair of critical nodes, compute the shortest path between them
    # 2. Create a complete graph on critical nodes with edge weights = shortest path
    # 3. Find MST of this complete graph
    
    # Compute all-pairs shortest paths only between critical nodes
    # Actually, compute shortest paths from each critical node to all nodes
    crit_dist = {}
    for c in critical:
        dist_c = [INF] * n
        dist_c[c] = 0
        pq = [(0, c)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist_c[u]:
                continue
            for v, w in graph[u]:
                if dist_c[v] > d + w:
                    dist_c[v] = d + w
                    heapq.heappush(pq, (dist_c[v], v))
        crit_dist[c] = dist_c
    
    # Now create a complete graph on critical nodes
    # Edge weight between c1 and c2 is the shortest path between them
    # This is the metric closure
    def steiner_tree_cost(critical_nodes):
        k = len(critical_nodes)
        if k <= 1:
            return 0
            
        # Create distance matrix for critical nodes
        dist_matrix = [[0]*k for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if i != j:
                    dist_matrix[i][j] = crit_dist[critical_nodes[i]][critical_nodes[j]]
        
        # Now find MST of this complete graph using Prim's or Kruskal's
        # Kruskal's algorithm
        edge_list = []
        for i in range(k):
            for j in range(i+1, k):
                edge_list.append((dist_matrix[i][j], i, j))
        edge_list.sort()
        
        parent = list(range(k))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
                return True
            return False
        
        cost = 0
        edges_used = 0
        for w, u, v in edge_list:
            if union(u, v):
                cost += w
                edges_used += 1
                if edges_used == k - 1:
                    break
        return cost
    
    # The answer is the cost of the Steiner tree on the critical nodes
    result = steiner_tree_cost(crit_list)
    print(result)

if __name__ == "__main__":
    main()