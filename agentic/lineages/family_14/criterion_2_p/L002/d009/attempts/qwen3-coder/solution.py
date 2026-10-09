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

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    critical = set(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    
    # Sort edges by weight
    edges.sort()
    
    # First, find MST of the entire graph
    parent_full = list(range(n + 1))
    rank_full = [0] * (n + 1)
    mst_edges = []
    
    for w, u, v in edges:
        if union(parent_full, rank_full, u, v):
            mst_edges.append((w, u, v))
    
    # Now we need to find the minimum cost to connect all critical nodes
    # This is equivalent to finding the MST of the critical nodes only
    # We can use the fact that the full MST has weight equal to sum of all edge weights in it
    
    # But we want the minimum cost to connect all critical vertices
    # This is the Steiner tree problem, but since the graph is a tree, 
    # we can solve it efficiently
    
    # In a tree, to connect a subset of nodes, we need to activate edges 
    # on the paths between them in the tree
    
    # Build adjacency list for the MST
    adj = defaultdict(list)
    for w, u, v in mst_edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Find the subtree that spans all critical nodes
    # We can do this by finding all edges in the tree that lie on paths between critical nodes
    
    # First, let's root the tree at an arbitrary node
    def dfs(node, parent_node):
        visited.add(node)
        subtree_critical = node in critical
        for neighbor, weight in adj[node]:
            if neighbor != parent_node and neighbor not in visited:
                child_critical = dfs(neighbor, node)
                if child_critical:
                    subtree_critical = True
                    # This edge is needed
                    needed_edges.append(weight)
        return subtree_critical
    
    # Alternative approach: 
    # Since we have a tree and want to connect all critical nodes,
    # we need to find the minimal subtree containing all critical nodes
    
    # This is the Steiner tree for a tree, which can be found by:
    # 1. Root the tree at some node
    # 2. For each node, compute if its subtree contains any critical node
    # 3. An edge is needed if it connects two subtrees both containing critical nodes
    
    if len(critical) == 1:
        print(0)
        return
    
    # Use a different approach:
    # In the MST, find the unique path between every pair of critical nodes
    # Union all these paths - this gives us the minimum set of edges needed
    
    # Actually, there's a simpler way for trees:
    # The minimum cost to connect all critical nodes in a tree is the 
    # total weight of edges in the "Steiner tree" which is just the union
    # of paths between critical nodes
    
    # Even simpler approach:
    # In a tree, to connect k critical nodes, we need exactly k-1 edges
    # But which edges? Those that form the minimal subtree containing all critical nodes
    
    # Algorithm:
    # 1. Root the tree at some node
    # 2. For each node, calculate if its subtree contains any critical node
    # 3. An edge {u,v} where v is child of u is needed iff both u's subtree 
    #    (including u) and v's subtree contain critical nodes
    
    # Let's implement this properly
    
    # Build parent relationships for rooted tree
    children = defaultdict(list)
    parent_edge_weight = [0] * (n + 1)
    parent_of = [0] * (n + 1)
    
    # Root at node 1
    def build_tree_dfs(node, parent_node, weight_from_parent):
        parent_of[node] = parent_node
        parent_edge_weight[node] = weight_from_parent
        for neighbor, weight in adj[node]:
            if neighbor != parent_node:
                children[node].append((neighbor, weight))
                build_tree_dfs(neighbor, node, weight)
    
    build_tree_dfs(1, 0, 0)
    
    # For each node, determine if its subtree contains any critical node
    contains_critical = [False] * (n + 1)
    
    def mark_critical_subtree(node):
        if node in critical:
            contains_critical[node] = True
        for child, _ in children[node]:
            mark_critical_subtree(child)
            if contains_critical[child]:
                contains_critical[node] = True
    
    mark_critical_subtree(1)
    
    # Now collect edges that are needed
    total_cost = 0
    
    def collect_needed_edges(node):
        nonlocal total_cost
        for child, weight in children[node]:
            collect_needed_edges(child)
            # Edge from node to child is needed if:
            # 1. Child's subtree contains at least one critical node
            # 2. Node's subtree (when excluding child's subtree) also contains a critical node
            #    OR node itself is critical
            
            if contains_critical[child]:
                # Check if there's another critical node outside child's subtree
                # This is complex, so let's use a cleaner approach
                
                # Simpler: reroot and count
                total_cost += weight
    
    # Cleaner approach:
    # Reroot the tree conceptually and count edges in the minimal subtree spanning critical nodes
    
    # In a tree, the minimum subtree connecting a set of nodes S has cost equal to
    # sum of weights of edges {u,v} such that both components of T-{u,v} contain nodes from S
    
    # Even simpler: 
    # Use the fact that in the unique path between any two critical nodes,
    # all edges must be included. The union of all such paths is what we need.
    
    # But there's an even cleaner way for trees:
    # Root the tree, then for each edge e={u,v}, let T1, T2 be the two components of T-e
    # Edge e is needed iff both T1 and T2 contain at least one critical node
    
    # So we need to count for each edge how many critical nodes are in each side
    
    # Compute number of critical nodes in each subtree
    crit_count = [0] * (n + 1)
    
    def count_critical_subtree(node):
        count = 1 if node in critical else 0
        for child, _ in children[node]:
            count += count_critical_subtree(child)
        crit_count[node] = count
        return count
    
    count_critical_subtree(1)
    
    total_crit = len(critical)
    result = 0
    
    def calculate_cost(node):
        nonlocal result
        for child, weight in children[node]:
            calculate_cost(child)
            # For edge (node, child)
            # Number of critical nodes in child's subtree
            crit_in_child = crit_count[child]
            # Number of critical nodes outside child's subtree
            crit_outside_child = total_crit - crit_in_child
            
            # If both sides have at least one critical node, this edge is needed
            if crit_in_child > 0 and crit_outside_child > 0:
                result += weight
    
    calculate_cost(1)
    print(result)

solve()