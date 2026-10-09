import sys
from collections import defaultdict

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each forecast (a or b), we build implications
    # We'll use 2-SAT approach.
    # Variables: x1, x2, ..., xn (xi = 1 means "buy", xi = 0 means "sell")
    # For each clause (a or b), we add edges:
    # (~a => b) and (~b => a) in implication graph
    
    # Node IDs: for variable i (1-based), 
    # node 2*i represents xi (positive literal)
    # node 2*i+1 represents ~xi (negative literal)
    # But in our case, variables can be negative, so:
    # for a literal x: if x > 0, variable is x, value is True
    #                  if x < 0, variable is -x, value is False
    
    adj = defaultdict(list)
    
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        
        # Clause: (l1 or l2)
        # This is equivalent to (~l1 => l2) and (~l2 => l1)
        
        # Convert literals to nodes in implication graph
        # Function to get node id from literal
        def lit_to_node(lit):
            var = abs(lit)
            val = lit > 0
            # node id: 2*var + (0 if val else 1)
            # i.e., 2*var for positive literal (variable=True)
            #       2*var+1 for negative literal (variable=False)
            return 2 * var + (0 if val else 1)
        
        # ~l1 => l2
        adj[lit_to_node(-l1)].append(lit_to_node(l2))
        # ~l2 => l1
        adj[lit_to_node(-l2)].append(lit_to_node(l1))
    
    # Now we do 2-SAT using Kosaraju's algorithm to find SCCs
    # and check if for any variable xi, both xi and ~xi are in same SCC
    
    # Build reverse graph
    radj = defaultdict(list)
    for u in adj:
        for v in adj[u]:
            radj[v].append(u)
    
    # First DFS to get finishing times
    visited = [False] * (2 * (n + 1))
    finish_stack = []
    
    def dfs1(u):
        if visited[u]:
            return
        visited[u] = True
        for v in adj[u]:
            dfs1(v)
        finish_stack.append(u)
    
    for i in range(1, n + 1):
        # Check both xi and ~xi (nodes 2*i and 2*i+1)
        if not visited[2 * i]:
            dfs1(2 * i)
        if not visited[2 * i + 1]:
            dfs1(2 * i + 1)
    
    # Second DFS on reverse graph in order of decreasing finishing time
    visited = [False] * (2 * (n + 1))
    scc_id = [0] * (2 * (n + 1))
    scc_count = 0
    
    def dfs2(u):
        if visited[u]:
            return
        visited[u] = True
        scc_id[u] = scc_count
        for v in radj[u]:
            dfs2(v)
    
    while finish_stack:
        u = finish_stack.pop()
        if not visited[u]:
            scc_count += 1
            dfs2(u)
    
    # Check for contradiction: for any variable i, 
    # if 2*i and 2*i+1 are in same SCC, then unsatisfiable
    for i in range(1, n + 1):
        if scc_id[2 * i] == scc_id[2 * i + 1]:
            print("NO")
            return
    
    # Otherwise, construct solution
    # For each variable, if scc_id[2*i] > scc_id[2*i+1], set xi = True (1)
    # else set xi = False (0)
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        if scc_id[2 * i] > scc_id[2 * i + 1]:
            result[i] = 1
        else:
            result[i] = 0
    
    print("YES")
    print(" ".join(map(str, result[1:])))

if __name__ == "__main__":
    main()