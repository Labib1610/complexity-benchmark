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
    
    index = 0
    n = int(data[index])
    index += 1
    m = int(data[index])
    index += 1
    t = int(data[index])
    index += 1
    
    T = list(map(int, data[index:index+t]))
    index += t
    
    edges = []
    for _ in range(m):
        u = int(data[index])
        index += 1
        v = int(data[index])
        index += 1
        w = int(data[index])
        index += 1
        edges.append((w, u, v))
    
    if t <= 1:
        print(0)
        return
    
    # We need to find the minimum cost to connect all nodes in T
    # This is a Steiner tree problem, but since the transpositions form a connected graph
    # that generates S_n, we can use the fact that we need to connect the nodes in T
    # in the graph formed by the transpositions.
    
    # Since the original graph is a tree (n-1 edges and connected), 
    # the solution is to find the minimum spanning tree that connects all vertices in T.
    # This is the MST of the complete graph on T where edge weights are shortest path distances.
    
    # But there's a simpler approach for this specific case:
    # Since we're working with a tree, the Steiner tree is the same as the MST of the subtree
    # induced by the terminals plus the necessary connecting paths.
    
    # However, given the constraints and the nature of the problem,
    # we can solve it by finding the MST of the subgraph induced by T.
    # But since we're dealing with a tree structure, we can do better.
    
    # Key insight: In a tree, to connect k terminal nodes, we need exactly k-1 edges.
    # But we need to find the minimum cost set of original edges such that 
    # their span contains all nodes in T.
    
    # This is the Steiner tree problem on a general graph, but since our base graph is a tree,
    # we can solve it efficiently.
    
    # For a tree, the Steiner tree is found by:
    # 1. Consider the subtree induced by the terminals
    # 2. The optimal solution is to take the edges on the paths between terminals
    # 3. But we want the minimum weight set that connects all terminals
    
    # Simpler approach for trees:
    # Find the minimal subtree that spans all terminals.
    # This can be done by finding the "Steiner tree" in a tree, which is just
    # the union of paths between consecutive terminals in some ordering.
    # But the optimal is to take the edges in the subtree that contains all terminals.
    
    # Even simpler: since the base graph is a tree, we can find the unique paths
    # and take the union of edges needed to connect all terminals.
    
    # Build adjacency list for the tree
    adj = [[] for _ in range(n+1)]
    for i, (w, u, v) in enumerate(edges):
        adj[u].append((v, w, i))
        adj[v].append((u, w, i))
    
    # If we have only one terminal, cost is 0
    if t <= 1:
        print(0)
        return
    
    # Find the subtree that spans all terminals
    # We'll use a modified Prim's algorithm or just find the minimal way to connect them
    
    # Since it's a tree, we can find the minimal subtree containing all terminals
    # by finding the union of all paths between terminals, then taking a MST of that
    
    # But there's an even simpler way for trees:
    # The Steiner tree in a tree is the minimal subtree containing all terminals
    # which can be found by:
    # 1. Root the tree at some node
    # 2. Find the deepest common ancestor of all terminals
    # 3. The Steiner tree includes all paths from each terminal to this ancestor
    
    # Actually, let's think differently:
    # Since the original graph is a tree with n-1 edges, and we want to connect t terminals,
    # the minimum number of edges needed is t-1. But we must use edges from the original tree.
    
    # The solution is to find the minimal subtree of the original tree that contains all terminals.
    # This is a classic problem and can be solved by:
    # 1. Finding the union of paths between all pairs of terminals
    # 2. Or, more efficiently, by finding the minimal connected subgraph containing all terminals
    
    # Efficient approach:
    # 1. Mark all terminal nodes
    # 2. Run a BFS/DFS from all terminals to find the minimal subtree that connects them all
    # 3. Sum up the weights of edges in this subtree
    
    # But we need to be careful about what "connects them all" means.
    # It means the subgraph induced by the selected edges makes all terminals connected.
    
    # Since the original graph is a tree, the minimal way to connect k terminals
    # requires selecting edges such that in the subgraph they induce, all k terminals
    # are in the same connected component.
    
    # The optimal solution is the minimum weight set of edges such that 
    # all terminals are connected within the subgraph they induce.
    
    # This is exactly the Steiner tree problem on a graph, but for trees it's solvable.
    
    # Algorithm for Steiner tree in a tree:
    # 1. Root the tree at an arbitrary node
    # 2. For each node, compute whether it's an ancestor of any terminal
    # 3. An edge should be included if it's on the path between two terminals
    # 4. But more precisely, include an edge if removing it increases the number of components 
    #    containing terminals
    
    # Let's implement a clean solution:
    # Use Union-Find and Kruskal's algorithm concept, but only consider edges that are necessary
    
    # Actually, simplest correct approach:
    # Since we're working with a tree, the Steiner tree is the subgraph formed by taking
    # all edges that lie on paths between any pair of terminals.
    # To find this efficiently:
    # 1. Root the tree
    # 2. Precompute ancestors and depths
    # 3. For each terminal, mark the path from root to terminal
    # 4. The union of all such paths forms the Steiner tree
    
    # But there's an issue with that approach. Let me think of the correct way.
    
    # Correct approach for Steiner tree in a tree:
    # 1. Root the tree at node 1
    # 2. Compute parent and depth for each node
    # 3. For each edge, determine if it's part of the minimal subtree containing all terminals
    # 4. An edge (u,v) with u deeper than v is in the Steiner tree if the subtree rooted at u 
    #    contains at least one terminal but not all terminals
    
    # Let's build the tree and solve
    
    # Build adjacency list
    adj = [[] for _ in range(n+1)]
    edge_list = []
    for i, (w, u, v) in enumerate(edges):
        adj[u].append((v, w, i))
        adj[v].append((u, w, i))
        edge_list.append((w, u, v))
    
    # Root the tree at node 1 and compute parents and depths
    parent = [-1] * (n+1)
    depth = [0] * (n+1)
    visited = [False] * (n+1)
    
    def dfs(u, p, d):
        parent[u] = p
        depth[u] = d
        visited[u] = True
        for v, w, idx in adj[u]:
            if not visited[v]:
                dfs(v, u, d+1)
    
    dfs(1, -1, 0)
    
    # For each node, precompute if its subtree contains any terminal
    contains_terminal = [False] * (n+1)
    terminal_set = set(T)
    
    # Second DFS to compute contains_terminal
    visited = [False] * (n+1)
    
    def dfs2(u):
        visited[u] = True
        if u in terminal_set:
            contains_terminal[u] = True
        
        for v, w, idx in adj[u]:
            if not visited[v]:
                dfs2(v)
                if contains_terminal[v]:
                    contains_terminal[u] = True
                    
    dfs2(1)
    
    # Count total terminals in the whole tree
    total_terminals = sum(contains_terminal[1:])
    
    # Now for each edge, check if it should be included
    # An edge (u,v) where depth[u] > depth[v] should be included if:
    # - The subtree of u contains at least one terminal
    # - The subtree of u does not contain ALL terminals
    # (i.e., removing the edge separates terminals)
    
    result = 0
    # Reorganize edges to have parent-child relationship
    for w, u, v in edge_list:
        # Ensure u is the child (deeper node)
        if depth[u] < depth[v]:
            u, v = v, u  # Now u is deeper, so u is child of v
            
        # u is child, v is parent
        # Include this edge if subtree of u has some but not all terminals
        subtree_terminals = 0
        # Count terminals in subtree of u
        visited_count = [False] * (n+1)
        
        def count_subtree(node, exclude_parent):
            count = 1 if node in terminal_set else 0
            visited_count[node] = True
            for neighbor, _, _ in adj[node]:
                if not visited_count[neighbor] and neighbor != exclude_parent:
                    count += count_subtree(neighbor, node)
            return count
            
        subt_term = count_subtree(u, v)
        
        # Edge should be included if this subtree has some terminals but not all
        if subt_term > 0 and subt_term < len(T):
            result += w
    
    print(result)

if __name__ == "__main__":
    main()