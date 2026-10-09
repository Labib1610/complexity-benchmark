import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1000000)
    
    n, m, t = map(int, sys.stdin.readline().split())
    terminals = set(map(int, sys.stdin.readline().split()))
    
    # If there's only one terminal, we don't need any edges
    if t <= 1:
        print(0)
        return
    
    # Build the tree
    adj = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # Find the minimum spanning tree that connects all terminals
    # This is essentially the Steiner tree problem, but since we have a tree,
    # we can solve it efficiently.
    
    # Approach:
    # 1. Find the minimal subtree that contains all terminals
    # 2. The cost is the sum of weights in this subtree
    
    # In a tree, the minimal connected subgraph containing all terminals
    # is the union of all paths between terminals.
    # But there's a simpler way: find the "Steiner tree" in a tree.
    
    # Algorithm:
    # 1. Root the tree at any node
    # 2. For each node, compute if it's needed in the Steiner tree
    # 3. A node is needed if it's a terminal or has two subtrees that contain terminals
    
    # Let's use a different approach:
    # Find the minimal subtree that spans all terminals.
    # In a tree, this is unique.
    
    # We can do this by:
    # 1. Finding all pairwise paths between terminals
    # 2. Taking the union of these paths
    # 3. Summing the unique edge weights
    
    # But that's complex. Simpler approach:
    # The minimal subtree connecting all terminals can be found by:
    # 1. Starting with all terminals
    # 2. Repeatedly adding the parent until we have a connected component
    # Actually, in a tree, the minimal subtree is the union of paths between terminals.
    # But there's a linear-time algorithm:
    
    # Key insight: In a tree, the minimal subtree connecting a set of vertices
    # is the subtree induced by all vertices that lie on some path between two terminals.
    
    # Algorithm:
    # 1. Root the tree at an arbitrary node
    # 2. Compute for each node whether the subtree rooted at it contains a terminal
    # 3. An edge is in the minimal subtree if it connects a node where the subtree
    #    contains a terminal to its parent, and the parent's removal would disconnect
    #    terminals.
    
    # Even simpler:
    # The cost is the sum of edge weights in the minimal subtree connecting all terminals.
    # In a tree, this is computed by:
    # 1. Rooting the tree
    # 2. For each node, determine if it's in the Steiner tree
    # 3. Count edges between nodes in the Steiner tree
    
    # Let's implement a clean solution:
    
    # Build adjacency list with weights
    tree = defaultdict(list)
    for u, v, w in edges:
        tree[u].append((v, w))
        tree[v].append((u, w))
    
    # If there's only one terminal, cost is 0
    if len(terminals) <= 1:
        print(0)
        return
    
    # Function to find the minimal subtree weight connecting all terminals
    def dfs(node, parent):
        # Returns (is_subtree_node, total_weight)
        # is_subtree_node: whether this node should be in the minimal subtree
        is_terminal = node in terminals
        is_needed = is_terminal
        total_weight = 0
        
        for neighbor, weight in tree[node]:
            if neighbor == parent:
                continue
            is_needed_child, child_weight = dfs(neighbor, node)
            if is_needed_child:
                is_needed = True
                total_weight += child_weight + weight
                
        return (is_needed, total_weight) if is_needed else (False, 0)
    
    # Start DFS from node 1
    _, result = dfs(1, -1)
    print(result)

if __name__ == "__main__":
    main()