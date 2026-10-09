import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    k = int(input_data[0])
    t = int(input_data[1])
    
    profiles = []
    for i in range(t):
        x = int(input_data[2 + 3*i])
        y = int(input_data[3 + 3*i])
        z = int(input_data[4 + 3*i])
        profiles.append((x, y, z))
        
    # We need to find a perfect matching in a 3-partite 3-uniform hypergraph.
    # We can reduce this to a 2-SAT problem.
    # For each profile i, we introduce a boolean variable v_i.
    # v_i = True means profile i is selected.
    # Clause 1: At most one profile per operator, terminal, or shift.
    # If two profiles i and j share an operator, terminal, or shift, 
    # they cannot both be selected: (~v_i OR ~v_j).
    # Clause 2: Exactly one profile per operator.
    # For each operator x, let S_x be the set of profiles with operator x.
    # We need exactly one profile in S_x to be selected.
    # This is equivalent to: (OR_{i in S_x} v_i) AND (for all i!=j in S_x, ~v_i OR ~v_j).
    # The pairwise exclusions already enforce the "at most one" part.
    # We just need to add the "at least one" part: (OR_{i in S_x} v_i).
    # Same for terminals and shifts.
    
    N = t
    if N == 0:
        if k == 0:
            print("YES")
        else:
            print("NO")
        return
        
    adj = [[] for _ in range(2 * N)]
    
    # Helper to add implication u -> v
    def add_imp(u, v):
        adj[u].append(v)
        
    def add_or(a, b):
        # a OR b  <=>  ~a -> b  and  ~b -> a
        add_imp(a ^ 1, b)
        add_imp(b ^ 1, a)
        
    # Clause 1: pairwise incompatibilities
    # Group profiles by operator, terminal, and shift
    ops = [[] for _ in range(k + 1)]
    ters = [[] for _ in range(k + 1)]
    shfs = [[] for _ in range(k + 1)]
    
    for i, (x, y, z) in enumerate(profiles):
        ops[x].append(i)
        ters[y].append(i)
        shfs[z].append(i)
        
    for group in ops + ters + shfs:
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                # ~v_i OR ~v_j
                add_or(group[i] ^ 1, group[j] ^ 1)
                
    # Clause 2: at least one profile per operator, terminal, and shift
    for x in range(1, k + 1):
        if not ops[x]:
            print("NO")
            return
        clause = [v for v in ops[x]]
        # To add OR of multiple variables without O(N^2) edges,
        # we use auxiliary variables.
        # v_i OR v_{i+1} OR ... OR v_m
        # We introduce aux_j such that aux_j -> (v_j OR aux_{j+1})
        # and aux_m -> v_m, and we assert aux_1.
        # This takes O(len) edges.
        
        prev = clause[0]
        for i in range(1, len(clause)):
            aux = N
            N += 1
            adj.append([])
            adj.append([])
            # aux -> prev OR clause[i]
            # ~aux -> prev OR clause[i]
            # ~aux -> prev
            add_imp(aux ^ 1, prev)
            # ~aux -> clause[i]
            add_imp(aux ^ 1, clause[i])
            # prev -> aux
            add_imp(prev, aux)
            # clause[i] -> aux
            add_imp(clause[i], aux)
            prev = aux
        # Assert the final auxiliary variable
        add_imp(prev ^ 1, prev)
        
    for y in range(1, k + 1):
        if not ters[y]:
            print("NO")
            return
        clause = [v for v in ters[y]]
        prev = clause[0]
        for i in range(1, len(clause)):
            aux = N
            N += 1
            adj.append([])
            adj.append([])
            add_imp(aux ^ 1, prev)
            add_imp(aux ^ 1, clause[i])
            add_imp(prev, aux)
            add_imp(clause[i], aux)
            prev = aux
        add_imp(prev ^ 1, prev)
        
    for z in range(1, k + 1):
        if not shfs[z]:
            print("NO")
            return
        clause = [v for v in shfs[z]]
        prev = clause[0]
        for i in range(1, len(clause)):
            aux = N
            N += 1
            adj.append([])
            adj.append([])
            add_imp(aux ^ 1, prev)
            add_imp(aux ^ 1, clause[i])
            add_imp(prev, aux)
            add_imp(clause[i], aux)
            prev = aux
        add_imp(prev ^ 1, prev)
        
    # Kosaraju's algorithm for 2-SAT
    # 1. Get topological order of nodes in the original graph
    visited = [False] * (2 * N)
    order = []
    
    sys.setrecursionlimit(max(200000, 2 * N + 10))
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
        
    for i in range(2 * N):
        if not visited[i]:
            dfs1(i)
            
    # 2. Process in reverse topological order on the reversed graph
    rev_adj = [[] for _ in range(2 * N)]
    for u in range(2 * N):
        for v in adj[u]:
            rev_adj[v].append(u)
            
    comp_id = [-1] * (2 * N)
    cid = 0
    
    def dfs2(u, cid):
        comp_id[u] = cid
        for v in rev_adj[u]:
            if comp_id[v] == -1:
                dfs2(v, cid)
                
    for u in reversed(order):
        if comp_id[u] == -1:
            dfs2(u, cid)
            cid += 1
            
    # 3. Check for contradictions and find assignment
    assignment = [False] * t
    for i in range(t):
        if comp_id[2 * i] == comp_id[2 * i + 1]:
            print("NO")
            return
        assignment[i] = comp_id[2 * i] > comp_id[2 * i + 1]
        
    # Output the result
    print("YES")
    for i in range(t):
        if assignment[i]:
            print(profiles[i][0], profiles[i][1], profiles[i][2])

if __name__ == '__main__':
    solve()