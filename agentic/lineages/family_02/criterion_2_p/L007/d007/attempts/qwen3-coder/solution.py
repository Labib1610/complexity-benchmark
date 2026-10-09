import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    constraints = []
    idx = 2
    for _ in range(m):
        l1 = int(data[idx])
        l2 = int(data[idx+1])
        idx += 2
        constraints.append((l1, l2))
    
    # For each constraint: E > C
    # E = l1*(2*s_|l1| - 1) + l2*(2*s_|l2| - 1)
    # C = -(|l1| + |l2|)
    # So: l1*(2*s_|l1| - 1) + l2*(2*s_|l2| - 1) > -(|l1| + |l2|)
    # Rearranging:
    # 2*l1*s_|l1| - l1 + 2*l2*s_|l2| - l2 > -|l1| - |l2|
    # 2*l1*s_|l1| + 2*l2*s_|l2| > l1 + l2 - |l1| - |l2|
    # Let a = |l1|, b = |l2|
    # If l1 > 0: s_a term is 2*l1*s_a
    # If l1 < 0: s_a term is 2*l1*(s_a - 1) = 2*l1*s_a - 2*|l1|
    # Similarly for l2
    
    # So total coefficient of s_a is:
    # if l1 > 0: 2*l1
    # if l1 < 0: 2*l1 = -2*|l1|
    # Constant shift from s terms: 
    # if l1 > 0: -l1 = -|l1|
    # if l1 < 0: -l1 - 2*|l1| = |l1| - 2*|l1| = -|l1|
    # Wait, let's recompute carefully.
    
    # E = l1*(2*s_a - 1) + l2*(2*s_b - 1) > -(|l1| + |l2|)
    # 2*l1*s_a - l1 + 2*l2*s_b - l2 > -|l1| - |l2|
    # 2*l1*s_a + 2*l2*s_b > l1 + l2 - |l1| - |l2|
    
    # Let's define: for each variable s_i, we'll track its coefficients.
    # But perhaps it's easier to convert to a graph 2-SAT problem.
    
    # Each s_i is a boolean variable.
    # Each constraint defines a linear inequality in two variables.
    # We can rewrite each constraint as:
    # l1*(2*s_a - 1) + l2*(2*s_b - 1) > -(|l1| + |l2|)
    # Which simplifies to:
    # 2*l1*s_a + 2*l2*s_b > l1 + l2 - |l1| - |l2|
    
    # Let's denote a=|l1|, b=|l2|.
    # Then:
    # if l1>0: coeff of s_a is 2*l1
    # if l1<0: s_a term is 2*l1*(s_a - 1) = 2*l1*s_a - 2*|l1|
    # So total s_a coefficient is always 2*l1
    # Similarly for s_b: coefficient is 2*l2
    # Constant terms from -l1 - l2
    # So we have:
    # 2*l1*s_a + 2*l2*s_b - l1 - l2 > -|l1| - |l2|
    # 2*l1*s_a + 2*l2*s_b > l1 + l2 - |l1| - |l2|
    
    # Let's compute RHS:
    # rhs = l1 + l2 - |l1| - |l2|
    # if l1>0: |l1|=l1, so l1 - |l1| = 0
    # if l1<0: |l1|=-l1, so l1 - |l1| = l1 - (-l1) = 2*l1
    # So l1 - |l1| = 0  if l1>0
    #              2*l1 if l1<0
    # Similarly l2 - |l2| = 0  if l2>0
    #                    2*l2 if l2<0
    # Therefore:
    # rhs = (l1 - |l1|) + (l2 - |l2|) = max(0, 2*l1) + max(0, 2*l2)
    # No, that's not right either.
    # l1 - |l1| = 0 if l1 >= 0
    #            2*l1 if l1 < 0
    # So rhs = (l1 - |l1|) + (l2 - |l2|)
    # This equals 0 + 0 = 0 if both l1,l2 >=0
    #                2*l1 + 0 if l1<0, l2>=0
    #                0 + 2*l2 if l1>=0, l2<0
    #                2*l1 + 2*l2 if l1,l2 < 0
    
    # So our constraint is:
    # 2*l1*s_a + 2*l2*s_b > (l1 - |l1|) + (l2 - |l2|)
    
    # This is getting complex. Let's think differently.
    # Let's just implement a brute-force approach for small cases,
    # but since n can be up to 1e5, we need something better.
    
    # Actually, this is a classic 2-SAT problem.
    # Each constraint gives us a relation between two boolean variables.
    # We can convert the linear inequality into logical implications.
    
    # Let's try to model it properly.
    # Given: l1*(2*s_a - 1) + l2*(2*s_b - 1) > -(|l1| + |l2|)
    # Where a = |l1|, b = |l2|
    # Let's enumerate all 4 possibilities for (s_a, s_b) and see which ones satisfy the constraint.
    # s_a in {0,1}, s_b in {0,1}
    
    # For each constraint (l1, l2):
    # Compute E for all (s_a, s_b) pairs and check E > C
    
    # This suggests building an implication graph for 2-SAT.
    # But let's just check if any constraint is unsatisfiable by trying all 4 combinations.
    
    # However, with m up to 2e5, we can't do that per constraint.
    # Instead, let's build the 2-SAT instance correctly.
    
    # For each constraint:
    # l1*(2*s_a - 1) + l2*(2*s_b - 1) > -(|l1| + |l2|)
    # Let's call a = |l1|, b = |l2|
    # We want: 2*l1*s_a - l1 + 2*l2*s_b - l2 > -a - b
    #          2*l1*s_a + 2*l2*s_b > l1 + l2 - a - b
    # Let c = l1 + l2 - a - b
    # So: 2*l1*s_a + 2*l2*s_b > c
    
    # Now, for each of the four (s_a, s_b) in {0,1}x{0,1}, we can evaluate LHS and compare with c.
    # At least one should satisfy the constraint, otherwise it's impossible.
    
    # But we also need global consistency across all constraints.
    # This is exactly what 2-SAT solves.
    
    # Let's build the implication graph.
    # For each constraint, determine which assignments (s_a, s_b) satisfy it.
    # For those that don't, add "forbidden" edges to the implication graph.
    
    # Actually, simpler approach:
    # For each constraint, find which of the 4 value combinations are forbidden.
    # Then use union-find or 2-SAT solver.
    
    # Let's enumerate forbidden pairs and use Union-Find with negation.
    
    # But given time limits, let's just check if any single constraint forbids all 4 combinations.
    # That would make it immediately unsatisfiable.
    
    # Check for local unsatisfiability first:
    for l1, l2 in constraints:
        a = abs(l1)
        b = abs(l2)
        c = l1 + l2 - a - b  # This is l1 - |l1| + l2 - |l2|
        
        ok = False
        for sa in [0, 1]:
            for sb in [0, 1]:
                lhs = 2 * l1 * sa + 2 * l2 * sb
                if lhs > c:
                    ok = True
                    break
            if ok:
                break
        
        if not ok:
            print("NO")
            return
    
    # All constraints are locally satisfiable. Now check global satisfiability using 2-SAT.
    
    # Build implication graph for 2-SAT
    # Variables: x1, ..., xn where xi = si
    # For each constraint, figure out forbidden (sa, sb) pairs
    # For each forbidden pair, add clauses to enforce that at least one is false in its context
    
    # It's easier to use the standard reduction:
    # For each constraint, determine which (sa,sb) assignments violate it
    # For each violating assignment, we must have NOT(sa==va AND sb==vb)
    # Which is equivalent to (NOT sa==va) OR (NOT sb==vb)
    # Which translates to (sa != va) OR (sb != vb)
    
    # In terms of implications:
    # If sa == va AND sb == vb leads to contradiction,
    # then we must have sa != va OR sb != vb
    # This means: if sa == va => sb != vb
    #             if sb == vb => sa != va
    
    # Let's represent variables as 2*i (for s_i = 0) and 2*i+1 (for s_i = 1)
    # But for implication graph, it's easier to use x_i and NOT x_i
    
    # Let's use a proper 2-SAT implementation.
    
    # Number of variables
    num_vars = n
    # We'll map variable i (1-based) and values 0/1 to nodes
    # Node 2*i represents s_i = False (0)
    # Node 2*i+1 represents s_i = True (1)
    # But in 2-SAT literature, often it's 2*i-2 and 2*i-1 for 1-based vars
    
    adj = [[] for _ in range(2 * n)]
    adj_inv = [[] for _ in range(2 * n)]
    
    def add_clause(a_var, a_sign, b_var, b_sign):
        # a_sign = True means a_var should be True, False means it should be False
        # Same for b_sign
        # Add clause (a_sign ? a_var : NOT a_var) OR (b_sign ? b_var : NOT b_var)
        # Which is equivalent to:
        # If NOT (a_sign ? a_var) then (b_sign ? b_var)
        # If NOT (b_sign ? b_var) then (a_sign ? a_var)
        u = 2 * (a_var - 1) + (0 if a_sign else 1)
        v = 2 * (b_var - 1) + (0 if b_sign else 1)
        adj[u ^ 1].append(v)
        adj[v ^ 1].append(u)
        adj_inv[v].append(u ^ 1)
        adj_inv[u].append(v ^ 1)
    
    # Process constraints
    for l1, l2 in constraints:
        a = abs(l1)
        b = abs(l2)
        c = l1 + l2 - abs(l1) - abs(l2)
        
        forbidden = []
        for sa in [0, 1]:
            for sb in [0, 1]:
                lhs = 2 * l1 * sa + 2 * l2 * sb
                if not (lhs > c):
                    forbidden.append((sa, sb))
        
        # For each forbidden pair, add clause that prevents it
        for sa, sb in forbidden:
            # We cannot have s_a = sa AND s_b = sb
            # So we add clause: (s_a != sa) OR (s_b != sb)
            # Which means: (s_a = 1-sa) OR (s_b = 1-sb)
            add_clause(a, sa == 0, b, sb == 0)
    
    # Now solve 2-SAT using Kosaraju's algorithm
    # Find strongly connected components
    order = []
    visited = [False] * (2 * n)
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)
    
    # Transpose graph already built as adj_inv
    visited = [False] * (2 * n)
    components = [-1] * (2 * n)
    comp_cnt = 0
    
    def dfs2(u, comp_num):
        components[u] = comp_num
        for v in adj_inv[u]:
            if components[v] == -1:
                dfs2(v, comp_num)
    
    for u in reversed(order):
        if components[u] == -1:
            dfs2(u, comp_cnt)
            comp_cnt += 1
    
    # Check if any variable and its negation are in the same component
    for i in range(n):
        node_false = 2 * i       # s_{i+1} = 0
        node_true = 2 * i + 1     # s_{i+1} = 1
        if components[node_false] == components[node_true]:
            print("NO")
            return
    
    # Otherwise, construct a solution
    print("YES")
    result = [0] * n
    comp_order = sorted(range(2 * n), key=lambda x: components[x])
    assignment = [-1] * (2 * n)
    
    for u in comp_order:
        if assignment[u] == -1:
            assignment[u] = 0  # False
            assignment[u ^ 1] = 1  # True
    
    for i in range(n):
        # If s_i = 1 (node 2*i+1) is in a later component than s_i = 0 (node 2*i),
        # then setting s_i = 1 is safe.
        # Actually, in standard 2-SAT resolution, if component of x is > component of NOT x,
        # then x should be TRUE.
        node_false = 2 * i
        node_true = 2 * i + 1
        if components[node_true] > components[node_false]:
            result[i] = 1
        else:
            result[i] = 0
    
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()