import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    # q_i = 2*s_i - 1, so s_i=1 -> q_i=+1, s_i=0 -> q_i=-1
    # I(v) = sign(v) * q_{|v|}
    # Constraint: I(l1) + I(l2) >= 0
    
    # Build implication graph on q_i in {+1, -1}
    # q_i = +1 means s_i = 1; q_i = -1 means s_i = 0
    # Node 2*i-1 = q_i=+1, node 2*i = q_i=-1
    
    # For each constraint, enumerate all (q_a, q_b) in {+1,-1}^2 that satisfy it,
    # then for each violating pair, add implication (violating -> satisfying).
    
    # We'll collect edges and run iterative Tarjan SCC + topological assignment.
    
    edges = []
    
    def add_edge(u, v):
        edges.append((u, v))
    
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        a = abs(l1)
        b = abs(l2)
        sa = 1 if l1 > 0 else -1
        sb = 1 if l2 > 0 else -1
        
        # node(q, val): val=+1 -> 2*q-1, val=-1 -> 2*q
        # We'll enumerate all 4 combos
        for qa in (1, -1):
            for qb in (1, -1):
                I1 = sa * qa
                I2 = sb * qb
                if I1 + I2 >= 0:
                    continue
                # (qa, qb) violates. Need implication to a satisfying pair.
                # Find a satisfying pair (ra, rb):
                # Try ra = -qa, rb = qb
                ra, rb = -qa, qb
                if sa*ra + sb*rb >= 0:
                    u = 2*a - (1 if qa == 1 else 0)
                    v = 2*a - (1 if ra == 1 else 0)
                    add_edge(u, v)
                    u2 = 2*b - (1 if qb == 1 else 0)
                    v2 = 2*b - (1 if rb == 1 else 0)
                    add_edge(u2, v2)
                    continue
                # Try ra = qa, rb = -qb
                ra, rb = qa, -qb
                if sa*ra + sb*rb >= 0:
                    u = 2*a - (1 if qa == 1 else 0)
                    v = 2*a - (1 if ra == 1 else 0)
                    add_edge(u, v)
                    u2 = 2*b - (1 if qb == 1 else 0)
                    v2 = 2*b - (1 if rb == 1 else 0)
                    add_edge(u2, v2)
                    continue
                # Try ra = -qa, rb = -qb
                ra, rb = -qa, -qb
                if sa*ra + sb*rb >= 0:
                    u = 2*a - (1 if qa == 1 else 0)
                    v = 2*a - (1 if ra == 1 else 0)
                    add_edge(u, v)
                    u2 = 2*b - (1 if qb == 1 else 0)
                    v2 = 2*b - (1 if rb == 1 else 0)
                    add_edge(u2, v2)
                    continue
                # If none of the three satisfy, then the only satisfying pair
                # is the one with both signs flipped from the violating pair,
                # which we already tried. So no satisfying pair exists? 
                # Actually there are 4 combos total; we tried 3 alternatives.
                # If none satisfy, the constraint is unsatisfiable for this (qa,qb),
                # meaning this (qa,qb) must be forbidden. We can force contradiction
                # by adding edge (u, not_u) so that choosing u forces not_u too,
                # making it impossible.
                u = 2*a - (1 if qa == 1 else 0)
                not_u = 2*a - (1 if qa == -1 else 0)
                add_edge(u, not_u)
                u2 = 2*b - (1 if qb == 1 else 0)
                not_u2 = 2*b - (1 if qb == -1 else 0)
                add_edge(u2, not_u2)
    
    N = 2 * n
    if N == 0:
        print("YES")
        print()
        return
    
    # Build adjacency
    head = [-1] * (N + 1)
    to = []
    nxt = []
    for u, v in edges:
        to.append(v)
        nxt.append(head[u])
        head[u] = len(to) - 1
    
    # Tarjan SCC iterative
    index = 0
    dfn = [0] * (N + 1)
    low = [0] * (N + 1)
    onstack = bytearray(N + 1)
    stk = []
    stk_sz = 0
    # preallocate stack as list
    stk = [0] * N
    bel = [0] * (N + 1)
    scc_cnt = 0
    
    # We'll use an explicit stack for DFS: each element is (node, edge_iter_index)
    call_stack = []
    
    for i in range(1, N + 1):
        if dfn[i] != 0:
            continue
        # start DFS
        call_stack.append((i, head[i]))
        dfn[i] = low[i] = index + 1
        index += 1
        onstack[i] = 1
        stk[stk_sz] = i
        stk_sz += 1
        
        while call_stack:
            u, e = call_stack[-1]
            if e != -1:
                # advance to next edge
                call_stack[-1] = (u, nxt[e])
                v = to[e]
                if dfn[v] == 0:
                    dfn[v] = low[v] = index + 1
                    index += 1
                    onstack[v] = 1
                    stk[stk_sz] = v
                    stk_sz += 1
                    call_stack.append((v, head[v]))
                elif onstack[v]:
                    if dfn[v] < low[u]:
                        low[u] = dfn[v]
            else:
                # finished u
                call_stack.pop()
                if call_stack:
                    pu = call_stack[-1][0]
                    if low[u] < low[pu]:
                        low[pu] = low[u]
                if low[u] == dfn[u]:
                    scc_cnt += 1
                    while True:
                        w = stk[stk_sz - 1]
                        stk_sz -= 1
                        onstack[w] = 0
                        bel[w] = scc_cnt
                        if w == u:
                            break
    
    # Check satisfiability
    for i in range(1, n + 1):
        if bel[2*i - 1] == bel[2*i]:
            print("NO")
            return
    
    # Build condensation graph for topological order
    # We need edges between SCCs
    scc_head = [-1] * (scc_cnt + 1)
    scc_to = []
    scc_nxt = []
    # To avoid duplicate edges, we can use a set per node, but that's heavy.
    # Instead, since we just need topological order, duplicates are fine but may slow.
    # Use a hash set per SCC for dedup.
    # Actually, we can compute topological order via DFS on condensation with dedup using a visited array per SCC.
    # Let's build adjacency with dedup using sets for small, but scc_cnt can be up to N.
    # Use a dict of sets? Might be heavy. Alternative: sort edges and dedup.
    
    # Collect inter-SCC edges
    inter_edges = []
    for u, v in edges:
        bu = bel[u]
        bv = bel[v]
        if bu != bv:
            inter_edges.append((bu, bv))
    
    # Dedup by sorting
    if inter_edges:
        inter_edges.sort()
        unique = []
        prev = None
        for e in inter_edges:
            if e != prev:
                unique.append(e)
                prev = e
        inter_edges = unique
        
        scc_head = [-1] * (scc_cnt + 1)
        scc_to = []
        scc_nxt = []
        for bu, bv in inter_edges:
            scc_to.append(bv)
            scc_nxt.append(scc_head[bu])
            scc_head[bu] = len(scc_to) - 1
    
    # Topological sort via iterative DFS
    order = []
    visited = bytearray(scc_cnt + 1)
    for s in range(1, scc_cnt + 1):
        if visited[s]:
            continue
        # iterative DFS
        st = [(s, scc_head[s])]
        visited[s] = 1
        while st:
            u, e = st[-1]
            if e != -1:
                st[-1] = (u, scc_nxt[e])
                v = scc_to[e]
                if not visited[v]:
                    visited[v] = 1
                    st.append((v, scc_head[v]))
            else:
                order.append(u)
                st.pop()
    
    # order is post-order; reverse for topological order
    comp_val = [0] * (scc_cnt + 1)
    for u in reversed(order):
        if comp_val[u] == 0:
            comp_val[u] = 1
            # find the negation SCC
            # For each node in this SCC, its negation's SCC gets 0
            # We need a mapping from SCC to its negation SCC
            # Build it: for each i, scc of (2i-1) and scc of (2i) are negations
            pass
    
    # Build negation mapping
    neg_scc = [0] * (scc_cnt + 1)
    for i in range(1, n + 1):
        a = bel[2*i - 1]
        b = bel[2*i]
        neg_scc[a] = b
        neg_scc[b] = a
    
    # Assign in reverse topological order
    comp_val = [0] * (scc_cnt + 1)
    for u in reversed(order):
        if comp_val[u] == 0:
            comp_val[u] = 1
            comp_val[neg_scc[u]] = -1
    
    # Now determine s_i
    # q_i = +1 if comp_val[bel[2i-1]] == 1 else -1
    # s_i = 1 if q_i == +1 else 0
    ans = []
    for i in range(1, n + 1):
        node_pos = 2*i - 1
        if comp_val[bel[node_pos]] == 1:
            ans.append('1')
        else:
            ans.append('0')
    
    print("YES")
    print(' '.join(ans))

solve()