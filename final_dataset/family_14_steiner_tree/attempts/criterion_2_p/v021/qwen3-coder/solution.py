import sys
from collections import defaultdict
import heapq

def main():
    import sys
    sys.setrecursionlimit(1000000)
    
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    m = int(data[idx+1])
    t = int(data[idx+2])
    idx += 3
    
    if t == 1:
        print(0)
        return
        
    mural_chambers = set()
    for _ in range(t):
        mural_chambers.add(int(data[idx]))
        idx += 1
        
    edges = []
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        w = int(data[idx+2])
        idx += 3
        edges.append((w, u, v))
        
    # Build graph
    adj = defaultdict(list)
    for w, u, v in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    # Prim's algorithm modified to find the minimum spanning tree that connects all mural chambers
    # We can do this by starting with all mural nodes in the initial "connected" set
    # But since we want the minimal cost to connect them, we can use a multi-source Prim's variant
    # Or better yet, build the MST of the entire graph and then find the minimal subtree that connects all mural nodes
    # That's the Steiner tree problem on a tree, which can be solved by taking the MST of the induced subgraph
    # But since the graph is a tree already, the MST is itself.
    # Wait, the problem says m=n-1 and the graph is connected if all tunnels are cleared => it's a tree.
    
    # So the tunnels form a tree. We need to find the minimum cost subtree that connects all mural nodes.
    # This is the Minimum Spanning Tree of the Steiner tree problem on a tree.
    # On a tree, the Steiner tree is obtained by taking the subtree induced by the terminal nodes (murals),
    # which means we take the union of all paths between every pair of terminal nodes,
    # and then remove unnecessary branches. But there's a simpler way.
    
    # In a tree, the minimum cost to connect a subset of nodes is the cost of the subtree formed by
    # taking all nodes that lie on some path between any two nodes in the subset.
    # This is equivalent to finding the "closure" of the subset under the tree metric.
    # A simpler approach: Root the tree at some node, compute the minimal subtree containing all terminals.
    
    # Let's build the tree and root it at node 1 (or any node)
    # Then we can do a DFS to find the minimal subtree that includes all terminals.
    
    # Actually, let's think differently. Since it's a tree, we can use the fact that 
    # the minimum cost to connect all terminals is the sum of edge weights in the subtree
    # formed by taking the union of paths between all pairs, but that's complicated.
    
    # Better approach:
    # 1. Root the tree at some node.
    # 2. Do a post-order DFS: for each node, if any of its children's subtrees contain terminals,
    #    or if the node itself is a terminal, then include this node in the subtree.
    # 3. Count the edge weight if both endpoints are included in the final subtree.
    
    # Let's implement this.
    
    # First, let's build adjacency list as undirected graph
    # We'll convert it to a rooted tree later
    
    # Pick a root, say node 1
    root = 1
    # Build parent pointers and depth via BFS/DFS
    from collections import deque
    parent = [-1] * (n+1)
    depth = [0] * (n+1)
    visited = [False] * (n+1)
    
    # BFS to build parent relationships
    queue = deque()
    queue.append(root)
    visited[root] = True
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                depth[v] = depth[u] + 1
                queue.append(v)
                
    # Now we have a rooted tree. Do post-order DFS to determine which edges to include
    # We'll compute for each node whether its subtree contains any terminal
    contains_terminal = [False] * (n+1)
    result_cost = 0
    
    # Mark leaf nodes that are terminals
    for node in range(1, n+1):
        if node in mural_chambers:
            contains_terminal[node] = True
            
    # Post-order traversal to propagate terminal info up and accumulate costs
    # Process nodes in reverse topological order based on depth (leaves first)
    # We can sort nodes by decreasing depth
    nodes_by_depth = [(depth[i], i) for i in range(1, n+1)]
    nodes_by_depth.sort(reverse=True)
    
    processed = [False] * (n+1)
    
    for _, node in nodes_by_depth:
        if processed[node]:
            continue
        processed[node] = True
        # If node is terminal, mark it
        # Propagate to parent
        if contains_terminal[node] and parent[node] != -1:
            # Edge from node to parent should be included if node's subtree has terminals
            # But we're going bottom-up, so when we process a child, we decide if edge to parent is needed
            # Let's reorganize the logic
            
            pass # This approach is getting messy
            
    # Let's try a cleaner approach:
    # 1. Root the tree at any node
    # 2. Do a DFS to compute for each node whether its subtree contains any terminal
    # 3. Do another DFS to count edges where both endpoints are needed
    
    # Reset and rebuild properly
    # Build adjacency as list of lists for efficiency
    adj_list = [[] for _ in range(n+1)]
    for w, u, v in edges:
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))
        
    # DFS to mark which nodes are needed
    is_needed = [False] * (n+1)
    is_terminal = [False] * (n+1)
    for node in mural_chambers:
        is_terminal[node] = True
        is_needed[node] = True
        
    # First DFS to propagate need upwards
    def dfs1(u, par):
        has_terminal_descendant = is_terminal[u]
        for v, w in adj_list[u]:
            if v == par:
                continue
            dfs1(v, u)
            if is_needed[v]:  # if subtree of v needs to be included
                has_terminal_descendant = True
        is_needed[u] = has_terminal_descendant
        
    dfs1(1, -1)
    
    # Second DFS to accumulate cost
    total_cost = 0
    def dfs2(u, par):
        nonlocal total_cost
        for v, w in adj_list[u]:
            if v == par:
                continue
            if is_needed[v]:  # Only traverse needed parts
                total_cost += w
                dfs2(v, u)
                
    dfs2(1, -1)
    print(total_cost)

if __name__ == "__main__":
    main()