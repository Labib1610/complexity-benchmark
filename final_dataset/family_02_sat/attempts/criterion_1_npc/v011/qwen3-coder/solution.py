from collections import defaultdict
import sys

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    clauses = []
    for _ in range(m):
        clause = list(map(int, sys.stdin.readline().split()))
        clauses.append(clause)
    return n, m, clauses

def solve_2sat(n, clauses):
    # Convert to 2-SAT format
    # Each variable x_i corresponds to lens i being in focus (1) or defocus (0)
    # We'll use indices 0 to 2*n-1 where:
    # - index 2*i represents x_i (lens i+1 in focus)
    # - index 2*i+1 represents ~x_i (lens i+1 in defocus)
    
    # For each clause with 3 literals, convert to equivalent 2-SAT clauses
    two_sat_clauses = []
    
    for clause in clauses:
        # A 3-SAT clause (a OR b OR c) is equivalent to:
        # (a OR b OR new_var) AND (~new_var OR c)
        # But we need to be more careful here
        
        # Actually, let's think differently. 
        # A clause (a OR b OR c) can be converted to 2-SAT as:
        # (a OR b) OR c => introduce a new variable z such that z <=> (a OR b)
        # Then we have (z OR c) which is 2-SAT
        # And we need to express z <=> (a OR b) in 2-SAT
        # z => (a OR b) is equivalent to (~z OR a OR b) - but this is still 3-SAT
        # (a OR b) => z is equivalent to (~a OR z) AND (~b OR z) - this is 2-SAT
        
        # Let's use a different approach:
        # For clause (a OR b OR c), it's false only when all a,b,c are false
        # So we add constraints to prevent that case
        # We can split into: (a OR b) AND (a OR c) AND (b OR c) - No, that's not equivalent
        # Actually (a OR b OR c) is equivalent to (~a => (b OR c))
        
        # Simpler approach: for each 3-literal clause, create multiple 2-literal clauses
        # that together enforce the same constraint.
        # We can do this by introducing auxiliary variables, but for implementation simplicity,
        # let's directly work with implication graph for 3-SAT
        
        # Better yet, let's reduce 3-SAT to 2-SAT by introducing new variables
        # For clause (l1 OR l2 OR l3), introduce new variable t
        # Add clauses: (l1 OR l2 OR t) AND (l3 OR ~t)
        # But (l1 OR l2 OR t) still has 3 literals...
        
        # Let's just implement a direct 3-SAT solver using SCC
        # Each clause (l1 OR l2 OR l3) means at least one literal must be true
        
        # We'll build an implication graph for the 3-SAT instance
        pass
    
    # Let's take a simpler approach and model this as a general SAT problem
    # solved via strong connected components in the implication graph
    
    # Build implication graph
    # Nodes: 0..2*n-1 where 2*i is x_i (lens i+1 in focus) and 2*i+1 is ~x_i (lens i+1 in defocus)
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    # For each 3-literal clause (a OR b OR c)
    # It's equivalent to (~a AND ~b AND ~c) => False
    # Which means at least one of a, b, c must be true
    # In other words, if ~a and ~b then c must be true
    # This gives us implications: (~a AND ~b) => c
    # Which is equivalent to (~a => c) OR (~b => c)
    # Which means (a OR c) AND (b OR c)
    
    for clause in clauses:
        # Convert 3-SAT clause to equivalent 2-SAT clauses
        # Clause is (l1 OR l2 OR l3)
        # This is equivalent to (l1 OR l2) AND (l1 OR l3) AND (l2 OR l3) ? No!
        # That would be too restrictive.
        
        # Correct reduction:
        # (l1 OR l2 OR l3) is equivalent to:
        # Introduce new variable y
        # Add clauses: (l1 OR l2 OR y) AND (l3 OR ~y)
        # But we still have 3-literal clauses...
        
        # Let's handle 3-SAT directly with SCC
        # For clause (l1 OR l2 OR l3) to be satisfied, 
        # if l1 is false and l2 is false, then l3 must be true
        # This gives (~l1 AND ~l2) => l3
        # Which is equivalent to (l1 OR l3) AND (l2 OR l3)
        
        l1, l2, l3 = clause
        
        # Convert literals to variable indices
        def lit_to_idx(lit):
            var = abs(lit) - 1  # 0-indexed
            if lit > 0:
                return 2 * var      # x_var
            else:
                return 2 * var + 1  # ~x_var
                
        def not_lit_to_idx(lit):
            var = abs(lit) - 1  # 0-indexed
            if lit > 0:
                return 2 * var + 1  # ~x_var
            else:
                return 2 * var      # x_var
        
        idx1 = lit_to_idx(l1)
        idx2 = lit_to_idx(l2)
        idx3 = lit_to_idx(l3)
        not_idx1 = not_lit_to_idx(l1)
        not_idx2 = not_lit_to_idx(l2)
        not_idx3 = not_lit_to_idx(l3)
        
        # From (l1 OR l2 OR l3), we derive:
        # (~l1 AND ~l2) => l3  which gives (~l1 => l3) AND (~l2 => l3)
        # (~l1 AND ~l3) => l2  which gives (~l1 => l2) AND (~l3 => l2)
        # (~l2 AND ~l3) => l1  which gives (~l2 => l1) AND (~l3 => l1)
        
        # But we should be more precise. The clause (l1 OR l2 OR l3) is false only when
        # all literals are false. To prevent this, we add implications:
        adj[not_idx1].append(idx2)
        adj[not_idx2].append(idx1)
        adj[not_idx1].append(idx3)
        adj[not_idx3].append(idx1)
        adj[not_idx2].append(idx3)
        adj[not_idx3].append(idx2)
        
        rev_adj[idx2].append(not_idx1)
        rev_adj[idx1].append(not_idx2)
        rev_adj[idx3].append(not_idx1)
        rev_adj[idx1].append(not_idx3)
        rev_adj[idx3].append(not_idx2)
        rev_adj[idx2].append(not_idx3)
    
    # Kosaraju's algorithm for finding SCCs
    visited = [False] * (2 * n)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)
    
    # Second DFS on transpose graph
    visited = [False] * (2 * n)
    scc_id = [-1] * (2 * n)
    scc_count = 0
    
    def dfs2(u):
        visited[u] = True
        scc_id[u] = scc_count
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v)
    
    while order:
        u = order.pop()
        if not visited[u]:
            dfs2(u)
            scc_count += 1
    
    # Check if satisfiable
    for i in range(n):
        if scc_id[2*i] == scc_id[2*i + 1]:
            return None  # Contradiction
    
    # Assign values
    assignment = [0] * n
    # Process SCCs in reverse topological order
    scc_order = list(range(scc_count))
    # For simplicity, we can assign values based on SCC ids
    for i in range(n):
        # If SCC of x_i is processed after SCC of ~x_i, then x_i = True
        if scc_id[2*i] > scc_id[2*i + 1]:
            assignment[i] = 1
        else:
            assignment[i] = 0
            
    return assignment

def main():
    n, m, clauses = read_input()
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    result = solve_2sat(n, clauses)
    
    if result is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()