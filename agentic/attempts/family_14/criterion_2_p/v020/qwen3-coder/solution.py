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
    
    incantation_fragments = list(map(int, data[idx:idx+t]))
    idx += t
    
    # If there's only one incantation fragment, no fusion is needed
    if t <= 1:
        print(0)
        return
    
    edges = []
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((w, u, v))
    
    # Sort edges by weight
    edges.sort()
    
    # Create a new graph with only incantation fragments as nodes
    # We'll use Kruskal's algorithm to find the MST that connects all incantation fragments
    
    # But we need to find the minimum cost to connect all incantation fragments in the tree
    # This is essentially finding the Steiner tree for the incantation fragments
    # However, since the input forms a tree, we can do this more efficiently
    
    # In a tree, to connect a subset of nodes, we need to find the minimal subtree that spans them
    # This is the subtree that includes all paths between pairs of the selected nodes
    # The cost is the sum of weights of edges in this subtree
    
    # Build adjacency list representation of the tree
    adj = defaultdict(list)
    for w, u, v in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Mark which nodes are incantation fragments
    is_incantation = [False] * (n + 1)
    for frag in incantation_fragments:
        is_incantation[frag] = True
    
    # If there's only one incantation fragment, no cost is needed
    if t == 1:
        print(0)
        return
    
    # Find all edges that must be included in the minimal connected subtree containing all incantation fragments
    # We can do this by finding the paths between all pairs of incantation fragments and taking the union of edges
    # But there's a more efficient way: since it's a tree, we can find the minimal subtree containing all marked nodes
    
    # One approach: Use the fact that in a tree, the minimal connected subgraph containing a set of vertices
    # is the union of all paths between pairs of these vertices. 
    # A simpler way: repeatedly contract edges not involving incantation fragments when possible,
    # but since it's a tree, we can think of it differently.
    
    # Better approach for a tree:
    # The minimal subtree containing all marked nodes can be found by:
    # 1. Starting with all leaves that are not marked, remove them
    # 2. Repeat until all remaining nodes are either marked or have degree > 1 in the current tree
    # But actually, we just need to find the sum of edge weights in the subtree that spans all marked nodes
    
    # Even simpler approach for this problem:
    # Since the structure is a tree, we can use the following algorithm:
    # 1. Root the tree at any node
    # 2. For each node, compute if its subtree contains any marked node
    # 3. An edge should be counted if it connects two components that both contain marked nodes
    
    # Let's implement this properly:
    
    # First, let's build the tree and root it
    # We'll use DFS to determine for each node if its subtree contains a marked node
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for w, u, v in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Track which nodes are marked
    marked = [False] * (n + 1)
    for frag in incantation_fragments:
        marked[frag] = True
        
    if t == 1:
        print(0)
        return

    # DFS to find the edges needed
    visited = [False] * (n + 1)
    total_cost = 0
    
    def dfs(u):
        visited[u] = True
        # Count of marked nodes in subtree rooted at u
        count = 1 if marked[u] else 0
        for v, w in adj[u]:
            if not visited[v]:
                child_count = dfs(v)
                # If the child subtree has at least one marked node and we have at least one marked node
                # in the rest of the tree, then this edge must be included
                if child_count > 0:
                    nonlocal total_cost
                    total_cost += w
                count += child_count
        return count
    
    # Start DFS from node 1
    dfs(1)
    
    # Wait, this approach counts too many edges. Let me rethink.
    
    # Correct approach:
    # In the minimal subtree spanning all marked vertices in a tree:
    # An edge {u,v} is in this subtree iff removing it separates the tree into two components,
    # each containing at least one marked vertex.
    
    # Algorithm:
    # 1. Root the tree at an arbitrary node
    # 2. Compute for each node u, the number of marked nodes in its subtree (num_marked[u])
    # 3. For each edge {u,v} where v is a child of u:
    #    It's in the minimal subtree iff num_marked[v] > 0 and num_marked[root] - num_marked[v] > 0
    
    visited = [False] * (n + 1)
    num_marked = [0] * (n + 1)
    total_cost = 0
    
    # Build parent relationship for tree traversal
    parent = [-1] * (n + 1)
    
    # First, create adjacency list and find a root
    adj_list = [[] for _ in range(n + 1)]
    for w, u, v in edges:
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))
        
    # Pick node 1 as root and build tree structure via BFS
    queue = [1]
    visited[1] = True
    tree_adj = [[] for _ in range(n + 1)]  # tree_adj[u] = [(child, weight)]
    
    while queue:
        u = queue.pop(0)
        for v, w in adj_list[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                tree_adj[u].append((v, w))
                queue.append(v)
                
    # Now compute num_marked via post-order traversal (children first)
    visited = [False] * (n + 1)
    
    def compute_num_marked(u):
        visited[u] = True
        count = 1 if marked[u] else 0
        for v, w in tree_adj[u]:
            if not visited[v]:
                count += compute_num_marked(v)
        num_marked[u] = count
        return count
    
    compute_num_marked(1)
    
    # Total marked nodes
    total_marked = num_marked[1]
    
    # Calculate cost by checking each edge in the tree
    visited = [False] * (n + 1)
    
    def calculate_cost(u):
        visited[u] = True
        cost = 0
        for v, w in tree_adj[u]:
            if not visited[v]:
                # Edge from u to v
                # It's needed if v's subtree has marked nodes AND the rest of the tree has marked nodes
                if num_marked[v] > 0 and (total_marked - num_marked[v]) > 0:
                    cost += w
                cost += calculate_cost(v)
        return cost
    
    total_cost = calculate_cost(1)
    print(total_cost)

if __name__ == "__main__":
    main()