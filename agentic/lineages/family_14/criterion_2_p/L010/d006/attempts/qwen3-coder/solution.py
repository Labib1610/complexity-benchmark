import sys
from collections import defaultdict
import heapq

def find_mst_with_pseudo_edges(n, edges, terminals):
    if len(terminals) <= 1:
        return 0
    
    # Build adjacency list
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Find the subtree that connects all terminals
    # This is essentially finding the Steiner tree, but we'll use a simpler approach:
    # Build a complete graph where edge weights are shortest paths between terminals,
    # then find MST of this complete graph.
    
    # However, there's a more efficient way for trees:
    # We can find the minimal subtree that connects all terminals.
    # This is done by finding the "Steiner tree" on a tree, which can be found by:
    # 1. Finding all nodes that are on paths between terminal pairs
    # 2. Taking the subtree induced by these nodes
    
    # Simpler approach for trees:
    # The minimal set of edges is the set of edges in the tree that lie on some path
    # between two terminals. We can find this by marking all edges that are on paths
    # between terminal pairs.
    
    # Even simpler: since it's a tree, the Steiner tree is the union of paths between
    # terminals. But we want the minimum cost, so we need to avoid double-counting.
    
    # Best approach for tree: 
    # Root the tree at any node, compute for each node whether its subtree contains
    # any terminal. Then an edge is needed iff it separates two parts each containing
    # at least one terminal.
    
    # Let's implement this correctly:
    
    # First, root the tree at node 1
    # Build parent/depth information via DFS
    parent = [-1] * (n + 1)
    depth = [0] * (n + 1)
    children = defaultdict(list)
    
    def dfs(u, p, d):
        parent[u] = p
        depth[u] = d
        for v, w in adj[u]:
            if v != p:
                children[u].append((v, w))
                dfs(v, u, d + 1)
    
    dfs(1, -1, 0)
    
    # For each node, compute if its subtree contains any terminal
    is_terminal = [False] * (n + 1)
    for t in terminals:
        is_terminal[t] = True
        
    subtree_has_terminal = [False] * (n + 1)
    
    # Post-order traversal to compute subtree_has_terminal
    def post_order(u):
        has = is_terminal[u]
        for v, w in children[u]:
            has |= post_order(v)
        subtree_has_terminal[u] = has
        return has
    
    post_order(1)
    
    # Now collect edges that connect different components with terminals
    total_cost = 0
    # Pre-order traversal to check edges
    def pre_order(u):
        nonlocal total_cost
        for v, w in children[u]:
            # Edge from u to v
            # It's needed if subtree of v has terminals AND the rest of the tree has terminals
            # The rest has terminals iff total terminals > terminals in subtree of v
            pre_order(v)
            
    # Better approach: count edges in the Steiner tree
    # An edge {u, v} where v is child of u is in Steiner tree iff
    # both the subtree of v contains a terminal and the rest of the tree contains a terminal
    
    terminal_set = set(terminals)
    total_terminals = len(terminals)
    
    # Compute for each subtree how many terminals it contains
    count_in_subtree = [0] * (n + 1)
    
    def compute_counts(u):
        count = 1 if u in terminal_set else 0
        for v, w in children[u]:
            count += compute_counts(v)
        count_in_subtree[u] = count
        return count
    
    compute_counts(1)
    
    # Now sum up the weights of edges that should be included
    total_cost = 0
    def calculate_cost(u):
        nonlocal total_cost
        for v, w in children[u]:
            # Edge from u to v is included if:
            # - subtree of v contains at least one terminal, and
            # - the rest (including u) contains at least one terminal
            terminals_in_v_subtree = count_in_subtree[v]
            if terminals_in_v_subtree > 0 and (total_terminals - terminals_in_v_subtree) > 0:
                total_cost += w
            calculate_cost(v)
                
    calculate_cost(1)
    
    return total_cost

# Read input
line = sys.stdin.readline().split()
n, m, t = int(line[0]), int(line[1]), int(line[2])

terminals = list(map(int, sys.stdin.readline().split()))

edges = []
for _ in range(m):
    line = sys.stdin.readline().split()
    u, v, w = int(line[0]), int(line[1]), int(line[2])
    edges.append((u, v, w))

print(find_mst_with_pseudo_edges(n, edges, terminals))