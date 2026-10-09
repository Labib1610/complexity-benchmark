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
    idx = 2
    for _ in range(m):
        c1 = int(data[idx])
        c2 = int(data[idx+1])
        idx += 2
        clauses.append((c1, c2))
    
    # Create implication graph for 2-SAT
    # Variables: 0 to n-1 (for valves 1 to n being open)
    #            n to 2n-1 (for valves 1 to n being closed)
    # But we'll use a more standard approach with variables 1..n and -1..-n
    
    # For each clause (a OR b), we add edges (~a -> b) and (~b -> a)
    # Node representation: for variable x (1-based), 
    #                      x represents x is True (open if x>0, closed if x<0 handled specially)
    #                     -x represents x is False
    # But it's easier to map: for valve i (1-based):
    #                         node i: valve i is open
    #                        -i: valve i is closed
    
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    for c1, c2 in clauses:
        # c1 OR c2 must be true
        # which means (~c1 -> c2) AND (~c2 -> c1)
        
        # Normalize to get the actual variable and whether it's negated
        if c1 > 0:
            var1, neg1 = c1, False  # var1 is open
        else:
            var1, neg1 = -c1, True  # var1 is closed
            
        if c2 > 0:
            var2, neg2 = c2, False  # var2 is open
        else:
            var2, neg2 = -c2, True  # var2 is closed
            
        # Add implications
        # (~c1 -> c2)
        if not neg1:  # c1 is (var1 open), so ~c1 is (var1 closed) i.e. -var1
            u = -var1
        else:         # c1 is (var1 closed), so ~c1 is (var1 open) i.e. var1
            u = var1
            
        if not neg2:  # c2 is (var2 open) i.e. var2
            v = var2
        else:         # c2 is (var2 closed) i.e. -var2
            v = -var2
            
        adj[u].append(v)
        rev_adj[v].append(u)
        
        # (~c2 -> c1)
        if not neg2:  # c2 is (var2 open), so ~c2 is (var2 closed) i.e. -var2
            u = -var2
        else:         # c2 is (var2 closed), so ~c2 is (var2 open) i.e. var2
            u = var2
            
        if not neg1:  # c1 is (var1 open) i.e. var1
            v = var1
        else:         # c1 is (var1 closed) i.e. -var1
            v = -var1
            
        adj[u].append(v)
        rev_adj[v].append(u)
    
    # Kosaraju's algorithm for SCC
    visited = set()
    order = []
    
    def dfs1(u):
        visited.add(u)
        for v in adj[u]:
            if v not in visited:
                dfs1(v)
        order.append(u)
    
    # Run DFS1 on all nodes
    nodes = set()
    for u in adj:
        nodes.add(u)
    for u in rev_adj:
        nodes.add(u)
        
    for u in nodes:
        if u not in visited:
            dfs1(u)
    
    # Second DFS on transpose graph in reverse order
    visited.clear()
    scc_map = {}
    scc_id = 0
    
    def dfs2(u):
        visited.add(u)
        scc_map[u] = scc_id
        for v in rev_adj[u]:
            if v not in visited:
                dfs2(v)
    
    while order:
        u = order.pop()
        if u not in visited:
            dfs2(u)
            scc_id += 1
    
    # Check for contradiction: variable and its negation in same SCC
    for i in range(1, n+1):
        if scc_map.get(i, -1) == scc_map.get(-i, -2):
            print("NO")
            return
    
    # Assign values: process SCCs in topological order
    # We can do this by processing in reverse finish time of first DFS
    assignment = {}
    
    # Re-process order in reverse to assign truth values
    for u in reversed(order):
        if u not in assignment:
            # Assign true to all in this SCC
            stack = [u]
            while stack:
                v = stack.pop()
                if v in assignment:
                    continue
                assignment[v] = True
                assignment[-v] = False
                for w in adj[v]:
                    if w not in assignment:
                        stack.append(w)
                        
    # Build result
    result = []
    for i in range(1, n+1):
        if assignment.get(i, False):
            result.append('1')  # open
        else:
            result.append('0')  # closed
            
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()