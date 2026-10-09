import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1000000)
    
    R, S, P = map(int, sys.stdin.readline().split())
    mandated = set(map(int, sys.stdin.readline().split()))
    
    # Build adjacency list with weights
    adj = defaultdict(list)
    edges = []
    for _ in range(S):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # If all nodes are mandated, redundancy index = P - S
    # We need redundancy index = 1, so P - (S - extra) = 1
    # So extra = S - P + 1
    
    if len(mandated) == R:
        # All nodes are mandated
        total = sum(w for u, v, w in edges)
        print(total)
        return
        
    # Find connected components when removing mandated nodes
    # But since it's a tree, we can think differently
    
    # Key insight: In a tree, if we have a subset of nodes,
    # the redundancy index = number of nodes in subset - number of edges with both ends in subset
    # We want this to be exactly 1.
    
    # So we want |Subset| - |E_subset| = 1
    # Which means |E_subset| = |Subset| - 1
    # This means the subgraph induced by Subset is a tree.
    
    # So we want to find a minimal superset of mandated nodes that induces a connected subtree.
    
    # Since the original graph is a tree, the minimal connected subgraph containing all mandated nodes
    # is the union of all paths between pairs of mandated nodes.
    # This is equivalent to the subtree induced by all nodes on paths between any two mandated nodes.
    
    # To find this, we can do a BFS/DFS from all mandated nodes simultaneously until we connect them all.
    # Actually, there's a simpler way for trees:
    # The minimal connected subtree containing all mandated nodes is the same as taking the union
    # of all paths between mandated nodes.
    
    # Even simpler approach:
    # In a tree, the minimal connected subgraph containing a set of nodes
    # is obtained by including all nodes that lie on some path between two nodes in the set.
    # But there's an even simpler characterization:
    # It's the subtree formed by starting with the mandated nodes and adding all nodes that are on
    # the paths between them.
    
    # Efficient way:
    # 1. Root the tree at any node.
    # 2. Find the "center" or use a different approach.
    # Let's use the fact that in a tree, the minimal connected subtree containing a set of nodes
    # can be found by doing multi-source BFS from all mandated nodes until we've included enough nodes
    # to make the induced subgraph connected.
    
    # Actually, let's think combinatorially:
    # We want a set S' such that:
    # 1. Mandated nodes ⊆ S'
    # 2. Number of nodes in S' - number of edges with both endpoints in S' = 1
    # 3. Sum of weights of edges with both endpoints in S' is minimized
    
    # Since the graph is a tree, any connected subset of k nodes has exactly k-1 edges.
    # So for condition 2: |S'| - |edges in S'| = 1 => |S'| - (|S'|-1) = 1 => 1 = 1. Always true for connected sets.
    
    # Wait, that's not right. Let me re-read...
    
    # Redundancy Index = (number of upgraded outposts) - (number of internal links)
    # We want this to be exactly 1.
    
    # In a general graph, if we pick a subset of nodes, the number of internal links depends on which edges are picked.
    # In our case, the graph is a tree.
    
    # So we want to choose a subset S' such that:
    # 1. Mandated ⊆ S'
    # 2. |S'| - |{edges e={u,v} : u∈S', v∈S'}| = 1
    # 3. Minimize sum_{e={u,v}, u∈S', v∈S'} w(e)
    
    # In a tree, a subset of nodes induces a subtree iff it's connected.
    # For a connected subset of k nodes in a tree, there are exactly k-1 edges.
    # So |S'| - |edges[S']| = |S'| - (|S'|-1) = 1.
    # So any connected subset satisfies the redundancy index = 1.
    
    # Therefore, we just need to find the minimum weight subtree that contains all mandated nodes.
    # This is a classic problem: find the minimum Steiner tree for the mandated nodes.
    # But in a general graph, this is NP-hard. However, in a tree, it's polynomial.
    
    # In a tree, the minimum connected subgraph containing a set of terminals (mandated nodes)
    # is unique and can be found as follows:
    # 1. Root the tree at any node.
    # 2. Find the deepest node that is a descendant of all mandated nodes (this doesn't work).
    # Better approach:
    # 3. Find all pairwise LCA (lowest common ancestors) and take the union of paths.
    # Even better:
    # 4. Do a single traversal to find the minimal subtree.
    
    # Algorithm:
    # 1. Root the tree at node 1.
    # 2. Do a DFS to compute parent and depth for each node.
    # 3. Mark all nodes that are either mandated or have a mandated descendant.
    # 4. The minimal connected subtree consists of all nodes that are marked and their neighbors in the tree
    #    that are also marked.
    
    # Simpler approach:
    # The minimal subtree containing all mandated nodes is the union of all paths between pairs of mandated nodes.
    # But there's a linear-time algorithm:
    # 1. Pick any mandated node as root.
    # 2. Compute distances from root to all other nodes.
    # 3. Find the farthest mandated node from root. Call it u.
    # 4. Compute distances from u. Find the farthest mandated node from u. Call it v.
    # 5. The path from u to v contains all mandated nodes (in a tree, this gives us a "diameter").
    # 6. But actually, we want the whole subtree, not just the diameter path.
    
    # Correct approach for trees:
    # 1. Root the tree at any node.
    # 2. Do post-order traversal. For each node, mark it if it is mandated or if any of its children is marked.
    # 3. The marked nodes form the minimal connected subtree containing all mandated nodes.
    
    # Implementation:
    
    # Build parent pointers via BFS
    parent = [-1] * (R + 1)
    visited = [False] * (R + 1)
    queue = deque([1])
    visited[1] = True
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.append(v)
    
    # Mark nodes that should be included in the minimal subtree
    include = [False] * (R + 1)
    # Mark all mandated nodes
    for node in mandated:
        include[node] = True
    
    # Propagate marks up to ancestors
    # Process nodes in reverse topological order (from leaves to root)
    # We can do BFS from leaves or use another method.
    # Simple way: repeatedly add parents of included nodes until no change
    
    changed = True
    while changed:
        changed = False
        for u in range(1, R + 1):
            if not include[u]:
                for v, w in adj[u]:
                    if include[v]:
                        include[u] = True
                        changed = True
                        break
    
    # Now, include contains all nodes that should be in our subtree
    # Count the cost of edges within this subtree
    cost = 0
    for u, v, w in edges:
        if include[u] and include[v]:
            cost += w
            
    print(cost)

if __name__ == "__main__":
    main()