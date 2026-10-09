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
    index = 2
    for _ in range(m):
        l1 = int(data[index])
        l2 = int(data[index+1])
        index += 2
        clauses.append((l1, l2))
    
    # Convert to 2-SAT format
    # Variables are 1-indexed. We'll use 0-indexed internally by subtracting 1
    # For variable x (1-based), x is True if toggle x is ON, False if OFF
    # -x means toggle x is OFF, which is NOT(x-1)
    
    # Build implication graph
    # Each variable has two nodes: 2*(x-1) for x being False, 2*(x-1)+1 for x being True
    # We'll use adjacency list
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    for l1, l2 in clauses:
        # Clause (l1 OR l2) is equivalent to (NOT l1 -> l2) AND (NOT l2 -> l1)
        # l1 can be positive (x) or negative (-x)
        # If l1 is positive, NOT l1 is node 2*(l1-1)
        # If l1 is negative, NOT l1 is node 2*(-l1-1)+1
        # Similarly for l2
        
        # First implication: NOT l1 -> l2
        if l1 > 0:
            # NOT (l1 is ON) -> (l2 is ON)
            # Node for (l1 is OFF) is 2*(l1-1)
            u = 2 * (l1 - 1)
        else:
            # NOT (l1 is OFF) -> (l2 is ON) 
            # Node for (l1 is ON) is 2*(-l1-1)+1
            u = 2 * (-l1 - 1) + 1
            
        if l2 > 0:
            # (l2 is ON) is node 2*(l2-1)+1
            v = 2 * (l2 - 1) + 1
        else:
            # (l2 is OFF) is node 2*(-l2-1)
            v = 2 * (-l2 - 1)
            
        adj[u].append(v)
        rev_adj[v].append(u)
        
        # Second implication: NOT l2 -> l1
        if l2 > 0:
            # NOT (l2 is ON) -> (l1 is ON)
            # Node for (l2 is OFF) is 2*(l2-1)
            u2 = 2 * (l2 - 1)
        else:
            # NOT (l2 is OFF) -> (l1 is ON)
            # Node for (l2 is ON) is 2*(-l2-1)+1
            u2 = 2 * (-l2 - 1) + 1
            
        if l1 > 0:
            # (l1 is ON) is node 2*(l1-1)+1
            v2 = 2 * (l1 - 1) + 1
        else:
            # (l1 is OFF) is node 2*(-l1-1)
            v2 = 2 * (-l1 - 1)
            
        adj[u2].append(v2)
        rev_adj[v2].append(u2)
    
    # Kosaraju's algorithm for SCC
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
    
    # Reverse graph DFS
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
        # Variable i corresponds to nodes 2*i and 2*i+1
        if scc_id[2*i] == scc_id[2*i+1]:
            print("NO")
            return
    
    # Build solution
    # In the toposort of SCCs, if NOT x appears in a later SCC than x,
    # then x should be True
    result = [0] * n
    for i in range(n):
        if scc_id[2*i] > scc_id[2*i+1]:
            result[i] = 1
    
    print("YES")
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()