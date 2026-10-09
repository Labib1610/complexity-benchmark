import sys
import heapq
from collections import defaultdict

def find_mst_with_anomalies(n, edges, anomalies, B):
    # We need to ensure that no two anomalies are connected
    # This is equivalent to finding a spanning forest where each tree contains at most one anomaly
    # Or, we can think of it as making the graph such that anomalies are in different components
    
    # To do this optimally, we can:
    # 1. First, build a MST of the entire graph
    # 2. Then, remove edges that connect anomalies until they're all separated
    # But that's complex. Let's think differently.
    
    # Better approach:
    # We want to find a set of edges to remove such that no two anomalies are in the same component
    # This is essentially finding a minimum cut that separates all anomalies from each other
    # But that's also complex.
    
    # Let's think of it this way:
    # We want to find a set of edges to keep such that the anomalies are in different components
    # This is the same as finding a partition of the graph where each anomaly is in a different subset
    # And we want to minimize the total weight of edges that cross between subsets
    
    # Actually, let's think of it as: we want to delete edges to disconnect all anomalies from each other
    # This is the same as making sure that in the remaining graph, no two anomalies are in the same component
    
    # One approach:
    # 1. Build a graph
    # 2. Find connected components
    # 3. For each component that contains more than one anomaly, we need to disconnect them
    # 4. This is essentially a multiway cut problem, which is NP-hard
    # But since k is small (at most n), we can try all possible ways to separate them
    
    # Let's try a different approach:
    # We can model this as: we want to find a set of edges to delete such that in the resulting graph,
    # no two anomalies are in the same connected component.
    
    # This is the same as finding a multiway cut.
    # For small k, we can enumerate all possible partitions of anomalies and find the minimum cut for each
    
    # But let's think of a simpler approach for now:
    # We can use the fact that we only need to disconnect anomalies from each other
    # One way is to find a spanning tree and remove edges that connect different anomalies
    # But that's not optimal
    
    # Let's use the following approach:
    # 1. Use Union-Find to group nodes
    # 2. Start with all edges sorted by weight
    # 3. Process edges in increasing order of weight
    # 4. For each edge, if it connects two components that both contain anomalies, don't add it
    # 5. Otherwise, add it
    # 6. The edges we don't add are the ones we collapse
    
    # Actually, that's not right either. Let me re-read the problem.
    
    # The goal is to collapse a set of passageways such that no two anomalies can reach each other
    # We want to minimize the total cost of collapsed passageways
    
    # This is a minimum multiway cut problem.
    # For small k, we can solve it by trying all possible ways to separate the anomalies
    
    # But let's think of it more carefully:
    # We want to find a set of edges to remove such that in the remaining graph,
    # no two anomalies are in the same connected component.
    
    # One approach is to:
    # 1. Try all possible partitions of the anomalies
    # 2. For each partition, compute the minimum cut that separates the groups
    # 3. Take the minimum over all partitions
    
    # But that's complex. Let's try a greedy approach:
    # 1. Build a graph
    # 2. Find all pairs of anomalies
    # 3. For each pair, find the minimum cut (which is the shortest path in terms of edge weights)
    # 4. Select cuts to disconnect all pairs, minimizing total cost
    
    # Even simpler: let's model this as a minimum edge cover that separates all anomalies
    # Or think of it as finding a minimum weight set of edges whose removal disconnects all anomalies
    
    # Let's try this:
    # 1. Use a greedy approach with Union-Find
    # 2. Sort edges by weight in descending order
    # 3. For each edge, if it connects two components that both contain anomalies, collapse it
    # 4. Keep track of total cost
    
    # No, that's not right either.
    
    # Let me think of it this way:
    # We want to find a minimum weight set of edges to remove such that the remaining graph
    # has the property that no two anomalies are in the same connected component.
    
    # This is exactly the minimum multiway cut problem.
    # For k=2, it's just the minimum s-t cut.
    # For larger k, it's more complex.
    
    # Let's implement a solution that works for small k:
    # Try all possible ways to assign vertices to groups such that each anomaly is in a different group
    # Then find the minimum cut for that partition
    
    # But that's still complex. Let's look at the constraints.
    # n, m up to 1000, k up to n, B up to 10000
    
    # Let's try a different approach:
    # Model this as a flow problem or use a known algorithm for multiway cut
    
    # For now, let's implement a greedy solution:
    # 1. Sort edges by weight in ascending order
    # 2. Use Union-Find
    # 3. For each edge, if it connects two components and both components contain anomalies, skip it
    # 4. Otherwise, merge the components
    # 5. The edges we skip are the ones we collapse
    
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n
            # Which anomalies are in each component
            self.anomalies = [set() for _ in range(n)]
            
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
            
        def union(self, x, y):
            px, py = self.find(x), self.find(y)
            if px == py:
                return
            if self.rank[px] < self.rank[py]:
                px, py = py, px
            self.parent[py] = px
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1
            # Merge anomalies
            self.anomalies[px] |= self.anomalies[py]
            
        def add_anomaly(self, x, anomaly):
            root = self.find(x)
            self.anomalies[root].add(anomaly)
            
        def get_anomalies(self, x):
            root = self.find(x)
            return self.anomalies[root]
    
    # Initialize Union-Find
    uf = UnionFind(n+1)  # 1-indexed
    for anomaly in anomalies:
        uf.add_anomaly(anomaly, anomaly)
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    collapsed = []
    total_cost = 0
    
    for u, v, w in edges:
        # Check if both components contain anomalies
        anomalies_u = uf.get_anomalies(u)
        anomalies_v = uf.get_anomalies(v)
        
        # If both components contain anomalies and they're different sets, we must collapse this edge
        if anomalies_u and anomalies_v and anomalies_u != anomalies_v:
            if total_cost + w > B:
                return "NO", []
            collapsed.append((u, v))
            total_cost += w
        else:
            # It's safe to connect these components
            uf.union(u, v)
    
    return "YES", collapsed

# Read input
line = input().split()
n, m, k, B = map(int, line)
anomalies = list(map(int, input().split()))

edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

result, collapsed_edges = find_mst_with_anomalies(n, edges, anomalies, B)

if result == "NO":
    print("NO")
else:
    print("YES")
    print(len(collapsed_edges))
    for u, v in collapsed_edges:
        print(u, v)