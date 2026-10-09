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
    
    # Build implication graph
    # Variables: for switch i, we have variables 2*i (for s_i=0) and 2*i+1 (for s_i=1)
    # But easier to think in terms of literals: +i means s_i=1, -i means s_i=0
    # For literal l, variable is 2*|l| + (0 if l>0 else 1)
    
    # We'll build a 2-SAT instance
    # For each relay with literals l1, l2:
    # Add clause (~l1 OR ~l2) which is equivalent to (l1 => ~l2) AND (l2 => ~l1)
    # Which means if l1 is true, then ~l2 must be true, etc.
    
    # Let's use a different approach: for each relay (a,b), at least one must hold
    # So NOT(a AND b) = NOT(a) OR NOT(b)
    # This means if a holds, then NOT(b) must hold, and vice versa
    
    # Let's define variables: for switch i (1-based), 
    # var i represents s_i=1, and var -i represents s_i=0
    
    adj = defaultdict(list)  # adjacency list for implications
    adj_rev = defaultdict(list)  # reverse adjacency list
    
    index = 2
    while index < len(data):
        l1 = int(data[index])
        l2 = int(data[index+1])
        index += 2
        
        # Clause: NOT(l1 is true AND l2 is true)
        # This is equivalent to: NOT(l1) OR NOT(l2)
        # In implication form: l1 -> NOT(l2) and l2 -> NOT(l1)
        
        # l1 implies NOT l2
        adj[-l1].append(l2)
        adj_rev[l2].append(-l1)
        
        # l2 implies NOT l1  
        adj[-l2].append(l1)
        adj_rev[l1].append(-l2)
    
    # Now we do Kosaraju's algorithm for 2-SAT
    # First DFS on original graph to get finishing times
    visited = set()
    order = []
    
    def dfs1(u):
        if u in visited:
            return
        visited.add(u)
        for v in adj[u]:
            dfs1(v)
        order.append(u)
    
    # Collect all nodes
    nodes = set()
    for u in adj:
        nodes.add(u)
        for v in adj[u]:
            nodes.add(v)
    for u in adj_rev:
        nodes.add(u)
        for v in adj_rev[u]:
            nodes.add(v)
            
    for node in nodes:
        dfs1(node)
    
    # Second DFS on transpose graph in reverse finish order
    visited.clear()
    components = {}
    component_num = 0
    
    def dfs2(u):
        if u in visited:
            return
        visited.add(u)
        components[u] = component_num
        for v in adj_rev[u]:
            dfs2(v)
    
    order.reverse()
    for u in order:
        if u not in visited:
            dfs2(u)
            component_num += 1
            
    # Check if any variable and its negation are in the same SCC
    for i in range(1, n+1):
        if components.get(i, -1) == components.get(-i, -1):
            print("NO")
            return
            
    # Assign values based on topological order of SCCs
    # Variables in later components (higher number) are assigned TRUE
    assignment = {}
    
    # Process components in reverse topological order (component_num-1 down to 0)
    for i in range(1, n+1):
        pos_comp = components.get(i, 0)
        neg_comp = components.get(-i, 0)
        if pos_comp > neg_comp:
            assignment[i] = 1
        else:
            assignment[i] = 0
            
    print("YES")
    result = [str(assignment[i]) for i in range(1, n+1)]
    print(" ".join(result))

if __name__ == "__main__":
    main()