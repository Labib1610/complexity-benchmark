import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
        
    num_vars = 3 * m
    
    def var_id(e, c):
        return e * 3 + c + 1
    
    clauses = []
    
    # 1. Each edge has at least one color and at most one color
    for e in range(m):
        v0, v1, v2 = var_id(e, 0), var_id(e, 1), var_id(e, 2)
        clauses.append([v0, v1, v2])
        clauses.append([-v0, -v1])
        clauses.append([-v0, -v2])
        clauses.append([-v1, -v2])
        
    # 2. At each vertex, no two incident edges have the same color
    for u in range(1, n + 1):
        inc = adj[u]
        if len(inc) == 3:
            e1, e2, e3 = inc
            for c in range(3):
                v1, v2, v3 = var_id(e1, c), var_id(e2, c), var_id(e3, c)
                clauses.append([-v1, -v2])
                clauses.append([-v1, -v3])
                clauses.append([-v2, -v3])

    # Symmetry breaking on first vertex
    if m > 0 and len(adj[1]) == 3:
        e1, e2, e3 = adj[1]
        clauses.append([var_id(e1, 0)])
        clauses.append([var_id(e2, 1)])
        clauses.append([var_id(e3, 2)])

    # CDCL SAT Solver
    assign = [0] * (num_vars + 1)
    level = [0] * (num_vars + 1)
    reason = [-1] * (num_vars + 1)
    activity = [0.0] * (num_vars + 1)
    var_inc = 1.0
    
    # Watches: watches[lit] = list of clause indices
    # Literal mapping: lit > 0 -> lit, lit < 0 -> num_vars - lit
    def lit_to_idx(lit):
        return lit if lit > 0 else num_vars - lit

    watches = [[] for _ in range(2 * num_vars + 1)]
    
    for c_idx, c in enumerate(clauses):
        if len(c) >= 2:
            watches[lit_to_idx(c[0])].append(c_idx)
            watches[lit_to_idx(c[1])].append(c_idx)
        elif len(c) == 1:
            watches[lit_to_idx(c[0])].append(c_idx)
            
    trail = []
    trail_lim = []
    q_head = 0
    decision_level = 0
    
    def val(lit):
        v = abs(lit)
        a = assign[v]
        return a if lit > 0 else -a

    def assign_lit(lit, r):
        v = abs(lit)
        assign[v] = 1 if lit > 0 else -1
        level[v] = decision_level
        reason[v] = r
        trail.append(lit)

    def propagate():
        nonlocal q_head
        while q_head < len(trail):
            p = trail[q_head]
            q_head += 1
            neg_p = -p
            w_idx = lit_to_idx(neg_p)
            w_list = watches[w_idx]
            new_w_list = []
            
            conflict = -1
            for i in range(len(w_list)):
                c_idx = w_list[i]
                c = clauses[c_idx]
                
                if len(c) == 1:
                    if val(c[0]) == -1:
                        conflict = c_idx
                        new_w_list.extend(w_list[i:])
                        break
                    new_w_list.append(c_idx)
                    continue
                
                if c[0] == neg_p:
                    c[0], c[1] = c[1], c[0]
                    
                if val(c[0]) == 1:
                    new_w_list.append(c_idx)
                    continue
                
                found = False
                for k in range(2, len(c)):
                    if val(c[k]) != -1:
                        c[1], c[k] = c[k], c[1]
                        watches[lit_to_idx(c[1])].append(c_idx)
                        found = True
                        break
                        
                if found:
                    continue
                    
                new_w_list.append(c_idx)
                if val(c[0]) == -1:
                    conflict = c_idx
                    new_w_list.extend(w_list[i+1:])
                    break
                else:
                    assign_lit(c[0], c_idx)
                    
            watches[w_idx] = new_w_list
            if conflict != -1:
                return conflict
        return -1

    def backtrack_to(bt_level):
        nonlocal decision_level, q_head
        while trail_lim and len(trail_lim) > bt_level:
            target = trail_lim.pop()
            while len(trail) > target:
                p = trail.pop()
                assign[abs(p)] = 0
        decision_level = bt_level
        q_head = len(trail)

    # Initial propagation of unit clauses
    for c_idx, c in enumerate(clauses):
        if len(c) == 1:
            lit = c[0]
            if val(lit) == -1:
                print("NO")
                return
            if val(lit) == 0:
                assign_lit(lit, c_idx)
                
    if propagate() != -1:
        print("NO")
        return

    # Priority queue for decisions
    heap = [(-activity[i], i) for i in range(1, num_vars + 1)]
    heapq.heapify(heap)

    def pick_branching_var():
        while heap:
            act, v = heapq.heappop(heap)
            if assign[v] == 0:
                return v
        return 0

    seen = [False] * (num_vars + 1)
    
    while True:
        v = pick_branching_var()
        if v == 0:
            # SAT found!
            break
            
        decision_level += 1
        trail_lim.append(len(trail))
        assign_lit(v, -1)
        
        while True:
            confl = propagate()
            if confl == -1:
                break
                
            if decision_level == 0:
                print("NO")
                return
                
            # Conflict analysis
            learnt = []
            counter = 0
            p = None
            c = clauses[confl]
            idx = len(trail) - 1
            
            while True:
                for lit in c:
                    var = abs(lit)
                    if not seen[var] and level[var] > 0:
                        seen[var] = True
                        activity[var] += var_inc
                        heapq.heappush(heap, (-activity[var], var))
                        if level[var] == decision_level:
                            counter += 1
                        else:
                            learnt.append(lit)
                while not seen[abs(trail[idx])]:
                    idx -= 1
                p = trail[idx]
                idx -= 1
                seen[abs(p)] = False
                counter -= 1
                if counter == 0:
                    break
                c = clauses[reason[abs(p)]]
                
            var_inc *= 1.05
            learnt_lit = -p
            bt_level = 0
            if learnt:
                bt_level = max(level[abs(lit)] for lit in learnt)
            learnt.insert(0, learnt_lit)
            
            backtrack_to(bt_level)
            
            c_idx = len(clauses)
            clauses.append(learnt)
            if len(learnt) >= 2:
                watches[lit_to_idx(learnt[0])].append(c_idx)
                watches[lit_to_idx(learnt[1])].append(c_idx)
            else:
                watches[lit_to_idx(learnt[0])].append(c_idx)
                
            assign_lit(learnt_lit, c_idx)

    # Reconstruct edge colors
    res = []
    for e in range(m):
        for c in range(3):
            if assign[var_id(e, c)] == 1:
                res.append(c + 1)
                break
        else:
            res.append(1)
            
    print("YES")
    print(*(res))

if __name__ == '__main__':
    solve()