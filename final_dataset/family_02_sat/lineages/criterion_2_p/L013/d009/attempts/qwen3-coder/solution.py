import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # We will build a graph where each node is a variable (s_i or ~s_i)
    # and edges represent constraints.
    # Each s_i can be represented as a boolean variable.
    # We'll use 2*i for s_i (False) and 2*i+1 for ~s_i (True)
    
    # For each brace (l1, l2), the total displacement must NOT be -2.
    # Let's analyze what makes displacement -2:
    # Each connection contributes:
    #   if l > 0: +1 if s_{|l|}=1, -1 if s_{|l|}=0
    #   if l < 0: +1 if s_{|l|}=0, -1 if s_{|l|}=1
    # So total = contribution from l1 + contribution from l2
    # Displacement = -2 happens when both contributions are -1.
    # So we need to forbid the cases where both connections contribute -1.
    
    # For each brace, we'll derive a constraint.
    # Let's define boolean variables:
    # x_i = s_i (i.e., x_i = True means s_i = 1)
    
    # For a brace with connections l1 and l2:
    # Contribution of l1:
    #   if l1 > 0: +1 if x_{|l1|} is True, -1 if False
    #   if l1 < 0: +1 if x_{|l1|} is False, -1 if True
    # Similarly for l2.
    
    # So contribution_l1 = 2 * ( (l1>0) == x_{|l1|} ) - 1
    # contribution_l2 = 2 * ( (l2>0) == x_{|l2|} ) - 1
    # Total = contribution_l1 + contribution_l2
    # We want Total != -2, i.e., NOT (contribution_l1 = -1 AND contribution_l2 = -1)
    # contribution_l1 = -1 iff (l1>0) != x_{|l1|}
    # contribution_l2 = -1 iff (l2>0) != x_{|l2|}
    # So we forbid: ( (l1>0) != x_{|l1|} ) AND ( (l2>0) != x_{|l2|} )
    # This is equivalent to: NOT( (l1>0) != x_{|l1|} ) OR NOT( (l2>0) != x_{|l2|} )
    # Which is: ( (l1>0) == x_{|l1|} ) OR ( (l2>0) == x_{|l2|} )
    # In terms of boolean variables:
    # Let a = x_{|l1|}, b = x_{|l2|}
    # We want: ( (l1>0) == a ) OR ( (l2>0) == b )
    # This is a clause in 2-SAT.
    
    # Let's build the 2-SAT instance.
    # Variables: x_1, ..., x_n (x_i represents s_i = 1)
    # For each variable x_i, we use index 2*i for x_i (False) and 2*i+1 for ~x_i (True)
    # i.e., for variable i (1-based), False is 2*i, True is 2*i+1
    
    def var(i, neg):
        # i is 1-based strut index
        # neg: True means we want ~x_i, False means x_i
        return 2 * i + (1 if neg else 0)
    
    # Clauses: list of pairs (a, b) meaning a OR b
    clauses = []
    
    idx = 2
    for _ in range(m):
        l1 = int(data[idx])
        l2 = int(data[idx+1])
        idx += 2
        
        # We want: ( (l1>0) == x_{|l1|} ) OR ( (l2>0) == x_{|l2|} )
        # Let a = (l1>0) == x_{|l1|}
        #     b = (l2>0) == x_{|l2|}
        # We want a OR b
        
        # a is True iff (l1>0) == x_{|l1|}
        # This is equivalent to: (l1>0) XOR x_{|l1|} == False
        # Which is: (l1>0) == x_{|l1|}
        # In terms of literals:
        # If l1>0, then a = x_{|l1|} = x_{l1}
        # If l1<0, then a = ~x_{|l1|} = ~x_{-l1}
        # Similarly for b.
        
        # So the clause is:
        # If l1>0: x_{l1} OR ( (l2>0) == x_{|l2|} )
        # If l1<0: ~x_{-l1} OR ( (l2>0) == x_{|l2|} )
        # And symmetrically for l2.
        
        # Let's define the literals:
        # For l1:
        abs_l1 = abs(l1)
        sign_l1 = l1 > 0
        # literal for (l1>0) == x_{|l1|}
        # If sign_l1 is True (l1>0), we want x_{abs_l1}
        # If sign_l1 is False (l1<0), we want ~x_{abs_l1}
        lit1 = var(abs_l1, not sign_l1)  # because var(i, True) gives ~x_i
        
        # For l2:
        abs_l2 = abs(l2)
        sign_l2 = l2 > 0
        lit2 = var(abs_l2, not sign_l2)
        
        # Add clause: lit1 OR lit2
        clauses.append((lit1, lit2))
    
    # Now we solve 2-SAT
    # Number of variables: n
    # Variables are 1-based indices for struts, but in 2-SAT solver we use 0-based for simplicity
    # Actually, our var() function uses 1-based strut index and returns literal index
    # Literal indices are 2*i and 2*i+1 for i from 1 to n
    # So total literal indices up to 2*n+1
    
    # Let's build implication graph
    # Nodes: 0 to 2*n+1 (for literals 2*1 to 2*n+1)
    # But we need to map literal indices to node indices
    # Let's just use literal indices directly as node indices
    
    adj = defaultdict(list)
    adj_rev = defaultdict(list)
    
    for (a, b) in clauses:
        # Clause a OR b is equivalent to (~a => b) and (~b => a)
        # Literal indices are like 2*i and 2*i+1
        # To get negation: 2*i <-> 2*i+1
        not_a = a ^ 1
        not_b = b ^ 1
        adj[not_a].append(b)
        adj_rev[b].append(not_a)
        adj[not_b].append(a)
        adj_rev[a].append(not_b)
    
    # Kosaraju's algorithm for SCC
    visited = [False] * (2 * n + 2)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(2, 2*n + 2):
        if not visited[i]:
            dfs1(i)
    
    # Second DFS on reverse graph
    visited = [False] * (2 * n + 2)
    scc_id = [-1] * (2 * n + 2)
    scc_count = 0
    
    def dfs2(u):
        visited[u] = True
        scc_id[u] = scc_count
        for v in adj_rev[u]:
            if not visited[v]:
                dfs2(v)
    
    while order:
        u = order.pop()
        if not visited[u]:
            dfs2(u)
            scc_count += 1
    
    # Check if satisfiable
    for i in range(1, n + 1):
        lit_false = 2 * i       # x_i = False
        lit_true = 2 * i + 1    # x_i = True
        if scc_id[lit_false] == scc_id[lit_true]:
            print("NO")
            return
    
    # Extract solution
    # Assign True to the literal whose SCC comes later in topological order
    # We can use the fact that in Kosaraju, SCCs are in reverse topological order
    # So higher scc_id means later in topological order of SCC DAG
    assignment = [None] * (n + 1)
    for i in range(1, n + 1):
        lit_false = 2 * i
        lit_true = 2 * i + 1
        if scc_id[lit_true] > scc_id[lit_false]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    print("YES")
    print(" ".join(map(str, assignment[1:])))

if __name__ == "__main__":
    main()