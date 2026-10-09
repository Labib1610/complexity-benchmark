import sys
import threading

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # We'll use 2*n variables: 0 to n-1 for positive literals, n to 2n-1 for negative
    # But it's easier to work with 1-based indexing and separate positive/negative
    # Let's use implication graph: for clause (a OR b), add edges (-a -> b) and (-b -> a)
    
    # We'll build implication graph and do SCC to check 2-SAT satisfiability
    
    # Number of variables: 2*n (x1, ..., xn, -x1, ..., -xn)
    # Actually, let's map variable i (1-based) to node 2*i and -i to node 2*i+1
    # But to simplify, we'll use nodes 0..2n-1 where 0..n-1 are x_i=1 and n..2n-1 are x_i=0
    
    adj = [[] for _ in range(2 * n)]
    rev_adj = [[] for _ in range(2 * n)]
    
    index = 2
    clauses = []
    for i in range(m):
        a = int(data[index])
        b = int(data[index + 1])
        index += 2
        clauses.append((a, b))
        
        # Convert to 0-based indices
        # For a OR b, we have implications: NOT a -> b and NOT b -> a
        # If a > 0, then NOT a is at index a+n-1
        # If a < 0, then NOT a is at index -a-1
        # Similarly for b
        
        # Node mapping:
        # Variable i (1-based) true: node i-1
        # Variable i (1-based) false: node n+i-1
        
        def var_node(v):
            if v > 0:
                return v - 1
            else:
                return n + (-v) - 1
                
        def not_var_node(v):
            if v > 0:
                return n + v - 1
            else:
                return (-v) - 1
        
        # Add implications
        # NOT a -> b
        adj[not_var_node(a)].append(var_node(b))
        rev_adj[var_node(b)].append(not_var_node(a))
        
        # NOT b -> a
        adj[not_var_node(b)].append(var_node(a))
        rev_adj[var_node(a)].append(not_var_node(b))
    
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
    
    # Reverse the graph and find SCCs
    visited = [False] * (2 * n)
    scc_id = [-1] * (2 * n)
    scc_count = 0
    
    def dfs2(u):
        visited[u] = True
        scc_id[u] = scc_count
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v)
    
    order.reverse()
    for u in order:
        if not visited[u]:
            dfs2(u)
            scc_count += 1
            
    # Check if any variable and its negation are in the same SCC
    for i in range(n):
        if scc_id[i] == scc_id[n + i]:
            print("NO")
            return
    
    # Assign values based on topological order of SCCs
    # Variables in later SCCs should be assigned TRUE
    assignment = [0] * n
    scc_order = [-1] * scc_count
    for i in range(2 * n):
        scc_order[scc_id[i]] = i
    
    # For each variable, decide its value
    for i in range(n):
        if scc_id[i] > scc_id[n + i]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    print("YES")
    print(' '.join(map(str, assignment)))

threading.Thread(target=main).start()