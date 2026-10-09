import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    t = int(data[2])
    
    required = set(map(int, data[3:3+t]))
    
    # If there's only one required site, cost is 0
    if t <= 1:
        print(0)
        return
    
    # Build adjacency list for the tree
    adj = [[] for _ in range(n + 1)]
    edges = []
    index = 3 + t
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        w = int(data[index + 2])
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((w, u, v))
        index += 3
    
    # If all required nodes are the same (shouldn't happen per constraints), cost is 0
    if len(required) <= 1:
        print(0)
        return
        
    # Find the minimal subtree connecting all required nodes (Steiner tree in a tree)
    # In a tree, the minimal Steiner tree is the union of paths between required nodes
    # But we can compute it more efficiently:
    # The cost is the sum of edge weights in the minimal subtree spanning all required nodes
    
    # Approach: 
    # 1. Root the tree at any node (say node 1)
    # 2. Compute for each node whether its subtree contains any required node
    # 3. An edge is part of the minimal Steiner tree if it connects two components,
    #    each containing at least one required node
    
    # Let's use a different approach:
    # Since it's a tree, we can find the minimal subtree that connects all required nodes
    # by finding the union of all paths between required nodes.
    # But there's a simpler way: 
    # The minimal Steiner tree in a tree is obtained by taking the union of paths
    # between consecutive required nodes in some order.
    # However, even simpler: we can do a BFS/DFS from one required node to find distances
    # to others, but that's not directly helpful.
    
    # Best approach for tree:
    # 1. Root the tree at a required node (or any node)
    # 2. For each node, compute if its subtree contains any required node
    # 3. Count how many required nodes are in each subtree
    # 4. An edge contributes to the final cost if it separates required nodes
    
    # Let's root at node 1
    parent = [-1] * (n + 1)
    children = [[] for _ in range(n + 1)]
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
    
    # Now compute for each node, how many required nodes are in its subtree
    subtree_required_count = [0] * (n + 1)
    
    # Post-order traversal to count required nodes in subtrees
    def dfs_count(node):
        count = 1 if node in required else 0
        for child, weight in children[node]:
            count += dfs_count(child)
        subtree_required_count[node] = count
        return count
    
    dfs_count(1)
    
    # Now traverse the tree again and sum up edge weights where the edge
    # connects a subtree with >0 and <t required nodes
    total_cost = 0
    
    def dfs_cost(node):
        nonlocal total_cost
        for child, weight in children[node]:
            # The edge from 'node' to 'child' is included if:
            # - the subtree of 'child' has at least 1 required node, AND
            # - the subtree of 'child' doesn't have ALL required nodes
            if subtree_required_count[child] > 0 and subtree_required_count[child] < t:
                total_cost += weight
            dfs_cost(child)
                
    dfs_cost(1)
    print(total_cost)

if __name__ == "__main__":
    main()