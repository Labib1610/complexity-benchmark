import sys
from collections import defaultdict
import heapq

def main():
    import sys
    import threading
    
    def solve():
        n, m, t = map(int, sys.stdin.readline().split())
        T = list(map(int, sys.stdin.readline().split()))
        
        # If t == n, then for any S such that S ∩ T ≠ ∅ and T \ S ≠ ∅,
        # we have S ∩ T ≠ ∅ and T \ S ≠ ∅ implies S ≠ ∅ and S ≠ U.
        # But since T = U, T \ S ≠ ∅ means S ≠ U, and S ∩ T ≠ ∅ means S ≠ ∅.
        # So the condition becomes: for all S with ∅ ⊂ S ⊂ U, there exists an edge crossing the cut (S, U\S).
        # This is satisfied by any spanning tree. Since m=n-1 and all edges are available,
        # any spanning tree works. Minimum cost is the MST.
        if t == n:
            edges = []
            for _ in range(m):
                u, v, w = map(int, sys.stdin.readline().split())
                edges.append((w, u, v))
            # Compute MST using Kruskal's algorithm
            parent = list(range(n+1))
            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]
            def union(x, y):
                px, py = find(x), find(y)
                if px == py:
                    return False
                parent[px] = py
                return True
            edges.sort()
            total_cost = 0
            for w, u, v in edges:
                if union(u, v):
                    total_cost += w
            print(total_cost)
            return
        
        # If t < n, we need to ensure that for every S such that S ∩ T ≠ ∅ and T \ S ≠ ∅,
        # there exists an activated pair with exactly one element in S.
        # This is equivalent to: for every bipartition (A, T\A) of T where A ≠ ∅ and A ≠ T,
        # there must be an activated edge crossing the cut (S, U\S) where S contains A and not T\A.
        # To satisfy this, for each such bipartition (A, T\A), we need at least one edge
        # connecting a node in A to a node in U \ A (since S contains A and not T\A, so S ∩ T = A).
        # But actually, let's think differently.
        # The condition is: for all S ⊆ U, if S ∩ T ≠ ∅ and T \ S ≠ ∅, then ∃ {u,v} ∈ C s.t. |{u,v} ∩ S| = 1.
        # Let’s define a graph on the elements of T. Two elements in T are connected if there is a path
        # between them using the activated pairs.
        # The condition says: for any bipartition of T into (A, B) with A,B both non-empty,
        # there must be an edge in C crossing this partition.
        # This is equivalent to saying that the activated edges must connect all elements of T,
        # i.e., the subgraph induced by activated edges must connect all nodes in T.
        # So we want a Steiner tree on terminals T, but we're allowed to use other nodes too.
        # However, we are told that taking ALL m=n-1 edges works for ANY S, so the graph is connected.
        # We want the minimum cost subset of edges such that all nodes in T are connected.
        # This is exactly the Minimum Spanning Tree problem on the complete graph restricted to T,
        # but we can use nodes outside T as intermediate points.
        # This is the Euclidean Steiner Tree problem, which is NP-hard in general graphs.
        # But here we are given that the full graph (with m=n-1 edges) satisfies the property for all S.
        # And m=n-1 suggests a tree structure.
        # In fact, the m=n-1 edges form a spanning tree of the entire graph.
        # The condition is that for any S with S ∩ T ≠ ∅ and T \ S ≠ ∅, there is an edge in C
        # that crosses the cut (S, U\S).
        # This is equivalent to: in the graph formed by activated edges, for any bipartition of T
        # into (A,B), there must be an edge crossing this cut.
        # This means that in the activated subgraph, all vertices of T must be connected.
        # So we want the minimum cost set of edges that connects all vertices in T.
        # This is the Minimum Steiner Tree problem with terminals T.
        # But again, we are told that all m=n-1 edges work, so we can build a solution based on that.
        # Let's consider the tree formed by all m=n-1 edges. This is a spanning tree of the full graph.
        # Now, we want to find the minimum cost subset of edges that connects all nodes in T.
        # This is solved by finding the minimal subtree of the full spanning tree that contains all nodes in T.
        # This is called the "Steiner tree" of T within the tree.
        # Algorithm:
        # 1. Build the tree from the m=n-1 edges.
        # 2. Find the minimal subtree that contains all nodes in T.
        #    This is done by finding the union of all paths between pairs of nodes in T.
        #    Or equivalently, root the tree at some node, find the deepest node in T,
        #    and take the union of paths from all nodes in T to their lowest common ancestors.
        #    Actually, simpler: take all edges on the paths between all pairs of nodes in T.
        #    Even simpler: in a tree, the minimal connected subgraph containing a set of nodes
        #    is the union of paths between consecutive nodes in the DFS order of the set.
        #    Or even simpler: it's the subtree that has leaves in T and internal nodes of degree ≥ 2.
        #    The most straightforward way: find the "Steiner tree" of T in the tree.
        #    Algorithm:
        #    - Root the tree at some node.
        #    - For each node in T, mark its path to the root.
        #    - The union of all such paths forms the minimal subtree containing T.
        #    - The cost is the sum over all such marked edges.
        # Implementation:
        # Read all edges
        edges = []
        adj = [[] for _ in range(n+1)]
        for _ in range(m):
            u, v, w = map(int, sys.stdin.readline().split())
            edges.append((w, u, v))
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        # Since m=n-1 and the graph is connected, it's a tree.
        # Build adjacency list for tree traversal.
        # We'll build the tree explicitly.
        # Let's use Union-Find to check connectivity when adding edges, but since m=n-1 and connected, it's a tree.
        # Just pick any node as root and do BFS/DFS to build parent relationships.
        # Let's root the tree at node 1.
        parent_edge = [None] * (n+1)
        visited = [False] * (n+1)
        queue = [1]
        visited[1] = True
        tree_adj = [[] for _ in range(n+1)]
        while queue:
            u = queue.pop()
            for v, w in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent_edge[v] = (u, w)
                    tree_adj[u].append((v, w))
                    tree_adj[v].append((u, w))
                    queue.append(v)
        
        # Now we have a tree rooted (implicitly) at node 1.
        # We need to find the minimal subtree that contains all nodes in T.
        # Algorithm: Mark all nodes in T as "terminals".
        # Do a DFS to compute for each node whether its subtree contains any terminal.
        # Then, include an edge in the solution if it connects two subtrees that both contain terminals,
        # or if one subtree contains terminals and the other is the parent direction and also leads to terminals.
        # Simpler approach:
        # Do a post-order DFS. For each node, compute:
        # - does its subtree contain any terminal?
        # - what is the cost of the minimal subtree in its subtree that connects all terminals in its subtree?
        # But we just want to find which edges are needed.
        # Let's do this:
        # 1. Do a post-order DFS.
        # 2. For each node, count how many terminals are in its subtree.
        # 3. An edge is included if it connects a subtree with count > 0 to another subtree with count > 0,
        #    OR if one side has count > 0 and the other side is towards the rest of the tree and also leads to terminals.
        # Actually, let's think of it this way:
        # We want the subtree that spans all terminals.
        # In a tree, this is the union of paths between all pairs of terminals.
        # But we can compute it more efficiently:
        # Root the tree at some node.
        # For each node, compute whether its subtree contains any terminal.
        # An edge is in the Steiner tree if it connects two parts that both contain terminals.
        # Let's implement this.
        
        terminals = set(T)
        contains_terminal = [False] * (n+1)
        # We'll do a post-order traversal to compute 'contains_terminal'
        # We already have the tree structure in tree_adj.
        # Let's do DFS from node 1.
        # We need to traverse the tree and compute for each edge if it should be included.
        # Let's do a DFS that returns whether the subtree contains any terminal,
        # and accumulates the cost of necessary edges.
        
        total_cost = [0]
        
        def dfs(u, parent):
            has_terminal = u in terminals
            for v, w in tree_adj[u]:
                if v == parent:
                    continue
                child_has_terminal = dfs(v, u)
                if child_has_terminal and has_terminal:
                    total_cost[0] += w
                has_terminal |= child_has_terminal
            return has_terminal
        
        dfs(1, -1)
        print(total_cost[0])
    
    threading.Thread(target=solve).start()

if __name__ == "__main__":
    main()