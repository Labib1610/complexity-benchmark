import sys
from collections import defaultdict

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # For each constraint (a b), it means:
    # NOT ( (x[|a|] != sign(a)) AND (x[|b|] != sign(b)) )
    # Which is equivalent to:
    # (x[|a|] == sign(a)) OR (x[|b|] == sign(b))
    # This is a 2-SAT clause: (a OR b)
    
    # We'll build a 2-SAT graph
    # Variables: for each relay i, we have two nodes: i*2 (for 0) and i*2+1 (for 1)
    # But it's easier to think in terms of literals
    # Literal: +i means relay i is 1, -i means relay i is 0
    
    # For constraint (a b), we add edges:
    # NOT a -> b
    # NOT b -> a
    
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        # Constraint: (x[|a|] == sign(a)) OR (x[|b|] == sign(b))
        # Which means if x[|a|] != sign(a) then x[|b|] must == sign(b)
        # and if x[|b|] != sign(b) then x[|a|] must == sign(a)
        
        # NOT (x[|a|] == sign(a)) -> (x[|b|] == sign(b))
        # NOT (x[|b|] == sign(b)) -> (x[|a|] == sign(a))
        
        # Let's define:
        # not_a = literal meaning x[|a|] != sign(a)
        # a_true = literal meaning x[|a|] == sign(a)
        # same for b
        
        # We need to convert to implications:
        # not_a -> b_true
        # not_b -> a_true
        
        # Literal representation:
        # positive literal i means x[i] = 1
        # negative literal -i means x[i] = 0
        
        # For a:
        # if a > 0: a_true is +a, not_a is -a
        # if a < 0: a_true is -(-a) = +a, not_a is -a
        
        # So a_true = +abs(a) if we want x[abs(a)] = 1, which happens when sign(a) = 1
        #            = -abs(a) if we want x[abs(a)] = 0, which happens when sign(a) = -1
        # So a_true = a
        # and not_a = -a
        
        # The constraint is: (a_true) OR (b_true)
        # Which is equivalent to: (NOT not_a) OR (b_true) = not_a -> b_true
        # and: (NOT not_b) OR (a_true) = not_b -> a_true
        
        not_a = -a
        a_true = a
        not_b = -b
        b_true = b
        
        adj[not_a].append(b_true)
        adj[not_b].append(a_true)
        rev_adj[b_true].append(not_a)
        rev_adj[a_true].append(not_b)
    
    # Now we have a 2-SAT problem. We need to check if there's a valid assignment.
    # We'll use Kosaraju's algorithm to find strongly connected components.
    
    # Node IDs: for relay i (1-based), +i and -i are the literals
    # We need to collect all nodes
    nodes = set()
    for u in adj:
        nodes.add(u)
        for v in adj[u]:
            nodes.add(v)
    
    # Also add nodes that might not appear in constraints but are variables
    for i in range(1, n+1):
        nodes.add(i)
        nodes.add(-i)
    
    # Kosaraju's first DFS to get finishing times
    visited = set()
    finish_stack = []
    
    def dfs1(u):
        visited.add(u)
        for v in adj[u]:
            if v not in visited:
                dfs1(v)
        finish_stack.append(u)
    
    for node in nodes:
        if node not in visited:
            dfs1(node)
    
    # Second DFS on transpose graph in reverse finish order
    visited.clear()
    sccs = []
    scc_id = {}
    
    def dfs2(u, current_scc):
        visited.add(u)
        current_scc.append(u)
        scc_id[u] = len(sccs)
        for v in rev_adj[u]:
            if v not in visited:
                dfs2(v, current_scc)
    
    while finish_stack:
        node = finish_stack.pop()
        if node not in visited:
            current_scc = []
            dfs2(node, current_scc)
            sccs.append(current_scc)
    
    # Check if for any variable i, both +i and -i are in the same SCC
    for i in range(1, n+1):
        if scc_id[i] == scc_id[-i]:
            print("NO")
            return
    
    # Otherwise, there exists a solution
    # Assign values based on topological order of SCCs
    # Variables in later finishing SCCs in the first DFS are assigned True
    
    # Actually, in the 2-SAT setup, if scc_id[u] > scc_id[not_u], then u is true
    assignment = [0] * (n + 1)  # 1-indexed
    
    for i in range(1, n+1):
        if scc_id[i] > scc_id[-i]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    print("YES")
    print(' '.join(map(str, assignment[1:])))

if __name__ == "__main__":
    main()