import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # Each rule: (v1, v2, v3) where v in 1..2n
    # For each rule, we add clauses: (¬a ∨ ¬b) for each pair in the rule
    # This encodes "at most one of a, b, c is true"
    # Combined with (a ∨ b ∨ c) for each rule, we get "exactly one true"
    
    clauses = []
    rule_vars = []
    
    for _ in range(m):
        conditions = []
        for _ in range(3):
            x = int(next(it))
            # Map: positive x -> var x, negative x -> var x+n (negated form)
            if x > 0:
                conditions.append(x)
            else:
                conditions.append(-x + n)
        rule_vars.append(conditions)
        
        # Add "at most one" constraints: at most one of the three is true
        a, b, c = conditions
        # ¬a ∨ ¬b
        clauses.append((a + n, b + n))
        # ¬b ∨ ¬c
        clauses.append((b + n, c + n))
        # ¬a ∨ ¬c
        clauses.append((a + n, c + n))
    
    num_vars = 2 * n
    adj = [[] for _ in range(2 * num_vars + 1)]
    adj_rev = [[] for _ in range(2 * num_vars + 1)]
    
    def get_neg(v):
        if v > n:
            return v - n
        else:
            return v + n
    
    for a, b in clauses:
        # Implication: a -> ¬b (if a is true, b must be false)
        adj[a].append(get_neg(b))
        adj_rev[get_neg(b)].append(a)
        # Implication: b -> ¬a
        adj[b].append(get_neg(a))
        adj_rev[get_neg(a)].append(b)
    
    # Kosaraju's algorithm
    visited = [False] * (2 * num_vars + 1)
    order = []
    
    def dfs1(v):
        visited[v] = True
        for u in adj[v]:
            if not visited[u]:
                dfs1(u)
        order.append(v)
    
    for v in range(1, 2 * num_vars + 1):
        if not visited[v]:
            dfs1(v)
    
    visited = [False] * (2 * num_vars + 1)
    comp = [0] * (2 * num_vars + 1)
    comp_id = 0
    
    def dfs2(v):
        visited[v] = True
        comp[v] = comp_id
        for u in adj_rev[v]:
            if not visited[u]:
                dfs2(u)
    
    for v in reversed(order):
        if not visited[v]:
            comp_id += 1
            dfs2(v)
    
    # Check satisfiability for each i: comp[i] != comp[i+n]
    assignment = [0] * (n + 1)
    for i in range(1, n + 1):
        if comp[i] == comp[i + n]:
            print("NO")
            return
        assignment[i] = 1 if comp[i] > comp[i + n] else 0
    
    # Verify all rules
    for conditions in rule_vars:
        count = 0
        for v in conditions:
            if v <= n:
                if assignment[v] == 1:
                    count += 1
            else:
                if assignment[v - n] == 0:
                    count += 1
        if count != 1:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, assignment[1:])))

solve()