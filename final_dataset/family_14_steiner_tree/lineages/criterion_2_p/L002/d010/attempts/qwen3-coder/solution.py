import sys
from collections import defaultdict
import heapq

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find(parent, x), find(parent, y)
    if px == py:
        return False
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1
    return True

def main():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    
    critical = list(map(int, data[idx:idx+t]))
    idx += t
    
    edges = []
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((w, u, v))
    
    if t <= 1:
        print(0)
        return
    
    # We need to connect all critical variables with minimum cost
    # This is a Minimum Spanning Tree problem on the critical variables
    # But we're working with a graph that has n nodes and m=n-1 edges forming a tree
    
    # Since the full set forms a tree (m=n-1 edges, full row rank), 
    # we can consider the structure as a tree.
    
    # To make all critical variables equal, we need to connect them in the tree.
    # The minimum cost is the cost of the minimum spanning tree that connects all critical nodes.
    # This is equivalent to finding the Steiner tree for the critical nodes.
    
    # However, since the underlying graph is a tree, the Steiner tree is just the 
    # union of paths between the critical nodes, but we only pay for edges once.
    
    # Better approach:
    # In a tree, to connect a set of nodes, we need the minimal subtree that spans them.
    # The cost is the sum of edge weights in that subtree.
    
    # Algorithm:
    # 1. Build the tree from all edges
    # 2. Find the minimal subtree that connects all critical vertices
    # 3. This is the Steiner tree on a tree, which can be found by:
    #    - Finding the subtree induced by critical nodes
    #    - Taking all edges in the paths between critical nodes, but count each edge only once
    
    # Simpler approach for trees:
    # The minimum cost to connect a set of nodes in a tree is the cost of the 
    # edges in the subtree formed by the union of all paths between pairs of critical nodes.
    # But there's an even simpler way:
    # In a tree, the minimum cost to connect a set of terminal nodes is found by:
    # 1. Root the tree at some node
    # 2. For each node, compute if it's needed (is critical or has a critical descendant)
    # 3. Take all edges from root to critical nodes, but avoid double counting
    
    # Even simpler: 
    # The optimal solution is the MST of the complete graph where edge weights are 
    # shortest path distances between critical nodes in the original tree.
    # But since the original graph is a tree, we can do better.
    
    # Correct approach:
    # In a tree, to connect a set of terminals (critical nodes), 
    # we need exactly those edges that lie on paths between any pair of terminals.
    # This forms a subtree, and its total weight is what we want.
    
    # Efficient algorithm:
    # 1. Root the tree at an arbitrary node
    # 2. For each node, determine if it's critical or if any of its subtrees contain a critical node
    # 3. An edge should be included if it leads to a subtree containing a critical node,
    #    and that subtree contains at least one critical node not in other branches
    
    # Actually, there's a known result:
    # For a tree with edge weights and a set of terminal nodes,
    # the minimum cost to connect all terminals is the sum of weights of edges
    # such that removing the edge separates the tree into components, each containing
    # at least one terminal.
    
    # Algorithm:
    # 1. Root the tree arbitrarily
    # 2. Do a post-order traversal
    # 3. For each node, count how many critical nodes are in its subtree
    # 4. Include an edge if both endpoints' subtrees contain at least one critical node
    
    # Build adjacency list representation of the tree
    adj = defaultdict(list)
    edge_map = {}
    for i in range(m):
        w, u, v = edges[i]
        adj[u].append((v, w, i))
        adj[v].append((u, w, i))
        edge_map[i] = (u, v, w)
    
    # Convert critical to a set for fast lookup
    critical_set = set(critical)
    
    # Root the tree at node 1 (or any node)
    root = 1
    
    # Store edges with their weights
    edge_list = [(w, u, v) for w, u, v in edges]
    
    # If there's only one critical node, cost is 0
    if len(critical_set) <= 1:
        print(0)
        return
    
    # Build tree structure with DFS
    parent_edge = [-1] * (n + 1)  # parent_edge[u] = index of edge connecting u to its parent
    parent_node = [0] * (n + 1)   # parent_node[u] = parent of u
    children = defaultdict(list)
    
    visited = [False] * (n + 1)
    stack = [root]
    visited[root] = True
    
    while stack:
        u = stack.pop()
        for v, w, edge_idx in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent_node[v] = u
                parent_edge[v] = edge_idx
                children[u].append(v)
                stack.append(v)
    
    # Count critical nodes in each subtree
    subtree_critical_count = [0] * (n + 1)
    
    # Mark which nodes are critical
    is_critical = [0] * (n + 1)
    for c in critical:
        is_critical[c] = 1
    
    # Post-order traversal to compute subtree counts
    def dfs(u):
        count = is_critical[u]
        for v in children[u]:
            count += dfs(v)
        subtree_critical_count[u] = count
        return count
    
    dfs(root)
    
    # Calculate total cost
    total_cost = 0
    # For each edge, check if it should be included
    for i in range(m):
        u, v, w = edge_map[i]
        # Determine which one is the parent in the rooted tree
        if parent_node[u] == v:
            child = u
        elif parent_node[v] == u:
            child = v
        else:
            # Should not happen in a tree
            continue
            
        # Edge from parent_node[child] to child
        # This edge is needed if subtree rooted at child contains at least one critical
        # and also excludes at least one critical (so removal disconnects)
        count_in_subtree = subtree_critical_count[child]
        count_out_subtree = len(critical) - count_in_subtree
        
        if count_in_subtree > 0 and count_out_subtree > 0:
            total_cost += w
    
    print(total_cost)

if __name__ == "__main__":
    main()