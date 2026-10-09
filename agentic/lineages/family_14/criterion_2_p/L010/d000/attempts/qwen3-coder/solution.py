import sys
from collections import defaultdict
import heapq

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
        
    spores = set()
    for _ in range(t):
        spore = int(data[idx])
        spores.add(spore)
        idx += 1
    
    # Build the tree
    adj = [[] for _ in range(n + 1)]
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
    
    # Since it's a tree (n nodes, n-1 edges, connected), we can use Kruskal's or Prim's
    # But since we only care about connecting the 't' spore nodes, we want the Minimum Spanning Tree
    # that connects all the spore nodes - this is the Steiner Tree problem on a tree,
    # which can be solved by taking the union of paths between all pairs, but more efficiently:
    # In a tree, the minimal way to connect a subset of nodes is to take the MST of the subtree
    # induced by those nodes (including necessary intermediate nodes).
    # However, there's a simpler approach here:
    # Root the tree at any node, compute pairwise distances between spore nodes,
    # then find the MST of the complete graph on spore nodes with these distances.
    # But even simpler: since the original graph is a tree, we can just find the 
    # minimal subtree that spans all spore nodes. This is done by:
    # 1. Finding the subtree that contains all spore nodes (by removing leaf nodes not in spores)
    # 2. The cost is the sum of edge weights in that subtree.
    
    # Actually, let's think differently. Since the input is a tree, and we want to connect all spore nodes,
    # the minimal cost is the cost of the minimal subtree that contains all spore nodes.
    # This is known as the minimal Steiner tree on a tree, and can be computed as follows:
    # Root the tree at some node, then find the union of paths from root to each spore node.
    # But there's a better way:
    # The answer is the total weight of the minimal subtree spanning all terminals.
    # For a tree, this equals the total weight of edges in the subtree formed by all nodes
    # that are on some path between any two terminal nodes.
    # An easier algorithm:
    # 1. Mark all spore nodes as "terminals"
    # 2. Iteratively remove leaf nodes that are not terminals
    # 3. The remaining edges form the minimal subtree connecting all terminals
    # 4. Sum their weights
    
    # Let's implement this approach:
    
    # Build adjacency list with edge indices
    adj_list = [[] for _ in range(n+1)]
    edge_weights = {}
    for i in range(m):
        u, v, w = edges[i]
        adj_list[u].append((v, w, i))
        adj_list[v].append((u, w, i))
        edge_weights[(u,v)] = w
        edge_weights[(v,u)] = w
    
    # Count degree of each node
    degree = [0] * (n+1)
    for u in range(1, n+1):
        degree[u] = len(adj_list[u])
        
    # Mark terminal nodes
    is_terminal = [False] * (n+1)
    for s in spores:
        is_terminal[s] = True
    
    # Keep track of removed edges
    removed_edges = set()
    
    # Queue of leaves to process
    from collections import deque
    queue = deque()
    for u in range(1, n+1):
        if degree[u] == 1 and not is_terminal[u]:
            queue.append(u)
            
    # Iteratively remove non-terminal leaves
    while queue:
        u = queue.popleft()
        # u is a leaf and not terminal, remove it
        for v, w, edge_idx in adj_list[u]:
            if (u, v) not in removed_edges and (v, u) not in removed_edges:
                removed_edges.add((u, v))
                degree[u] -= 1
                degree[v] -= 1
                # Check if neighbor becomes a new leaf and is not terminal
                if degree[v] == 1 and not is_terminal[v]:
                    queue.append(v)
                    
    # Sum up weights of edges not removed
    total_cost = 0
    for u, v, w in edges:
        if (u, v) not in removed_edges and (v, u) not in removed_edges:
            total_cost += w
            
    print(total_cost)

if __name__ == "__main__":
    main()