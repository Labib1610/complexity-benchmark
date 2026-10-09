import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    
    if t <= 1:
        print(0)
        return
        
    essential = list(map(int, data[idx:idx+t]))
    idx += t
    essential_set = set(essential)
    
    # Build adjacency list with weights
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((w, u, v))
    
    # Since the graph is a tree, we can use the fact that we need to find the minimal subtree
    # that connects all essential nodes - this is the Steiner tree on a tree.
    # For a tree, the solution is to find the minimal connected subgraph containing all terminals.
    # This can be done by finding the union of paths between all pairs of terminals,
    # or more efficiently, by finding the minimal subtree spanning all terminals.
    
    # Efficient approach:
    # 1. Root the tree at any node (e.g., node 1)
    # 2. Compute parent and depth for each node using BFS/DFS
    # 3. Implement LCA (Lowest Common Ancestor) to find distances
    # 4. The minimal cost is the sum of edges in the subtree that spans all essential nodes
    
    # However, there's a simpler way for trees:
    # The minimal cost to connect all essential nodes is the cost of the edges in the 
    # minimal connected subtree that includes all essential nodes.
    # This is equivalent to finding the union of all paths between essential nodes,
    # but since it's a tree, we can do better.
    
    # Key insight: In a tree, to connect k essential nodes, we need exactly k-1 paths.
    # But we're looking for the minimal subtree that connects all of them.
    
    # Simpler approach:
    # 1. Root the tree at node 1
    # 2. Do DFS to compute parent and depth
    # 3. For each essential node, mark its path to root
    # 4. Count how many times each edge is used in these paths
    # 5. The minimal subtree is the union of these paths
    
    # Actually, even simpler:
    # The answer is the sum of weights of edges in the minimal subtree connecting all essential nodes.
    # This is known as the Steiner tree problem on trees.
    # Algorithm:
    # 1. Root the tree at any node
    # 2. For each node, compute count of essential nodes in its subtree
    # 3. An edge contributes to the final cost if it separates essential nodes
    
    # Let's implement this:
    
    # Step 1: Root the tree at node 1 and compute parent relationships
    parent = [-1] * (n + 1)
    children = defaultdict(list)
    visited = [False] * (n + 1)
    
    # BFS to build rooted tree
    queue = deque([1])
    visited[1] = True
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                children[u].append((v, w))
                queue.append(v)
    
    # Step 2: Compute count of essential nodes in each subtree
    count_essential = [0] * (n + 1)
    essential_in_subtree = [0] * (n + 1)
    
    # Mark which nodes are essential
    is_essential = [False] * (n + 1)
    for node in essential:
        is_essential[node] = True
    
    # Post-order traversal to compute counts
    def dfs_count(u):
        count = 1 if is_essential[u] else 0
        for v, w in children[u]:
            count += dfs_count(v)
        essential_in_subtree[u] = count
        return count
    
    dfs_count(1)
    
    # Step 3: Sum up the weights of edges that connect different parts with essential nodes
    total_cost = 0
    def dfs_cost(u):
        nonlocal total_cost
        for v, w in children[u]:
            # If subtree of v has at least one essential node and not all essential nodes
            # then this edge should be included
            c = essential_in_subtree[v]
            if c > 0 and c < t:
                total_cost += w
            dfs_cost(v)
    
    dfs_cost(1)
    
    print(total_cost)

if __name__ == "__main__":
    main()