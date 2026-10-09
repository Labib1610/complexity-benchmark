import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, t = map(int, sys.stdin.readline().split())
    focus = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    focus_set = set(focus)
    
    # We model the problem on a graph where nodes are indices 1..n
    # and edges are the basis vectors e_u - e_v with weight w
    # We need to ensure that for every pair of focus nodes,
    # their difference vector e_a - e_b is in the span of selected edges
    # This is equivalent to ensuring that the subgraph induced by selected edges
    # connects all the focus nodes.
    
    # Since we're given m = n-1 edges and they span all e_x - e_y,
    # the graph is a tree (since m=n-1 and connected).
    # So we have a tree, and we want to find the minimal cost subtree
    # that connects all the focus nodes. This is exactly the Steiner tree problem
    # on a tree, which has a greedy solution:
    # Root the tree arbitrarily, then for each focus node, mark the path to root.
    # The minimal subtree connecting all focus nodes is the union of all paths
    # from each focus node to the root, but we can do better:
    # Take the minimal subtree that connects all focus nodes.
    # For a tree, this is equivalent to finding the minimal connected subgraph
    # containing all focus nodes. This is the subtree induced by the union of
    # paths between all pairs of focus nodes. But there's a simpler way:
    # Root the tree at any node, and take the union of paths from each focus
    # node to the root. But even simpler: the minimal cost is the cost of
    # the subtree that spans all focus nodes. In a tree, this is just the
    # edges needed to connect all focus nodes together.
    
    # However, since it's a tree, we can use the fact that the minimum cost
    # to connect a subset of nodes (Steiner tree) in a tree can be computed
    # by rooting the tree and including all edges on the paths from each
    # focus node to the root, but removing duplicates appropriately.
    # A simpler approach is:
    # Build the minimal subtree containing all focus nodes.
    # This can be done by:
    # 1. Rooting the tree at some node
    # 2. For each focus node, include the path from that node to root
    # 3. Union of all such paths gives a connected subgraph containing all focus nodes
    # 4. But we want the minimal such subgraph (tree), so we take the union and
    #    remove redundant edges. Actually, in a tree, the minimal subtree
    #    spanning a set of nodes S is unique and its edge-set is the union
    #    of all paths between pairs of nodes in S. But there's a more efficient way:
    # If we root the tree, then the minimal subtree containing S is the subtree
    # induced by all nodes that are on some path between two nodes of S.
    # An easier characterization: take all nodes that are on the path between
    # any two focus nodes, and the edges between them.
    # But even simpler: sort focus nodes according to DFS pre-order,
    # then the minimal subtree is the union of paths from the first to last
    # in this order, plus paths to fill in the gaps.
    # Even simpler: the cost is the sum over all edges e such that
    # removing e disconnects the tree into two components both containing
    # at least one focus node.
    
    # So the algorithm is:
    # 1. Build the tree
    # 2. Do a DFS to compute for each edge whether its removal separates
    #    the focus nodes into two non-empty groups
    # 3. Sum the weights of such edges
    
    from collections import defaultdict
    
    # Build adjacency list representation of the tree
    adj = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # To solve this efficiently, we'll use the fact that we need to find
    # the minimum cost to connect all focus nodes in a tree.
    # This is the same as finding the minimum Steiner tree in a tree,
    # which equals the union of paths between consecutive focus nodes
    # in some ordering (like DFS order).
    # But there's a linear-time way:
    # Root the tree, compute for each node how many focus nodes are
    # in its subtree. Then an edge is needed iff both parts of the
    # split have at least one focus node.
    
    # Let's root the tree at node 1
    root = 1
    parent = [-1] * (n + 1)
    depth = [-1] * (n + 1)
    subtree_count = [0] * (n + 1)
    visited = [False] * (n + 1)
    
    # First DFS to compute depths and parents
    def dfs1(node, par, d):
        parent[node] = par
        depth[node] = d
        visited[node] = True
        for nei, w in adj[node]:
            if not visited[nei]:
                dfs1(nei, node, d + 1)
    
    dfs1(root, -1, 0)
    
    # Now we do a second DFS post-order to count focus nodes in each subtree
    visited = [False] * (n + 1)
    
    def dfs2(node):
        visited[node] = True
        count = 1 if node in focus_set else 0
        for nei, w in adj[node]:
            if not visited[nei] and nei != parent[node]:
                count += dfs2(nei)
        subtree_count[node] = count
        return count
    
    dfs2(root)
    
    # Now for each edge, check if it's a bridge separating focus nodes
    total_cost = 0
    
    for u, v, w in edges:
        # Determine which direction the edge goes in the rooted tree
        if parent[u] == v:
            # u is child of v
            child_side = subtree_count[u]
            other_side = t - child_side
        elif parent[v] == u:
            # v is child of u
            child_side = subtree_count[v]
            other_side = t - child_side
        else:
            # Should not happen in a tree
            continue
            
        if child_side > 0 and other_side > 0:
            total_cost += w
    
    print(total_cost)

threading.Thread(target=main).start()