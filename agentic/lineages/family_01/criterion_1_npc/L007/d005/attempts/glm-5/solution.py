import sys
sys.setrecursionlimit(10000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # We need to find assignment c in {1,2,3}^n such that for all edges (u,v):
    # (c_u - c_v)^4 - 5(c_u - c_v)^2 + 4 = 0
    # This holds iff |c_u - c_v| in {1, 2}.
    # |c_u - c_v| = 0 is forbidden (same color).
    # |c_u - c_v| = 3 is forbidden (colors 1 and 3).
    # So adjacent nodes must have different colors, and cannot be (1,3) or (3,1).
    # Valid adjacent pairs: (1,2), (2,1), (2,3), (3,2).
    # This means color 2 is compatible with 1 and 3, but 1 and 3 are not compatible.
    # Graph structure: nodes with color 1 or 3 form independent sets, and no edge connects 1 to 3.
    # Nodes with color 2 can connect to 1 or 3.
    
    # We use backtracking with constraint propagation.
    # Domains: 0 -> {1}, 1 -> {2}, 2 -> {3}, 3 -> {1,3}, 4 -> {1,2}, 5 -> {2,3}, 6 -> {1,2,3}
    # We want lexicographically smallest assignment.
    
    # Compatibility table: comp[d][c] = new domain after assigning color c
    # comp[d][c] = -1 if invalid, else new domain (possibly singleton)
    # d in 0..6, c in 1..3
    comp = [[-1]*4 for _ in range(7)]
    for d in range(7):
        for c in range(1, 4):
            if d == 0:
                comp[d][c] = 0 if c == 1 else -1
            elif d == 1:
                comp[d][c] = 1 if c == 2 else -1
            elif d == 2:
                comp[d][c] = 2 if c == 3 else -1
            elif d == 3:
                if c == 1: comp[d][c] = 0
                elif c == 3: comp[d][c] = 2
                else: comp[d][c] = -1
            elif d == 4:
                if c == 1: comp[d][c] = 0
                elif c == 2: comp[d][c] = 1
                else: comp[d][c] = -1
            elif d == 5:
                if c == 2: comp[d][c] = 1
                elif c == 3: comp[d][c] = 2
                else: comp[d][c] = -1
            else: # d == 6
                if c == 1: comp[d][c] = 0
                elif c == 2: comp[d][c] = 1
                else: comp[d][c] = 2
    
    # Reduction rules based on edge constraints
    # If u has color c_u, then v must have color c_v such that |c_u - c_v| in {1, 2}
    # c_u=1: c_v in {2}
    # c_u=2: c_v in {1, 3}
    # c_u=3: c_v in {2}
    
    # reduce[d_u][c_u] = new domain for v
    reduce_rule = [[-1]*4 for _ in range(7)]
    for d_u in range(7):
        for c_u in range(1, 4):
            if comp[d_u][c_u] == -1:
                continue
            if c_u == 1:
                target = 1 # v must be 2
            elif c_u == 3:
                target = 1 # v must be 2
            else: # c_u == 2
                target = 3 # v in {1, 3}
            reduce_rule[d_u][c_u] = target
    
    # Initial domains
    domains = [6] * n
    
    assignment = [0] * n
    found = False
    
    # AC-3 style propagation
    def propagate(queue):
        while queue:
            u = queue.pop()
            du = domains[u]
            # Determine possible colors of u
            if du == 0: colors_u = [1]
            elif du == 1: colors_u = [2]
            elif du == 2: colors_u = [3]
            elif du == 3: colors_u = [1, 3]
            elif du == 4: colors_u = [1, 2]
            elif du == 5: colors_u = [2, 3]
            else: colors_u = [1, 2, 3]
            
            for v in adj[u]:
                dv = domains[v]
                # Find intersection of allowed colors for v
                # allowed_v = intersection over c_u in colors_u of reduce_rule[du][c_u]
                # But reduce_rule gives domain index, we need to intersect them
                # Actually, for each c_u, v must be in reduce_rule[du][c_u]
                # So v's domain must be subset of union of these? No.
                # Constraint: exists c_u in colors_u s.t. c_v is compatible.
                # Compatible means |c_u - c_v| in {1,2}.
                # Let's compute allowed colors for v directly.
                allowed_v = set()
                for c_u in colors_u:
                    if c_u == 1: allowed_v.add(2)
                    elif c_u == 2: allowed_v.update([1, 3])
                    else: allowed_v.add(2)
                
                # Intersect with current domain
                new_dv = -1
                if dv == 0: set_v = {1}
                elif dv == 1: set_v = {2}
                elif dv == 2: set_v = {3}
                elif dv == 3: set_v = {1, 3}
                elif dv == 4: set_v = {1, 2}
                elif dv == 5: set_v = {2, 3}
                else: set_v = {1, 2, 3}
                
                inter = set_v & allowed_v
                if not inter:
                    return False
                if len(inter) == 1:
                    val = inter.pop()
                    if val == 1: new_dv = 0
                    elif val == 2: new_dv = 1
                    else: new_dv = 2
                elif inter == {1, 2}: new_dv = 4
                elif inter == {2, 3}: new_dv = 5
                elif inter == {1, 3}: new_dv = 3
                else: new_dv = 6
                
                if new_dv != dv:
                    domains[v] = new_dv
                    if v not in queue:
                        queue.append(v)
        return True
    
    # Initial propagation
    queue = list(range(n))
    if not propagate(queue):
        print("NO")
        return
    
    # Check if any domain is empty
    for d in domains:
        if d == -1:
            print("NO")
            return
    
    def backtrack(idx):
        nonlocal found
        if found:
            return
        if idx == n:
            found = True
            return
        
        # Find unassigned variable with smallest domain (MRV)
        # Actually, we assign in order 0..n-1 for lexicographical order
        # But we can use MRV for efficiency, then sort back? No, lex order is important.
        # We assign in order 0..n-1.
        
        # If already assigned (domain is singleton), skip
        d = domains[idx]
        if d < 3:
            c = d + 1
            assignment[idx] = c
            backtrack(idx + 1)
            if found: return
            assignment[idx] = 0
            return
        
        # Try colors in order 1, 2, 3
        colors_to_try = []
        if d == 3: colors_to_try = [1, 3]
        elif d == 4: colors_to_try = [1, 2]
        elif d == 5: colors_to_try = [2, 3]
        else: colors_to_try = [1, 2, 3]
        
        for c in colors_to_try:
            # Save state
            saved_domains = domains[:]
            
            assignment[idx] = c
            # Propagate assignment
            domains[idx] = c - 1  # singleton domain
            
            queue = [idx]
            if propagate(queue):
                # Check consistency
                consistent = True
                for i in range(n):
                    if domains[i] == -1:
                        consistent = False
                        break
                if consistent:
                    backtrack(idx + 1)
                    if found:
                        return
            
            # Restore state
            for i in range(n):
                domains[i] = saved_domains[i]
            assignment[idx] = 0
        
    backtrack(0)
    
    if found:
        print("YES")
        print(' '.join(map(str, assignment)))
    else:
        print("NO")

solve()