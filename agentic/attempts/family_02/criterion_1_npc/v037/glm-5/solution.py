import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    try:
        n = int(next(it))
        m = int(next(it))
    except StopIteration:
        return
    
    # 2-SAT: variable i is s_i, s_i=1 means ON, s_i=0 means OFF.
    # We model literal x_i as node (i, 1) (true state) and node (i, 0) (false state).
    # Total 2*n nodes. Nodes indexed 0 to 2n-1.
    # Node index: 2*i + (val), where val in {0, 1}.
    
    N = 2 * n
    adj = [[] for _ in range(N)]
    radj = [[] for _ in range(N)]
    
    def get_node_index(var	sign, polarity):
        # var_sign: 1-based index, positive means "task i is ON", negative means "task i is OFF"
        # polarity: 1 if this literal is True, 0 if False (for s_i)
        # returns node index
        task_idx = abs(var_sign) - 1
        # original literal: task is ON (if positive) or OFF (if negative).
        # s_i = 1 means ON.
        # literal (task i is ON) is true  <=> s_i == 1.
        # literal (task i is OFF) is true <=> s_i == 0.
        
        if var_sign > 0: # demands s_i = 1
            target_val = 1
        else: # demands s_i = 0
            target_val = 0
            
        # if polarity is 1, we want the node representing (s_i == target_val)
        # if polarity is 0, we want the node representing (s_i != target_val)
        
        if polarity == 1:
            val = target_val
        else:
            val = 1 - target_val
            
        return 2 * task_idx + val
    
    # Build implication graph
    # Each clause: (l1 OR l2 OR l3)
    # Transform to implications: (not l1 => l2), (not l1 => l3), etc.
    
    for _ in range(m):
        try:
            l1 = int(next(it))
            l2 = int(next(it))
            l3 = int(next(it))
        except StopIteration:
            break
        
        # list of literals
        literals = [l1, l2, l3]
        
        # For each literal, create implication from negation of others to it
        # Clause A or B or C is equivalent to:
        # (not A => B) and (not A => C)
        # (not B => A) and (not B => C)
        # (not C => A) and (not C => B)
        
        # We can iterate pairs: for j in 0..2, for k != j, add edge not lit[j] -> lit[k]
        
        nodes_true = [get_node_index(lit, 1) for lit in literals]
        nodes_false = [get_node_index(lit, 0) for lit in literals] # these are negations
        
        for j in range(3):
            u = nodes_false[j] # source: negation of lit j
            for k in range(3):
                if k == j: continue
                v = nodes_true[k] # destination: lit k
                adj[u].append(v)
                radj[v].append(u)
    
    # Kosaraju's algorithm for SCCs
    visited = [False] * N
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(N):
        if not visited[i]:
            dfs1(i)
    
    comp_id = [-1] * N
    current_comp = 0
    
    def dfs2(u, cid):
        comp_id[u] = cid
        for v in radj[u]:
            if comp_id[v] == -1:
                dfs2(v, cid)
    
    for u in reversed(order):
        if comp_id[u] == -1:
            dfs2(u, current_comp)
            current_comp += 1
    
    # Check for contradictions: x and not x in same SCC
    possible = True
    for i in range(n):
        if comp_id[2*i] == comp_id[2*i + 1]:
            possible = False
            break
    
    if not possible:
        print("NO")
        return
    
    print("YES")
    
    # Construct assignment
    # If comp_id[x] > comp_id[not x], then x should be true.
    # This is because in the condensation graph, if SCC(x) can reach SCC(not x),
    # setting x true would force not x true, a contradiction.
    # We process nodes in topological order (reverse of finishing times).
    # Actually, `order` has nodes in order of increasing finishing time.
    # Reverse `order` gives topological order of SCCs (source first).
    # So if SCC(x) comes earlier than SCC(not x) in reverse(order), comp_id[x] < comp_id[not x].
    # Wait, Kosaraju's second pass processes in reverse finishing order.
    # The first SCC formed (cid=0) is a sink in the condensation graph.
    # The last SCC formed (cid=current_comp-1) is a source.
    # Correct logic: If comp_id[x] > comp_id[not x], SCC(x) is closer to source, should be true.
    
    assignment = [0] * n
    for i in range(n):
        node_true = 2*i + 1
        node_false = 2*i
        if comp_id[node_true] > comp_id[node_false]:
            assignment[i] = 1
        else:
            assignment[i] = 0
            
    print(*(assignment))

if __name__ == '__main__':
    solve()