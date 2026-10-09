import sys
sys.setrecursionlimit(10**6)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build implication graph
    # Variables: 0 to n-1 represent mode 0, n to 2n-1 represent mode 1
    # But we'll use 0..n-1 for mode 0 (x_i = 0) and n..2n-1 for mode 1 (x_i = 1)
    # Actually, let's map variable x_i (0-based index) to node 2*i (mode 0) and 2*i+1 (mode 1)
    # But easier: let's have nodes 0..n-1 for x_i=0 and n..2n-1 for x_i=1
    
    adj = [[] for _ in range(2 * n)]
    rev_adj = [[] for _ in range(2 * n)]
    
    index = 2
    for i in range(m):
        c1 = int(data[index])
        c2 = int(data[index + 1])
        index += 2
        
        # c1 corresponds to machine |c1|-1
        # if c1 > 0, high when mode 0 => forbid x_(|c1|-1)=1
        # if c1 < 0, high when mode 1 => forbid x_(|c1|-1)=0
        # Similarly for c2
        
        # Forbid (c1 high AND c2 high)
        # If c1 high -> NOT(c2 high)
        # If c2 high -> NOT(c1 high)
        
        # Let's define:
        # Node i (0 <= i < n): x_i = 0 (machine i+1 in mode 0)
        # Node i+n (n <= i < 2n): x_i = 1 (machine i-n+1 in mode 1)
        
        # c1 high when:
        #   if c1 > 0: x_(c1-1) = 0 => node (c1-1)
        #   if c1 < 0: x_(-c1-1) = 1 => node (-c1-1)+n
        # Same for c2
        
        v1 = (abs(c1) - 1) + n * (c1 < 0)  # node where c1 is high
        v2 = (abs(c2) - 1) + n * (c2 < 0)  # node where c2 is high
        
        # Add implications: NOT(v1) OR NOT(v2) 
        # which is equivalent to v1 -> NOT(v2) and v2 -> NOT(v1)
        not_v2 = (v2 + n) % (2 * n)  # negation of v2
        not_v1 = (v1 + n) % (2 * n)  # negation of v1
        
        adj[v1].append(not_v2)
        adj[v2].append(not_v1)
        rev_adj[not_v2].append(v1)
        rev_adj[not_v1].append(v2)
    
    # Now run 2-SAT using Kosaraju's algorithm
    # Find SCCs and check if x_i and NOT(x_i) are in same SCC
    
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
    
    visited = [False] * (2 * n)
    components = [-1] * (2 * n)
    comp_id = 0
    
    def dfs2(u):
        visited[u] = True
        components[u] = comp_id
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v)
    
    for i in reversed(order):
        if not visited[i]:
            dfs2(i)
            comp_id += 1
    
    # Check satisfiability
    for i in range(n):
        if components[i] == components[i + n]:
            print("NO")
            return
    
    print("YES")
    assignment = [0] * n
    # Process components in reverse topological order
    comp_order = list(range(comp_id))
    # Actually, we just need to assign values based on component indices
    # Component with higher index in order comes first in reverse topo sort
    comp_to_val = {}
    for i in range(2 * n):
        cid = components[i]
        if cid not in comp_to_val:
            comp_to_val[cid] = None
            
    # Assign truth values
    for i in range(2 * n):
        cid = components[i]
        if comp_to_val[cid] is None:
            # Determine what this component should be
            # If there's a conflict, we take the one that makes more sense
            # Actually, since SAT, we can assign true to the later component in order
            # In Kosaraju, last finished component gets processed first
            # So higher component id means earlier in finishing time
            # We want to set variables to satisfy clauses
            # Simpler approach: for each variable, pick the value of the literal 
            # whose component appears later in the topological order of SCCs
            pass
    
    # Better way: process in reverse topological order of SCCs
    # Create mapping from component to literals in it
    comp_literals = [[] for _ in range(comp_id)]
    for i in range(2 * n):
        comp_literals[components[i]].append(i)
    
    assigned = [False] * n
    values = [0] * n
    
    # Process components in reverse topological order (decreasing component id)
    for cid in reversed(range(comp_id)):
        for node in comp_literals[cid]:
            var = node % n
            val = 0 if node < n else 1
            if not assigned[var]:
                assigned[var] = True
                values[var] = val
                
    print(' '.join(map(str, values)))

if __name__ == "__main__":
    main()