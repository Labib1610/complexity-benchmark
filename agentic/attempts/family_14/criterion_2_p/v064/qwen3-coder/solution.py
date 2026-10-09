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
    
    terminals = list(map(int, data[idx:idx+t]))
    idx += t
    
    # Since m = n-1 and it's a tree
    graph = defaultdict(list)
    
    edges = []
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        graph[u].append((v, w))
        graph[v].append((u, w))
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    terminal_set = set(terminals)
    
    # Build a virtual tree (Steiner tree) containing only the terminals and their connecting paths
    # We'll use the fact that in a tree, the minimal subtree connecting a subset of nodes 
    # is obtained by including all nodes on the paths between them.
    
    # First, root the tree at an arbitrary node, say node 1
    parent = [-1] * (n+1)
    depth = [0] * (n+1)
    weight_to_parent = [0] * (n+1)
    
    def dfs(u, par, d):
        parent[u] = par
        depth[u] = d
        for v, w in graph[u]:
            if v == par:
                weight_to_parent[v] = w  # This will be overwritten, we actually want weight_to_parent[u] = w
                continue
            if parent[v] == -1:
                weight_to_parent[v] = w
                dfs(v, u, d+1)
    
    parent[1] = 0  # mark as visited
    dfs(1, 0, 0)
    
    # Function to compute path from node to root
    def get_path_to_root(x):
        path = []
        while x != 0:
            path.append(x)
            x = parent[x]
        return path
    
    # Mark all nodes that are terminals
    is_terminal = [False] * (n+1)
    for term in terminals:
        is_terminal[term] = True
        
    # BFS from all terminals to find the minimal subtree connecting them
    # We can do this by finding the union of paths between all pairs, but more efficiently,
    # we can find the minimal subtree that connects all terminals.
    
    # An efficient way is to build the "Steiner tree" of terminals in a tree.
    # In a tree, the minimal subtree connecting a set of nodes is formed by taking
    # all nodes that lie on paths between any pair of terminals.
    # But even simpler: we can find the union of paths from each terminal to a fixed root,
    # then take the subtree induced by these nodes.
    
    # However, there's a better approach:
    # Root the tree arbitrarily. For each edge, determine if it's needed in the Steiner tree.
    # An edge is needed if removing it increases the number of components containing terminals.
    
    # Let's use a different approach:
    # Find the minimal subtree containing all terminals.
    # This is equivalent to finding the union of paths between terminals.
    # But since it's a tree, we can find the "smallest connected subgraph" containing all terminals.
    
    # Efficient method:
    # 1. Root the tree at some node.
    # 2. Find the deepest terminal.
    # 3. All ancestors of terminals must be included.
    # 4. The minimal subtree includes all nodes that are on paths between terminals.
    
    # Simpler approach:
    # Use Union-Find or just traverse the tree to find necessary edges.
    
    # Let's implement the following idea:
    # Root the tree. Then, for each edge, check if it separates the terminals into two sets.
    # If yes, we must include this edge in our solution.
    
    # But let's think differently:
    # Since it's a tree, the minimal cost to connect terminals is the MST of the metric closure
    # where distances are shortest paths in the tree. But that's complex.
    
    # Best approach:
    # Root the tree. Compute for each node whether its subtree contains a terminal.
    # Then, an edge from u to v (where v is deeper) is needed iff the subtree of v contains a terminal
    # and there exists another terminal outside the subtree of v.
    
    # Let's implement this:
    
    # Re-root at node 1
    # Already done above
    
    # Count how many terminals are in each subtree
    subtree_terminals = [0] * (n+1)
    
    # Do DFS post-order to count terminals in subtrees
    def count_subtree(node, parent_node):
        count = 1 if is_terminal[node] else 0
        for nei, _ in graph[node]:
            if nei == parent_node:
                continue
            count += count_subtree(nei, node)
        subtree_terminals[node] = count
        return count
    
    count_subtree(1, 0)
    
    total_terminals = sum(is_terminal[1:])
    
    # Now, traverse the tree again to collect necessary edges
    result = 0
    
    def dfs_collect_edges(node, parent_node):
        nonlocal result
        for nei, w in graph[node]:
            if nei == parent_node:
                continue
            # Edge from node to nei
            terminals_in_nei_subtree = subtree_terminals[nei]
            if terminals_in_nei_subtree > 0 and terminals_in_nei_subtree < total_terminals:
                result += w
            dfs_collect_edges(nei, node)
            
    dfs_collect_edges(1, 0)
    
    print(result)

if __name__ == "__main__":
    main()