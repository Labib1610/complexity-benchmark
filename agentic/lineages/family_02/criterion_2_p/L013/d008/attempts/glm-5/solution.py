import sys
sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    # Build implication graph for 2-SAT
    # Variables: s[1..n], represented as 2*i for s[i]=false, 2*i+1 for s[i]=true
    # For each detector, we need at least one manifold to deliver Isotope-1
    
    adj = [[] for _ in range(2 * n)]
    
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        
        # Determine which literal corresponds to "delivers Isotope-1"
        # For positive l: s[|l|] = 1 delivers Isotope-1
        # For negative l: s[|l|] = 0 delivers Isotope-1
        
        def get_literal(l):
            idx = abs(l) - 1
            if l > 0:
                # s[idx] = 1 delivers Isotope-1, literal is s[idx]
                return (2 * idx, 2 * idx + 1)  # (false node, true node)
            else:
                # s[idx] = 0 delivers Isotope-1, literal is NOT s[idx]
                return (2 * idx + 1, 2 * idx)  # (false node, true node)
        
        lit1_false, lit1_true = get_literal(l1)
        lit2_false, lit2_true = get_literal(l2)
        
        # Clause: lit1 OR lit2
        # Implications: NOT lit1 -> lit2, NOT lit2 -> lit1
        adj[lit1_false].append(lit2_true)
        adj[lit2_false].append(lit1_true)
    
    # Tarjan's SCC
    index = 0
    stack = []
    on_stack = [False] * (2 * n)
    indices = [-1] * (2 * n)
    lowlink = [0] * (2 * n)
    scc_id = [-1] * (2 * n)
    scc_count = 0
    
    def strongconnect(v):
        nonlocal index, scc_count
        indices[v] = index
        lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack[v] = True
        
        for w in adj[v]:
            if indices[w] == -1:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], indices[w])
        
        if lowlink[v] == indices[v]:
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc_id[w] = scc_count
                if w == v:
                    break
            scc_count += 1
    
    for v in range(2 * n):
        if indices[v] == -1:
            strongconnect(v)
    
    # Check if any variable and its negation are in the same SCC
    for i in range(n):
        if scc_id[2 * i] == scc_id[2 * i + 1]:
            print("NO")
            return
    
    # Assign values: if scc_id[false] > scc_id[true], set to true
    # (process in reverse topological order of SCCs)
    result = [0] * n
    for i in range(n):
        if scc_id[2 * i] < scc_id[2 * i + 1]:
            result[i] = 1
    
    print("YES")
    print(" ".join(map(str, result)))

solve()