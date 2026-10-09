import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, t = map(int, sys.stdin.readline().split())
    incantation_fragments = set(map(int, sys.stdin.readline().split()))
    
    # Since m = n-1 and the structure property says it forms a single tree,
    # this is a tree problem. We need to find the minimum cost to connect
    # all the incantation fragments.
    
    # In a tree, to connect k nodes, we need exactly k-1 edges.
    # The minimum cost to connect all incantation fragments is the
    # minimum spanning tree of the subgraph induced by the incantation fragments.
    # But since we're in a tree, the minimum way to connect the incantation fragments
    # is to take the edges on the paths between them.
    
    # Build the tree
    from collections import defaultdict
    import heapq
    
    adj = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((w, u, v))
    
    # If there's only one or zero incantation fragments, cost is 0
    if t <= 1:
        print(0)
        return
    
    # We need to find the minimum cost to connect all incantation fragments.
    # In a tree, this is equivalent to finding the minimum Steiner tree.
    # But there's a simpler way: since it's a tree, we can find the "Steiner tree"
    # by finding the union of paths between the incantation fragments.
    
    # Find paths between all pairs of incantation fragments? No, that's not efficient.
    # Better approach: find the minimal subtree that contains all incantation fragments.
    
    # In a tree, the minimal connected subtree containing a set of vertices
    # can be found by taking all edges on paths between pairs of these vertices.
    # But even better: we can do a single DFS and find the minimal subtree.
    
    # Let's do this:
    # 1. Root the tree at any node.
    # 2. Find the minimal subtree that contains all incantation fragments.
    # 3. The cost is the sum of weights of edges in this subtree.
    
    # Actually, let's think differently.
    # Since it's a tree, we can find the minimal connected subtree containing
    # all the incantation fragments by:
    # 1. Marking all incantation fragments as "special".
    # 2. Doing a post-order DFS: a node is in the subtree if it's special
    #    or if it has a child subtree that contains special nodes.
    # 3. Count an edge if it connects to a subtree that contains special nodes.
    
    # Let's root the tree at node 1
    parent = [-1] * (n + 1)
    children = defaultdict(list)
    edge_weight = {}
    
    def dfs_build(root, par):
        for nei, w in adj[root]:
            if nei != par:
                parent[nei] = root
                edge_weight[(nei, root)] = w
                edge_weight[(root, nei)] = w
                children[root].append(nei)
                dfs_build(nei, root)
    
    dfs_build(1, -1)
    
    # Now do a post-order DFS to find the minimal subtree
    # that contains all incantation fragments
    is_special = [False] * (n + 1)
    for frag in incantation_fragments:
        is_special[frag] = True
    
    total_cost = 0
    
    def dfs_subtree(node):
        # Returns True if subtree rooted at node contains any special node
        has_special = is_special[node]
        for child in children[node]:
            child_has_special = dfs_subtree(child)
            has_special |= child_has_special
            # If child subtree has special nodes, we need the edge to it
            if child_has_special:
                total_cost += edge_weight[(node, child)]
        return has_special
    
    dfs_subtree(1)
    print(total_cost)

threading.Thread(target=main).start()