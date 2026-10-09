import sys
from collections import defaultdict

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    constraints = []
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        constraints.append((l1, l2))
    return n, m, constraints

def build_graph(n, constraints):
    # Create implication graph for 2-SAT
    # Variables: x_i represents s_i = 1
    # For constraint l1, l2:
    # If l1 > 0 and l2 > 0: (not x_l1 or x_l2) and (not x_l2 or x_l1)
    # If l1 > 0 and l2 < 0: (not x_l1 or not x_|l2|) and (x_|l2| or x_l1)
    # If l1 < 0 and l2 > 0: (x_|l1| or x_l2) and (not x_l2 or not x_|l1|)
    # If l1 < 0 and l2 < 0: (x_|l1| or not x_|l2|) and (x_|l2| or not x_|l1|)
    
    # We'll use node IDs: for variable i (1-indexed): 
    # node 2*i represents x_i (s_i = 1)
    # node 2*i+1 represents not x_i (s_i = 0)
    
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    for l1, l2 in constraints:
        # Convert to 0-based indexing for variables
        v1, v2 = abs(l1)-1, abs(l2)-1
        # For each constraint I(l1) + I(l2) >= 0
        # This means q_|l1| * sign(l1) + q_|l2| * sign(l2) >= 0
        # Since q_i = 2*s_i - 1, we have:
        # (2*s_|l1| - 1)*sign(l1) + (2*s_|l2| - 1)*sign(l2) >= 0
        # 2*s_|l1|*sign(l1) - sign(l1) + 2*s_|l2|*sign(l2) - sign(l2) >= 0
        # 2*(s_|l1|*sign(l1) + s_|l2|*sign(l2)) >= sign(l1) + sign(l2)
        
        # Since s_i is 0 or 1, s_i*sign can be: -1, 0, 1
        # But since l1,l2 are non-zero, sign is -1 or 1
        # So s_|l1|*sign(l1) is either 0 or sign(l1)
        # The constraint becomes: s_|l1|*sign(l1) + s_|l2|*sign(l2) >= (sign(l1)+sign(l2))/2
        
        # Let's think differently. q_i = 2s_i - 1 => s_i = (q_i + 1)/2
        # I(l1) + I(l2) = sign(l1)*q_|l1| + sign(l2)*q_|l2| >= 0
        # = sign(l1)*(2s_|l1| - 1) + sign(l2)*(2s_|l2| - 1) >= 0
        # = 2(sign(l1)s_|l1| + sign(l2)s_|l2|) - sign(l1) - sign(l2) >= 0
        # => sign(l1)s_|l1| + sign(l2)s_|l2| >= (sign(l1) + sign(l2))/2
        
        # Since s_i is boolean, this is a linear constraint over booleans.
        # Let's enumerate cases:
        # Case 1: l1>0, l2>0: s_|l1| + s_|l2| >= 1
        #         Meaning at least one of them is 1
        #         Clause: (s_|l1| or s_|l2|)
        # Case 2: l1>0, l2<0: s_|l1| - s_|l2| >= 0
        #         Meaning s_|l1| >= s_|l2|
        #         Clause: (not s_|l1| or s_|l2|)
        # Case 3: l1<0, l2>0: -s_|l1| + s_|l2| >= 0
        #         Meaning s_|l2| >= s_|l1|
        #         Clause: (s_|l1| or not s_|l2|)
        # Case 4: l1<0, l2<0: -s_|l1| - s_|l2| >= -1
        #         Meaning s_|l1| + s_|l2| <= 1
        #         Clause: (not s_|l1| or not s_|l2|)
        
        if l1 > 0 and l2 > 0:
            # s_|l1| or s_|l2| 
            # not(not s_|l1| and not s_|l2|)
            # Add implications: not s_|l1| => s_|l2|, not s_|l2| => s_|l1|
            adj[2*v1 + 1].append(2*v2)      # not s_|l1| implies s_|l2|
            adj[2*v2 + 1].append(2*v1)      # not s_|l2| implies s_|l1|
            rev_adj[2*v2].append(2*v1 + 1)
            rev_adj[2*v1].append(2*v2 + 1)
            
        elif l1 > 0 and l2 < 0:
            # s_|l1| >= s_|l2|
            # not s_|l1| => not s_|l2|
            adj[2*v1 + 1].append(2*v2 + 1)   # not s_|l1| implies not s_|l2|
            adj[2*v2].append(2*v1)          # s_|l2| implies s_|l1|
            rev_adj[2*v2 + 1].append(2*v1 + 1)
            rev_adj[2*v1].append(2*v2)
            
        elif l1 < 0 and l2 > 0:
            # s_|l2| >= s_|l1|
            # not s_|l2| => not s_|l1|
            adj[2*v2 + 1].append(2*v1 + 1)  # not s_|l2| implies not s_|l1|
            adj[2*v1].append(2*v2)          # s_|l1| implies s_|l2|
            rev_adj[2*v1 + 1].append(2*v2 + 1)
            rev_adj[2*v2].append(2*v1)
            
        else:  # l1 < 0 and l2 < 0
            # s_|l1| + s_|l2| <= 1
            # not(s_|l1| and s_|l2|)
            # Add implications: s_|l1| => not s_|l2|, s_|l2| => not s_|l1|
            adj[2*v1].append(2*v2 + 1)      # s_|l1| implies not s_|l2|
            adj[2*v2].append(2*v1 + 1)      # s_|l2| implies not s_|l1|
            rev_adj[2*v2 + 1].append(2*v1)
            rev_adj[2*v1 + 1].append(2*v2)

    return adj, rev_adj

def kosaraju(n, adj, rev_adj):
    # First DFS to get finishing times
    visited = [False] * (2 * n)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    # Second DFS on transpose graph
    visited_t = [False] * (2 * n)
    components = [-1] * (2 * n)
    component_id = 0
    
    def dfs2(u, cid):
        visited_t[u] = True
        components[u] = cid
        for v in rev_adj[u]:
            if not visited_t[v]:
                dfs2(v, cid)
    
    # Run first DFS
    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)
    
    # Run second DFS in reverse finish order
    for u in reversed(order):
        if not visited_t[u]:
            dfs2(u, component_id)
            component_id += 1
            
    return components

def solve():
    n, m, constraints = read_input()
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    adj, rev_adj = build_graph(n, constraints)
    components = kosaraju(n, adj, rev_adj)
    
    # Check if satisfiable
    for i in range(n):
        if components[2*i] == components[2*i + 1]:
            print("NO")
            return
    
    # Extract solution
    assignment = [0] * n
    for i in range(n):
        # If not x_i is in a later component than x_i, then x_i is true (s_i = 1)
        if components[2*i + 1] > components[2*i]:
            assignment[i] = 1
    
    print("YES")
    print(" ".join(map(str, assignment)))

solve()