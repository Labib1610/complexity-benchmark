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
        print(" ".join(["1"] * n))
        return
    
    # For each microservice, we'll create two nodes: i (Primary) and -i (Secondary)
    # We'll build implication graph for 2-SAT
    
    # For each clause (l1 OR l2), we add edges:
    # NOT l1 -> l2 and NOT l2 -> l1
    
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    idx = 2
    for i in range(m):
        l1 = int(data[idx])
        l2 = int(data[idx+1])
        idx += 2
        
        # Add implications:
        # NOT l1 -> l2  ===  -l1 -> l2
        # NOT l2 -> l1  ===  -l2 -> l1
        
        adj[-l1].append(l2)
        adj[-l2].append(l1)
        rev_adj[l2].append(-l1)
        rev_adj[l1].append(-l2)
    
    # Kosaraju's algorithm for SCC
    visited = set()
    order = []
    
    def dfs1(u):
        visited.add(u)
        for v in adj[u]:
            if v not in visited:
                dfs1(v)
        order.append(u)
    
    # Collect all nodes
    nodes = set()
    for u in adj:
        nodes.add(u)
        for v in adj[u]:
            nodes.add(v)
    
    for u in nodes:
        if u not in visited:
            dfs1(u)
    
    visited = set()
    scc = {}
    scc_id = 0
    
    def dfs2(u):
        visited.add(u)
        scc[u] = scc_id
        for v in rev_adj[u]:
            if v not in visited:
                dfs2(v)
    
    while order:
        u = order.pop()
        if u not in visited:
            dfs2(u)
            scc_id += 1
    
    # Check if any variable and its negation are in the same SCC
    for i in range(1, n+1):
        if i in scc and -i in scc and scc[i] == scc[-i]:
            print("NO")
            return
    
    # Assign values: process SCCs in reverse topological order
    # We can do this by processing in the order of finishing times reversed
    assignment = {}
    
    # Process nodes in reverse order of finishing time
    for u in reversed(list(order)):
        if u not in assignment:
            # Assign True to u, False to -u if they exist
            if u > 0 and -u in nodes:
                if u not in assignment:
                    assignment[u] = 1
                if -u not in assignment:
                    assignment[-u] = 0
            elif u < 0 and (-u) in nodes:
                if u not in assignment:
                    assignment[u] = 1  # u is -i, so i gets 0
                if -u not in assignment:
                    assignment[-u] = 0  # -u is i, so i gets 0, u=-i gets 1
            else:
                # Isolated node
                assignment[abs(u)] = 1 if u > 0 else 0
    
    # Ensure all variables are assigned
    result = []
    for i in range(1, n+1):
        if i in assignment:
            result.append(str(assignment[i]))
        else:
            # Default assignment if not constrained
            result.append("1")
    
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()