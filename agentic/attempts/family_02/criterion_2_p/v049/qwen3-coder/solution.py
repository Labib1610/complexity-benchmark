import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # If no directives, any configuration works
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build implication graph for 2-SAT
    # Variables: 0 to n-1 for Focused, n to 2n-1 for Diffused
    # But we'll use a more direct approach with implications
    
    # For each installation i:
    # var[i] = True means Focused, var[i] = False means Diffused
    # We'll build a graph where each node represents a literal
    # Positive literal: 2*i for Focused, Negative literal: 2*i+1 for Diffused
    
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        # Convert to 0-indexed and get variable and sign
        if l1 > 0:
            var1, sign1 = l1 - 1, 0  # Focused
        else:
            var1, sign1 = -l1 - 1, 1  # Diffused
            
        if l2 > 0:
            var2, sign2 = l2 - 1, 0  # Focused
        else:
            var2, sign2 = -l2 - 1, 1  # Diffused
        
        # Clause: (sign1[var1] OR sign2[var2])
        # Equivalent to: (!sign1[var1] -> sign2[var2]) AND (!sign2[var2] -> sign1[var1])
        
        # !sign1[var1] is (1-sign1)[var1] which is node 2*var1 + (1-sign1)
        # sign2[var2] is node 2*var2 + sign2
        adj[2*var1 + (1-sign1)].append(2*var2 + sign2)
        adj[2*var2 + (1-sign2)].append(2*var1 + sign1)
        
        rev_adj[2*var2 + sign2].append(2*var1 + (1-sign1))
        rev_adj[2*var1 + sign1].append(2*var2 + (1-sign2))
    
    # Kosaraju's algorithm for SCC
    visited = [False] * (2*n)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(2*n):
        if not visited[i]:
            dfs1(i)
    
    # Second DFS on transpose graph
    visited = [False] * (2*n)
    scc_id = [-1] * (2*n)
    scc_count = 0
    
    def dfs2(u):
        visited[u] = True
        scc_id[u] = scc_count
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v)
    
    while order:
        u = order.pop()
        if not visited[u]:
            dfs2(u)
            scc_count += 1
    
    # Check if satisfiable
    for i in range(n):
        if scc_id[2*i] == scc_id[2*i + 1]:
            print("NO")
            return
    
    # Assign values based on SCC topological order
    result = [0] * n
    # In Kosaraju, later finishing times in first DFS correspond to sources in condensation
    # So we process SCCs in reverse order of their ids
    scc_order = sorted(range(scc_count), key=lambda x: -sum(1 for i in range(2*n) if scc_id[i] == x))
    
    assigned = [False] * n
    
    for comp in range(scc_count):
        literals = [i for i in range(2*n) if scc_id[i] == comp]
        for lit in literals:
            var = lit // 2
            if not assigned[var]:
                if lit % 2 == 0:  # Focused
                    result[var] = 1
                else:  # Diffused
                    result[var] = 0
                assigned[var] = True
    
    print("YES")
    print(" ".join(map(str, result)))

solve()