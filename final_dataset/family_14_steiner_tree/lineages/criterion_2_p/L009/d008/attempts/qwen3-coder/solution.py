import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    N, E, F = map(int, sys.stdin.readline().split())
    targets = list(map(int, sys.stdin.readline().split()))
    
    # Convert to 0-indexed
    targets = [t - 1 for t in targets]
    
    edges = []
    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u-1, v-1))
    
    # Sort edges by weight
    edges.sort()
    
    # Union-Find data structure
    parent = list(range(N))
    rank = [0] * N
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        return True
    
    # Kruskal's algorithm variant
    cost = 0
    components = len(targets)
    
    # Initially, each target is its own component
    target_set = set(targets)
    
    for w, u, v in edges:
        # Check if u and v belong to target set
        in_u = u in target_set
        in_v = v in target_set
        
        # Find roots
        ru = find(u)
        rv = find(v)
        
        # If they are already connected, skip
        if ru == rv:
            continue
            
        # Check if this edge connects two different components that contain targets
        u_is_target_component = (ru in [find(x) for x in targets])
        v_is_target_component = (rv in [find(x) for x in targets])
        
        # If both components have targets, we need this edge
        if u_is_target_component and v_is_target_component and find(u) != find(v):
            union(u, v)
            cost += w
            components -= 1
            if components == 1:
                break
        # If only one has targets, we might need it
        elif (u_is_target_component or v_is_target_component) and find(u) != find(v):
            union(u, v)
        # If neither has targets, we don't need it for targets but might for connectivity
        elif not u_is_target_component and not v_is_target_component:
            union(u, v)
    
    # Actually, let's think differently.
    # We want the minimum spanning tree that connects all targets.
    # This is exactly the Steiner tree problem, but on a graph where all edges are given.
    # However, since E = N-1, the graph is a tree!
    # So we need to find the minimal subtree that spans all target nodes.
    
    # In a tree, the minimal connected subgraph containing all target nodes
    # is the union of paths between all pairs of target nodes.
    # But that's expensive to compute directly.
    
    # Better approach: 
    # Since we have a tree (N nodes, N-1 edges), we can:
    # 1. Build the tree
    # 2. Find the minimal subtree that contains all targets
    # This is equivalent to finding the "Steiner tree" in a tree, which can be found by:
    # - Taking all leaves that are targets
    # - Taking the nodes on paths between them
    # - The cost is the sum of edge weights in this subtree
    
    # Even simpler: we can use the fact that in a tree, the minimal connected subgraph
    # containing a set of nodes is unique. We can find it by:
    # 1. Root the tree at any node
    # 2. Find the lowest common ancestor (LCA) concepts, but maybe overkill
    
    # Let's build adjacency list representation of the tree
    from collections import defaultdict, deque
    
    adj = defaultdict(list)
    edge_weights = {}
    
    for w, u, v in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
        edge_weights[(u,v)] = w
        edge_weights[(v,u)] = w
    
    # If only one target, cost is 0
    if F <= 1:
        print(0)
        return
    
    # Find the minimal subtree that connects all targets
    # In a tree, this is the union of paths between consecutive targets in some ordering
    # But the right way is to find the "Steiner tree"
    
    # Algorithm:
    # 1. Root the tree at target[0]
    # 2. For each target, find path to root
    # 3. Union of all such paths gives the minimal subtree
    # But we need to avoid double counting edges
    
    # Better: 
    # Use the fact that in a tree, the minimal subtree spanning a set of nodes
    # can be found by:
    # 1. Take all paths between pairs of targets
    # 2. The union is the desired subtree
    # But more efficiently:
    # 1. Root at any node
    # 2. Find all nodes that must be included (those on paths between targets)
    
    # Most efficient approach for tree:
    # 1. Root tree at target[0]
    # 2. Do DFS to mark ancestors
    # 3. Find the minimal connected subtree containing all targets
    
    def dfs_mark(root):
        visited = [False] * N
        parent_tree = [-1] * N
        stack = [root]
        visited[root] = True
        
        while stack:
            node = stack.pop()
            for nei, w in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    parent_tree[nei] = node
                    stack.append(nei)
        return parent_tree
    
    # Root at first target
    root = targets[0]
    parent_tree = dfs_mark(root)
    
    # Now find the minimal subtree that contains all targets
    # We need to include all nodes on paths from root to each target
    # and paths between targets
    
    # Actually, simpler approach:
    # In a tree, the minimal connected subgraph containing S is the union of paths
    # between all pairs of nodes in S. But there's a more efficient way:
    # Find the "closure" under taking paths.
    
    # Even simpler for tree:
    # 1. Root at any node
    # 2. For each target, mark all ancestors
    # 3. The minimal subtree is induced by marked nodes
    # But we also need to connect them properly
    
    # Best approach:
    # Use the fact that we can sort edges by weight and use Union-Find
    # but only consider edges that help connect targets
    
    # Re-initialize Union-Find
    parent = list(range(N))
    rank = [0] * N
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        return True
    
    cost = 0
    components = len(targets)
    
    # Create a mapping from node to whether it's a target
    is_target = [False] * N
    for t in targets:
        is_target[t] = True
    
    # We need to connect all targets. Since the graph is a tree,
    # we just need F-1 edges to connect F components (targets).
    # But targets might already be in same component.
    
    # Use Union-Find with Kruskal: process edges in order of weight
    # and connect components only when it helps connect targets
    
    target_components = set()
    for t in targets:
        target_components.add(find(t))
    
    for w, u, v in edges:
        pu = find(u)
        pv = find(v)
        
        if pu != pv:
            # Check if this union connects new target components
            u_has_target = any(find(t) == pu for t in targets)
            v_has_target = any(find(t) == pv for t in targets)
            
            if u_has_target or v_has_target:
                union(u, v)
                cost += w
                
                # Update number of target components
                new_components = len(set(find(t) for t in targets))
                if new_components == 1:
                    break
    
    print(cost)

threading.Thread(target=main).start()