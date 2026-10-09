import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    R, S, P = map(int, sys.stdin.readline().split())
    mandated = list(map(int, sys.stdin.readline().split()))
    
    # Build the tree
    graph = defaultdict(list)
    edges = {}
    
    for _ in range(S):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
        edges[(u,v)] = w
        edges[(v,u)] = w
    
    if P == 1:
        print(0)
        return
    
    # Find the subtree that contains all mandated nodes
    # We can do this by finding the minimal subtree that connects all mandated nodes
    # This is equivalent to finding the Steiner tree for the mandated nodes in a tree,
    # which is simply the union of paths between all pairs, but more efficiently,
    # it's the subtree induced by the mandated nodes and their connecting paths.
    
    # In a tree, the minimal connected subgraph containing a set of nodes
    # is the same as the union of all paths between pairs, but there's a simpler way:
    # Take all nodes that lie on some path between any two mandated nodes.
    
    # However, there's an even simpler approach for trees:
    # The minimal cost is the sum of edge weights in the subtree that spans all mandated nodes.
    # To find this, we can:
    # 1. Pick any mandated node as root
    # 2. Do a DFS to compute subtree info
    # 3. Count how many mandated nodes are in each subtree
    # 4. An edge is in the final tree if removing it separates the mandated nodes into two non-empty groups
    
    # Let's use the standard algorithm for finding the minimal subtree (Steiner tree) in a tree:
    # 1. Root the tree at any node
    # 2. For each node, compute how many mandated nodes are in its subtree
    # 3. An edge (u,v) where v is child of u is included if subtree of v contains at least 1 and at most P-1 mandated nodes
    
    # Let's root the tree at mandated[0]
    root = mandated[0]
    mandated_set = set(mandated)
    
    # Build parent pointers and depth via BFS
    parent = {root: None}
    depth = {root: 0}
    queue = deque([root])
    node_list = []
    
    while queue:
        u = queue.popleft()
        node_list.append(u)
        for v, w in graph[u]:
            if v not in parent:
                parent[v] = u
                depth[v] = depth[u] + 1
                queue.append(v)
    
    # Compute for each node, how many mandated nodes are in its subtree
    # We process nodes in reverse topological order (from leaves up)
    subtree_mandated_count = {node: 0 for node in node_list}
    
    # Initialize counts for mandated nodes
    for node in mandated_set:
        subtree_mandated_count[node] = 1
    
    # Process from leaves to root
    for node in reversed(node_list):
        if node != root:
            par = parent[node]
            subtree_mandated_count[par] += subtree_mandated_count[node]
    
    # Now, traverse the tree again to collect edges in the minimal subtree
    total_cost = 0
    visited_edges = set()
    
    # For each edge (u,v), check if it should be included
    # An edge is included if it separates the mandated nodes
    # i.e., one side has >=1 and <=P-1 mandated nodes
    
    for u in node_list:
        for v, w in graph[u]:
            if (u, v) in visited_edges or (v, u) in visited_edges:
                continue
            visited_edges.add((u, v))
            
            # Determine which direction the edge goes in the rooted tree
            if parent[v] == u:
                # u is parent of v
                count_in_subtree = subtree_mandated_count[v]
            elif parent[u] == v:
                # v is parent of u
                count_in_subtree = subtree_mandated_count[u]
            else:
                # Should not happen in a tree
                continue
                
            # Edge is included if 1 <= count_in_subtree <= P-1
            if 1 <= count_in_subtree <= P - 1:
                total_cost += w
    
    print(total_cost)

if __name__ == "__main__":
    main()