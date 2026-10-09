import sys
from collections import defaultdict

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
    
    clauses = []
    pos = 2
    for _ in range(m):
        c1 = int(data[pos])
        c2 = int(data[pos+1])
        pos += 2
        # clause is: not both linkages have negative torque
        # torque1 = c1*(2*s_{|c1|} - 1)
        # torque2 = c2*(2*s_{|c2|} - 1)
        # We want NOT (torque1 < 0 AND torque2 < 0)
        # This is equivalent to: torque1 >= 0 OR torque2 >= 0
        # Which means: c1*(2*s_{|c1|} - 1) >= 0 OR c2*(2*s_{|c2|} - 1) >= 0
        
        # Let's define boolean variables:
        # For machine u, let x_u = True mean s_u = 1, x_u = False mean s_u = 0
        # Then torque for c is c*(2*s_u - 1) = c*(2*x_u - 1)
        # So torque >= 0 iff c*(2*x_u - 1) >= 0
        # This is equivalent to:
        # if c > 0: 2*x_u - 1 >= 0 => x_u >= 1/2 => x_u = True
        # if c < 0: 2*x_u - 1 <= 0 => x_u <= 1/2 => x_u = False
        
        # So clause becomes:
        # (x_{|c1|} = (c1>0)) OR (x_{|c2|} = (c2>0))
        # Which is a 2-SAT clause
        
        u1 = abs(c1)
        u2 = abs(c2)
        sign1 = c1 > 0
        sign2 = c2 > 0
        # Add clause: x_u1 = sign1 OR x_u2 = sign2
        # In 2-SAT form: (x_u1 OR x_u2) if sign1 and sign2
        #                (x_u1 OR ~x_u2) if sign1 and not sign2
        #                (~x_u1 OR x_u2) if not sign1 and sign2
        #                (~x_u1 OR ~x_u2) if not sign1 and not sign2
        
        lit1 = u1 if sign1 else -u1
        lit2 = u2 if sign2 else -u2
        clauses.append((lit1, lit2))
        
    # Now we solve 2-SAT
    # Variables are 1-indexed from 1 to n
    
    # Build implication graph
    adj = defaultdict(list)
    adj_rev = defaultdict(list)
    
    for lit1, lit2 in clauses:
        # clause (lit1 OR lit2) is equivalent to (~lit1 -> lit2) AND (~lit2 -> lit1)
        adj[-lit1].append(lit2)
        adj[-lit2].append(lit1)
        adj_rev[lit2].append(-lit1)
        adj_rev[lit1].append(-lit2)
        
    # Kosaraju's algorithm for SCC
    visited = [False] * (2 * n + 1)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
                
    def dfs2(u, component):
        visited[u] = True
        component.append(u)
        for v in adj_rev[u]:
            if not visited[v]:
                dfs2(v, component)
                
    # First pass
    for i in range(1, n+1):
        if not visited[i]:
            dfs1(i)
        if not visited[-i]:
            dfs1(-i)
            
    # Second pass
    visited = [False] * (2 * n + 1)
    components = {}
    comp_id = 0
    
    while order:
        u = order.pop()
        if not visited[u]:
            component = []
            dfs2(u, component)
            comp_id += 1
            for node in component:
                components[node] = comp_id
                
    # Check satisfiability
    assignment = [None] * (n+1)
    for i in range(1, n+1):
        if components[i] == components[-i]:
            print("NO")
            return
            
    # Assign values based on component numbers
    # Nodes with higher component id come first in topological order
    for i in range(1, n+1):
        if components[i] > components[-i]:
            assignment[i] = True
        else:
            assignment[i] = False
            
    print("YES")
    result = []
    for i in range(1, n+1):
        if assignment[i]:
            result.append("1")
        else:
            result.append("0")
    print(" ".join(result))

if __name__ == "__main__":
    main()