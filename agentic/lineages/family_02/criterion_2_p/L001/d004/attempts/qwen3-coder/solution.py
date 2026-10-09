import sys
import threading

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each constraint (l1, l2):
    # An assessment is exposed if P(|l1|) != R(l1) AND P(|l2|) != R(l2)
    # We want NO exposed assessments => for each constraint, 
    # it's OK if P(|l1|) == R(l1) OR P(|l2|) == R(l2) (or both)
    # So for each constraint, we have a clause: (P(|l1|) == R(l1)) OR (P(|l2|) == R(l2))
    # This is a 2-SAT problem.
    
    # Variables: x_i represents P(i) (i from 1 to n)
    # For each clause (x_a == val_a) OR (x_b == val_b), we convert to implication graph:
    # NOT(x_a == val_a) -> (x_b == val_b)
    # NOT(x_b == val_b) -> (x_a == val_a)
    
    # Literal representation:
    # For variable i (1-based), 
    # literal i represents x_i = 1
    # literal -i represents x_i = 0
    # So x_i == val is represented by literal (val == 1) ? i : (-i)
    
    # For constraint (x_a == val_a) OR (x_b == val_b)
    # Equivalent to:
    # (NOT(x_a == val_a)) -> (x_b == val_b)
    # (NOT(x_b == val_b)) -> (x_a == val_a)
    
    # NOT(x_a == val_a) is represented as:
    # if val_a == 1, then NOT(x_a == 1) means x_a == 0, so literal -a
    # if val_a == 0, then NOT(x_a == 0) means x_a == 1, so literal a
    # Similarly for b
    
    clauses = []
    index = 2
    for i in range(m):
        l1 = int(data[index])
        l2 = int(data[index+1])
        index += 2
        clauses.append((l1, l2))
    
    # Build implication graph for 2-SAT
    # Nodes: 1 to n represent x_i = 1
    # Nodes: -(1) to -n represent x_i = 0
    # Total nodes: 2*n (we'll map negative literals properly)
    
    # Adjacency list for graph and reverse graph
    adj = [[] for _ in range(2 * n + 1)]
    adj_rev = [[] for _ in range(2 * n + 1)]
    
    def lit_to_node(lit):
        # Converts literal to node index (1-based)
        # Positive literal i -> node i
        # Negative literal -i -> node n + i
        if lit > 0:
            return lit
        else:
            return n + (-lit)
    
    def node_to_lit(node):
        # Converts node back to literal
        if node <= n:
            return node
        else:
            return -(node - n)
    
    # For each clause (l1, l2), meaning (P(|l1|) == R(l1)) OR (P(|l2|) == R(l2))
    # Let a = |l1|, va = R(l1)
    # Let b = |l2|, vb = R(l2)
    # Clause: (x_a == va) OR (x_b == vb)
    # Implications:
    # NOT(x_a == va) -> (x_b == vb)
    # NOT(x_b == vb) -> (x_a == va)
    
    for l1, l2 in clauses:
        a = abs(l1)
        va = 1 if l1 > 0 else 0
        b = abs(l2)
        vb = 1 if l2 > 0 else 0
        
        # First implication: NOT(x_a == va) -> (x_b == vb)
        # NOT(x_a == va) is literal: (va == 1) ? (-a) : a
        # (x_b == vb) is literal: (vb == 1) ? b : (-b)
        lit_from = a if va == 1 else -a
        lit_to = b if vb == 1 else -b
        adj[lit_to_node(-lit_from)].append(lit_to_node(lit_to))
        adj_rev[lit_to_node(lit_to)].append(lit_to_node(-lit_from))
        
        # Second implication: NOT(x_b == vb) -> (x_a == va)
        lit_from2 = b if vb == 1 else -b
        lit_to2 = a if va == 1 else -a
        adj[lit_to_node(-lit_from2)].append(lit_to_node(lit_to2))
        adj_rev[lit_to_node(lit_to2)].append(lit_to_node(-lit_from2))
    
    # Kosaraju's algorithm for SCC
    visited = [False] * (2 * n + 1)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(1, 2 * n + 1):
        if not visited[i]:
            dfs1(i)
    
    # Reverse the order
    order.reverse()
    
    # Reset visited for second DFS
    visited = [False] * (2 * n + 1)
    components = [0] * (2 * n + 1)
    comp_num = 0
    
    def dfs2(u):
        visited[u] = True
        components[u] = comp_num
        for v in adj_rev[u]:
            if not visited[v]:
                dfs2(v)
    
    for u in order:
        if not visited[u]:
            comp_num += 1
            dfs2(u)
    
    # Check if any variable and its negation are in the same SCC
    for i in range(1, n + 1):
        node_pos = i
        node_neg = n + i
        if components[node_pos] == components[node_neg]:
            print("NO")
            return
    
    # Assign values based on component numbers
    assignment = [0] * (n + 1)
    # Process components in topological order (reverse of finishing order)
    # Components with higher number come first
    for u in order:
        lit = node_to_lit(u)
        var = abs(lit)
        if assignment[var] == 0:
            # Assign value consistent with literal
            if lit > 0:
                assignment[var] = 1
            else:
                assignment[var] = 0
    
    print("YES")
    result = []
    for i in range(1, n + 1):
        result.append(str(assignment[i]))
    print(" ".join(result))

threading.Thread(target=main).start()