import sys
from collections import defaultdict, deque

def f1(x):
    return (2 * x + 1) % 5

def f2(x):
    return (3 * x + 2) % 5

# Composition functions
def compose(f, g):
    # Returns function h such that h(x) = g(f(x))
    return lambda x: g(f(x))

def check_composition_identity(f, g):
    # Check if g(f(x)) = x for all x in {0,1,2,3,4}
    for x in range(5):
        if g(f(x)) != x:
            return False
    return True

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    graph = [[] for _ in range(n+1)]
    edge_indices = dict()
    
    idx = 2
    for i in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
        edge_indices[(u,v)] = i
        edge_indices[(v,u)] = i
        
    # For each edge, determine which basis pairs are allowed
    # Basis 1: f1(x) = (2x+1)%5
    # Basis 2: f2(x) = (3x+2)%5
    
    # Precompute compositions
    funcs = [None, f1, f2]
    
    allowed = {}
    for b_u in [1, 2]:
        for b_v in [1, 2]:
            f_uv = lambda x, bu=b_u, bv=b_v: funcs[bv](funcs[bu](x))
            if check_composition_identity(funcs[b_u], funcs[b_v]):
                allowed[(b_u, b_v)] = True
            else:
                allowed[(b_u, b_v)] = False
                
    # Build constraint graph for 2-SAT
    # Variables: for each node i, we have variable i (basis 1) and ~i (basis 2)
    # But since we're dealing with basis in {1,2}, let's map:
    # var[i][1] means sensor i uses basis 1
    # var[i][2] means sensor i uses basis 2
    
    # For each edge (u,v), if allowed[(b_u,b_v)] is False, then we cannot have both
    # So we add clauses: NOT(var[u][b_u]) OR NOT(var[v][b_v]) for forbidden pairs
    
    # Actually, let's think differently. We want g_v(g_u(x)) = x for all x.
    # This means g_v is the inverse of g_u.
    # Let's find which pairs satisfy this.
    
    # Check which combinations satisfy the identity:
    valid_pairs = []
    for b_u in [1, 2]:
        for b_v in [1, 2]:
            # Check if funcs[b_v](funcs[b_u](x)) == x for all x
            ok = True
            for x in range(5):
                if funcs[b_v](funcs[b_u](x)) != x:
                    ok = False
                    break
            if ok:
                valid_pairs.append((b_u, b_v))
                
    # Build implication graph for 2-SAT
    # Variables: for sensor i and basis b, we have variable 2*i + b
    # But to simplify, let's use: for sensor i, var i_1 and i_2
    # Let's encode variables as: for sensor i and basis b (1 or 2)
    # var[i][b] = 2*i + b
    # But since i starts at 1, let's do: (i,b) -> 2*i + b - 2 
    
    # Simpler approach: for each edge, only certain basis pairs are allowed
    # This is a constraint satisfaction problem. 
    # For each edge, at least one of the valid basis pairs must be chosen.
    
    # This can be modeled as a 2-SAT problem:
    # For each sensor i, we have two variables: x_i1 (uses basis 1) and x_i2 (uses basis 2)
    # For each edge (u,v), we need to ensure that the combination (b_u, b_v) is valid.
    # Valid pairs are those where composition is identity.
    
    # Let's recompute valid pairs correctly:
    valid_edge_assignments = set()
    for b_u in [1, 2]:
        for b_v in [1, 2]:
            composed = [funcs[b_v](funcs[b_u](x)) for x in range(5)]
            identity = list(range(5))
            if composed == identity:
                valid_edge_assignments.add((b_u, b_v))
                
    # Now we model a 2-SAT problem:
    # Variables: for each sensor i and basis b, we have a boolean variable x[i,b]
    # For each edge (u,v), we need (x[u,1] AND x[v,?]) OR (x[u,2] AND x[v,?]) ...
    # Specifically, for each edge, only certain pairs of (b_u, b_v) are allowed.
    
    # The constraint for edge (u,v) is:
    # OR over all valid (b_u,b_v): (x[u,b_u] AND x[v,b_v])
    # This is equivalent to: for each invalid (b_u,b_v), add clause NOT x[u,b_u] OR NOT x[v,b_v]
    
    # But actually, it's simpler to think in terms of implications:
    # If u takes basis b_u and (b_u, b_v) is not valid, then v cannot take b_v.
    # So: x[u,b_u] => NOT x[v,b_v] if (b_u, b_v) is invalid.
    # Which is equivalent to: NOT x[u,b_u] OR NOT x[v,b_v]
    
    # Let's number variables: for sensor i (1-based) and basis b, variable is 2*(i-1) + b
    # So var[i][b] = 2*(i-1) + b, where i=1..n, b=1,2
    
    def var(i, b):
        return 2 * (i - 1) + b  # 1,2,3,4,...

    def not_var(i, b):
        return -(2 * (i - 1) + b)

    # Initialize 2-SAT instance
    num_vars = 2 * n
    clauses = []
    
    # For each edge, add constraints for invalid basis pairs
    for u, v in edges:
        for b_u in [1, 2]:
            for b_v in [1, 2]:
                if (b_u, b_v) not in valid_edge_assignments:
                    # Add clause: NOT x[u,b_u] OR NOT x[v,b_v]
                    clauses.append([not_var(u, b_u), not_var(v, b_v)])
                    
    # Additionally, each sensor must choose exactly one basis:
    # x[u,1] OR x[u,2] 
    # NOT x[u,1] OR NOT x[u,2]
    for u in range(1, n+1):
        clauses.append([var(u, 1), var(u, 2)])      # At least one
        clauses.append([not_var(u, 1), not_var(u, 2)])  # At most one
        
    # Solve 2-SAT using Kosaraju's algorithm for SCC
    # Build implication graph
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    for clause in clauses:
        # clause is [a, b] meaning a OR b
        # This translates to NOT a => b and NOT b => a
        if len(clause) == 1:
            lit = clause[0]
            adj[-lit].append(lit)
            rev_adj[lit].append(-lit)
        else:
            a, b = clause
            adj[-a].append(b)
            adj[-b].append(a)
            rev_adj[b].append(-a)
            rev_adj[a].append(-b)
            
    # Kosaraju's algorithm
    order = []
    visited = set()
    
    def dfs1(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in adj[node]:
            dfs1(neighbor)
        order.append(node)
        
    all_nodes = set()
    for clause in clauses:
        for lit in clause:
            all_nodes.add(lit)
            all_nodes.add(-lit)
            
    for node in all_nodes:
        dfs1(node)
        
    visited = set()
    scc_id = {}
    cnt = 0
    
    def dfs2(node, cid):
        if node in visited:
            return
        visited.add(node)
        scc_id[node] = cid
        for neighbor in rev_adj[node]:
            dfs2(neighbor, cid)
            
    order.reverse()
    for node in order:
        if node not in visited:
            dfs2(node, cnt)
            cnt += 1
            
    # Check if satisfiable
    for i in range(1, n+1):
        for b in [1, 2]:
            v = var(i, b)
            if scc_id[v] == scc_id[-v]:
                print("NO")
                return
                
    # Extract solution: for each variable, if scc_id[var] > scc_id[not var], set to True
    result = [0] * (n+1)
    for i in range(1, n+1):
        if scc_id[var(i, 1)] > scc_id[not_var(i, 1)]:
            result[i] = 1
        elif scc_id[var(i, 2)] > scc_id[not_var(i, 2)]:
            result[i] = 2
        else:
            # This should not happen if satisfiable
            result[i] = 1  # default
            
    # Verify that every sensor got assigned a basis
    for i in range(1, n+1):
        if result[i] == 0:
            result[i] = 1  # fallback
            
    print("YES")
    print(" ".join(map(str, result[1:])))
    
if __name__ == "__main__":
    main()