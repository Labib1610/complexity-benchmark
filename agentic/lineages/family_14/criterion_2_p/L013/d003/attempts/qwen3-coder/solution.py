import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, t = map(int, sys.stdin.readline().split())
    priorities = set(map(int, sys.stdin.readline().split()))
    
    # Since m = n - 1 and it's minimally connected, it's a tree
    graph = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
        edges.append((u, v, w))
    
    # If there's only one priority language, cost is 0
    if t <= 1:
        print(0)
        return
    
    # We need to find the minimal subtree that connects all priority nodes
    # This is the Steiner tree problem on a tree, which can be solved efficiently
    
    # Approach:
    # 1. Build a virtual tree (also called auxiliary tree) that contains only the priority nodes
    #    and their lowest common ancestors.
    # 2. The minimal cost is the sum of weights of edges in this virtual tree.
    
    # However, since the original graph is a tree, we can use the following approach:
    # Find the minimal connected subgraph containing all priority nodes.
    # This is equivalent to finding the union of paths between all pairs,
    # but more efficiently: we can find the minimal subtree spanning all priority nodes.
    
    # Efficient algorithm for Steiner tree on a tree:
    # 1. Root the tree at any node.
    # 2. For each priority node, mark its ancestors.
    # 3. The minimal subtree includes all nodes that lie on paths between any two priority nodes.
    # But even simpler: we can use the fact that in a tree, the minimal connected subgraph
    # containing a set of nodes is the union of paths between them.
    # A simpler way: find the "closure" of priority nodes under ancestor relationship.
    
    # Even simpler approach:
    # Since it's a tree, we can find the minimal subtree by:
    # 1. Pick any priority node as root
    # 2. Do BFS/DFS to compute parent and depth for all nodes
    # 3. Find the minimal connected component containing all priority nodes
    
    # Let's implement a clean solution:
    # We'll build the minimal subtree connecting all priority nodes.
    # In a tree, this is unique and can be found by:
    # 1. Rooting the tree
    # 2. Finding all nodes that are on paths between priority nodes
    
    # Simpler idea:
    # Use Union-Find with Kruskal-like approach but since it's already a tree,
    # we just need to find which edges are needed.
    
    # Best approach:
    # Since the graph is a tree, the minimal cost to connect all priority nodes
    # is the cost of the edges in the minimal subtree that spans all priority nodes.
    # This is known as the Steiner tree problem on trees.
    
    # Algorithm:
    # 1. Root the tree at an arbitrary node
    # 2. Compute parent and depth for each node via DFS
    # 3. Compute LCA data structure (but might be overkill)
    # 4. Instead, we can do: 
    #    - Mark all nodes that are on paths between priority nodes
    #    - An edge is needed if it separates priority nodes
    
    # Simpler yet:
    # Since it's a tree, we can do the following:
    # 1. Root the tree at node 1
    # 2. Compute parent and depth for each node
    # 3. For each edge, check if removing it disconnects priority nodes
    #    But this is O(m * t) which might be too slow
    
    # Optimal approach:
    # Build the "auxiliary tree" or "Steiner tree" on the original tree:
    # 1. Sort priority nodes by DFS time
    # 2. Take consecutive pairs (in DFS order) and include their path
    # 3. The total weight is what we want
    
    # Implementation:
    parent = [-1] * (n + 1)
    depth = [0] * (n + 1)
    visited = [False] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Root the tree at node 1
    def dfs(u, p, d):
        parent[u] = p
        depth[u] = d
        for v, w in adj[u]:
            if v != p:
                dfs(v, u, d + 1)
                
    dfs(1, -1, 0)
    
    # Function to find path weight between two nodes
    def path_cost(a, b):
        cost = 0
        # Bring both nodes to same depth
        while depth[a] > depth[b]:
            for v, w in adj[a]:
                if v == parent[a]:
                    cost += w
                    break
            a = parent[a]
        while depth[b] > depth[a]:
            for v, w in adj[b]:
                if v == parent[b]:
                    cost += w
                    break
            b = parent[b]
        # Now bring both up until they meet
        while a != b:
            for v, w in adj[a]:
                if v == parent[a]:
                    cost += w
                    break
            for v, w in adj[b]:
                if v == parent[b]:
                    cost += w
                    break
            a = parent[a]
            b = parent[b]
        return cost
    
    # If there's only one priority, cost is 0
    if len(priorities) <= 1:
        print(0)
        return
        
    # Convert to list and sort
    pri_list = sorted(list(priorities))
    
    # Sum of costs between consecutive priority nodes in sorted order gives the MST cost
    # This works because in a tree, sorting by DFS entry time and taking edges between 
    # consecutive nodes gives the minimal subtree
    total = 0
    for i in range(len(pri_list) - 1):
        # Need to compute actual path cost in the tree
        # But let's think differently
        
        # Actually, let's use Union-Find to simulate Kruskal on the original tree edges
        # Since the edges are part of a tree, we process them in order of inclusion in final MST
        
        # No, let's go back to the right approach:
        # In a tree, to connect k nodes optimally, we can:
        # 1. Sort the nodes according to a DFS traversal
        # 2. For every two consecutive nodes in this order, add the path between them
        # 3. The total cost is the answer
        
        # But computing path costs individually is complex. Let's try another way.
        
        # Key insight: In the auxiliary tree approach:
        # 1. Sort priority nodes by DFS time
        # 2. Answer = (sum of pairwise distances) / 2
        # But that's not right either.
        
        # Correct approach:
        # 1. Root the tree
        # 2. For each edge, count how many priority nodes are on each side
        # 3. If one side has k priority nodes, the other has (t-k), then this edge contributes to the final cost
        
    # Let's implement the correct counting approach:
    
    # Re-root at node 1
    # Compute subtree sizes for priority nodes
    
    subtree_count = [0] * (n + 1)
    pri_set = set(priorities)
    
    # DFS to compute number of priority nodes in each subtree
    def dfs_count(u, parent_node):
        count = 1 if u in pri_set else 0
        for v, w in adj[u]:
            if v != parent_node:
                count += dfs_count(v, u)
        subtree_count[u] = count
        return count
    
    dfs_count(1, -1)
    
    # Now for each edge, determine its contribution
    total_cost = 0
    visited_edges = set()
    
    # For each edge in the original tree, check if it should be included
    for u, v, w in edges:
        # Determine which direction the edge goes in rooted tree
        if parent[u] == v:
            # Edge from u to its parent v
            # Cut separates subtree of u from rest
            cut_size = subtree_count[u]
        elif parent[v] == u:
            # Edge from v to its parent u  
            # Cut separates subtree of v from rest
            cut_size = subtree_count[v]
        else:
            # Should not happen in a tree
            continue
            
        # If cut_size is between 1 and t-1, then this edge is in the minimal Steiner tree
        if 0 < cut_size < t:
            total_cost += w
    
    print(total_cost)

if __name__ == "__main__":
    main()