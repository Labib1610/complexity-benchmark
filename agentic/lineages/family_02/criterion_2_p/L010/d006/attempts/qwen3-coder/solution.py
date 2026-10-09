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
    
    # For each filter (l1, l2), we derive a constraint
    # Let's convert to 2-SAT
    # Each variable x_i corresponds to transmitter i being 1 (if x_i is True) or 0 (if x_i is False)
    
    # We'll build a graph for 2-SAT
    # Variables: 0 to n-1 for x_i (transmitter i is 1)
    #            n to 2n-1 for not x_i (transmitter i is 0)
    # But it's easier to work with signed indices: +i for x_i, -i for not x_i
    
    adj = defaultdict(list)
    adj_rev = defaultdict(list)
    
    # Process each filter
    idx = 2
    for _ in range(m):
        l1 = int(data[idx])
        l2 = int(data[idx+1])
        idx += 2
        
        # Transmitter indices (1-based to 0-based)
        t1 = abs(l1) - 1
        t2 = abs(l2) - 1
        
        # Signs
        s1 = 1 if l1 > 0 else -1
        s2 = 1 if l2 > 0 else -1
        
        # The constraint is R >= B
        # R = v1*s1 + v2*s2
        # B = (s1 + s2)/2
        # So v1*s1 + v2*s2 >= (s1 + s2)/2
        
        # Let's multiply by 2 to avoid fractions:
        # 2*(v1*s1 + v2*s2) >= s1 + s2
        
        # Now we enumerate all possible (v1, v2) in {0,1}x{0,1} and see which satisfy the constraint
        # v1=0, v2=0: 0 >= s1+s2 ?
        # v1=0, v2=1: s2 >= s1+s2 ?  => s2 - s1 - s2 >= 0 ? => -s1 >= 0 ? => s1 <= 0
        # v1=1, v2=0: s1 >= s1+s2 ?  => s1 - s1 - s2 >= 0 ? => -s2 >= 0 ? => s2 <= 0
        # v1=1, v2=1: s1+s2 >= s1+s2 ? => always true
        
        # So the forbidden assignments are those that make R < B
        # That is: 2*(v1*s1 + v2*s2) < s1 + s2
        
        forbidden = []
        for v1 in (0,1):
            for v2 in (0,1):
                R = v1 * s1 + v2 * s2
                B = (s1 + s2) / 2
                if R < B:
                    forbidden.append((v1, v2))
        
        # For each forbidden assignment (a,b), we add a 2-SAT clause
        # meaning NOT(x1=a AND x2=b)
        # which is equivalent to (x1 != a OR x2 != b)
        # which is (x1 = not a OR x2 = not b)
        
        for v1, v2 in forbidden:
            # x1 != v1 OR x2 != v2
            # In terms of literals:
            # if v1 == 1, then we want (not x1) => literal -t1-1
            # if v1 == 0, then we want x1 => literal t1
            # same for t2 and v2
            
            lit1 = -(t1+1) if v1 == 1 else (t1+1)
            lit2 = -(t2+1) if v2 == 1 else (t2+1)
            
            # Add clause (lit1 OR lit2)
            # In implication graph: (not lit1) => lit2 and (not lit2) => lit1
            adj[-lit1].append(lit2)
            adj[-lit2].append(lit1)
            adj_rev[lit2].append(-lit1)
            adj_rev[lit1].append(-lit2)
    
    # Now we do 2-SAT solving using Kosaraju's algorithm
    # Nodes are literals: 1 to n for x_i, -1 to -n for not x_i
    
    visited = set()
    order = []
    
    def dfs1(u):
        visited.add(u)
        for v in adj[u]:
            if v not in visited:
                dfs1(v)
        order.append(u)
    
    # First DFS on original graph
    all_nodes = set()
    for u in adj:
        all_nodes.add(u)
        for v in adj[u]:
            all_nodes.add(v)
    
    for u in all_nodes:
        if u not in visited:
            dfs1(u)
    
    # Second DFS on transpose graph in reverse order
    visited.clear()
    components = {}
    component_count = 0
    
    def dfs2(u):
        visited.add(u)
        components[u] = component_count
        for v in adj_rev[u]:
            if v not in visited:
                dfs2(v)
    
    while order:
        u = order.pop()
        if u not in visited:
            dfs2(u)
            component_count += 1
    
    # Check if for any variable x_i, both i and -i are in the same SCC
    for i in range(1, n+1):
        if components.get(i, -1) == components.get(-i, -2):
            print("NO")
            return
    
    # Otherwise, there exists a solution
    # Assign values based on topological order of SCCs
    # Variables in later SCCs (higher component number) are assigned True
    
    assignment = [None] * (n+1)  # 1-based indexing
    
    # Sort variables by component number
    var_to_comp = [(components.get(i, -1), i) for i in range(1, n+1)]
    var_to_comp.sort()
    
    for comp, var in var_to_comp:
        if assignment[var] is None:
            # Assign False to var, True to -var
            assignment[var] = 0
            if -var in components:
                # This is handled by the component logic
                pass
    
    # But we need to be more careful. 
    # Let's re-assign based on component numbers.
    # For each variable, if comp(var) > comp(-var), then var = True
    # elif comp(var) < comp(-var), then var = False
    # else (same component) => contradiction (already handled)
    
    result = [0] * n
    for i in range(1, n+1):
        comp_pos = components.get(i, -1)
        comp_neg = components.get(-i, -1)
        if comp_pos > comp_neg:
            result[i-1] = 1
        else:
            result[i-1] = 0
    
    print("YES")
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()