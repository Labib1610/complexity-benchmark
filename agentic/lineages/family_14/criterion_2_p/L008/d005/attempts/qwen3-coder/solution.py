import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1000000)
    
    R, S, P = map(int, sys.stdin.readline().split())
    injected = set(map(int, sys.stdin.readline().split()))
    
    # Since S = R - 1 and the graph is connected with no redundancy,
    # it's a tree.
    
    adj = defaultdict(list)
    edges = []
    
    for _ in range(S):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # If there's only one injected node, cost is 0
    if P == 1:
        print(0)
        return
    
    # We need to find the minimal subtree that connects all injected nodes.
    # This is the Steiner tree problem on a tree, which can be solved efficiently.
    
    # Approach:
    # 1. Find the subtree that contains all injected nodes.
    # 2. This can be done by finding the union of paths between all pairs of injected nodes,
    #    or more efficiently, by finding the minimal connected subtree containing all injected nodes.
    
    # Efficient approach:
    # 1. Root the tree at any node.
    # 2. Find all leaves that are not injected and remove them iteratively,
    #    until all remaining leaves are injected nodes.
    # But this is complex to implement correctly.
    
    # Simpler and correct approach:
    # Since it's a tree, the minimal connected subgraph containing all injected nodes
    # is the union of paths between them. But more precisely, it's the subtree
    # formed by taking all nodes that lie on some path between two injected nodes.
    
    # Even simpler:
    # The minimal cost is the cost of the subtree that spans all injected nodes.
    # In a tree, this is equivalent to finding the "Steiner tree" which can be found as follows:
    # - Root the tree at an arbitrary node.
    # - For each node, compute if the subtree rooted at that node contains any injected node.
    # - The edges in the minimal Steiner tree are those edges (u,v) such that
    #   the subtree of v (when rooted at u) contains at least one injected node,
    #   and the subtree of u (when rooted at v) contains at least one injected node.
    
    # Let's implement this.
    
    # First, let's root the tree at node 1 and do a DFS to mark which subtrees contain injected nodes.
    visited = [False] * (R + 1)
    contains_injected = [False] * (R + 1)
    
    # Build the tree structure for easier traversal
    tree = defaultdict(list)
    for u, v, w in edges:
        tree[u].append((v, w))
        tree[v].append((u, w))
    
    # First DFS to mark which nodes' subtree contains an injected node
    def dfs1(node, parent):
        visited[node] = True
        if node in injected:
            contains_injected[node] = True
        for nei, cost in tree[node]:
            if not visited[nei]:
                dfs1(nei, node)
                if contains_injected[nei]:
                    contains_injected[node] = True
    
    dfs1(1, -1)
    
    # Second DFS to calculate the minimum cost
    visited2 = [False] * (R + 1)
    total_cost = 0
    
    def dfs2(node, parent):
        visited2[node] = True
        for nei, cost in tree[node]:
            if not visited2[nei]:
                # Recurse first
                dfs2(nei, node)
                # If both the current node's side and the child's side contain injected nodes,
                # we must activate this edge
                if contains_injected[node] and contains_injected[nei]:
                    nonlocal total_cost
                    total_cost += cost
    
    dfs2(1, -1)
    print(total_cost)

if __name__ == "__main__":
    main()