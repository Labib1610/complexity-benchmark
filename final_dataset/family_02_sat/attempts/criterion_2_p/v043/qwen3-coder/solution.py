import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # For each variable x_i, we have two nodes: 2*i (for x_i = 0) and 2*i+1 (for x_i = 1)
    # But it's easier to work with variables: for node i (1-based), 
    # variable index is i-1, so:
    # variable v, value 0 -> node 2*v
    # variable v, value 1 -> node 2*v+1
    
    # But actually, let's think of this as a 2-SAT problem.
    # Each interlock is a clause: (l1 OR l2)
    # We need to convert literals to variable indices in our graph.
    
    # Let's map node-state to variable-value:
    # literal l represents "node |l| in state (l>0)"
    # So:
    # l > 0: node |l| must be in state 1
    # l < 0: node |l| must be in state 0
    
    # For 2-SAT:
    # variable i (0-based) corresponds to node (i+1)
    # variable i, value 0 -> node (i+1) in state 0 -> literal -(i+1)
    # variable i, value 1 -> node (i+1) in state 1 -> literal +(i+1)
    
    # In implication graph:
    # for clause (a OR b), we add edges (!a -> b) and (!b -> a)
    
    # Let's define:
    # for node i (1-based):
    # literal +i means node i in state 1
    # literal -i means node i in state 0
    
    # So for variable x_j (j from 0 to n-1), corresponding to node (j+1):
    # x_j = 0 -> literal -(j+1)
    # x_j = 1 -> literal +(j+1)
    
    # But in our standard 2-SAT implementation, it's easier to work with 0-based variables.
    # Let's use:
    # variable v (0 <= v < n) corresponds to node (v+1)
    # literal (2*v)   corresponds to "node (v+1) in state 0" (i.e., variable v is False)
    # literal (2*v+1) corresponds to "node (v+1) in state 1" (i.e., variable v is True)
    
    adj = [[] for _ in range(2 * n)]
    rev_adj = [[] for _ in range(2 * n)]
    
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        # Convert to 0-based variable indices and literal indices
        # l1 is a literal: +k means node k in state 1, -k means node k in state 0
        def lit_to_idx(l):
            node = abs(l) - 1  # 0-based
            if l > 0:
                return 2 * node + 1  # node in state 1
            else:
                return 2 * node      # node in state 0
        
        idx1 = lit_to_idx(l1)
        idx2 = lit_to_idx(l2)
        
        # Clause (l1 OR l2) is equivalent to (!l1 -> l2) and (!l2 -> l1)
        not_idx1 = idx1 ^ 1
        not_idx2 = idx2 ^ 1
        
        adj[not_idx1].append(idx2)
        adj[not_idx2].append(idx1)
        rev_adj[idx2].append(not_idx1)
        rev_adj[idx1].append(not_idx2)
    
    # Kosaraju's algorithm for SCC
    order = []
    visited = [False] * (2 * n)
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)
    
    # Second DFS on reverse graph
    comp = [-1] * (2 * n)
    num_scc = 0
    
    def dfs2(u):
        comp[u] = num_scc
        for v in rev_adj[u]:
            if comp[v] == -1:
                dfs2(v)
    
    for i in reversed(order):
        if comp[i] == -1:
            dfs2(i)
            num_scc += 1
    
    # Check if satisfiable
    for i in range(n):
        # variable i: literals are 2*i (False) and 2*i+1 (True)
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
    
    # Build solution
    # In the implication graph, if comp[2*i+1] > comp[2*i], then x_i should be True (state 1)
    # else x_i should be False (state 0)
    result = []
    for i in range(n):
        if comp[2*i+1] > comp[2*i]:
            result.append(1)
        else:
            result.append(0)
    
    print("YES")
    print(' '.join(map(str, result)))

threading.Thread(target=main).start()