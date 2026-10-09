import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # Build implication graph for 2-SAT
    # Variables: 0 to n-1 represent s[0]=0, s[0]=1, ..., s[n-1]=0, s[n-1]=1
    # But we'll use a more standard approach:
    # For variable i (0-based), i*2 represents x_i = 0, i*2+1 represents x_i = 1
    
    adj = [[] for _ in range(2 * n)]
    rev_adj = [[] for _ in range(2 * n)]
    
    # For each interlock (l1, l2), we need to ensure that NOT (condition1 AND condition2)
    # This is equivalent to (NOT condition1) OR (NOT condition2)
    # Which translates to implications: condition1 -> NOT condition2, condition2 -> NOT condition1
    
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        # Convert to 0-based indexing
        # l1 > 0 means array |l1|-1 is in mode 0
        # l1 < 0 means array |l1|-1 is in mode 1
        # Similarly for l2
        
        # Node indices:
        # For array i: node 2*i represents s[i]=0, node 2*i+1 represents s[i]=1
        
        if l1 > 0:
            # l1 condition: s[l1-1] = 0, which is node 2*(l1-1)
            node1 = 2 * (l1 - 1)
        else:
            # l1 condition: s[-l1-1] = 1, which is node 2*(-l1-1)+1
            node1 = 2 * (-l1 - 1) + 1
            
        if l2 > 0:
            # l2 condition: s[l2-1] = 0, which is node 2*(l2-1)
            node2 = 2 * (l2 - 1)
        else:
            # l2 condition: s[-l2-1] = 1, which is node 2*(-l2-1)+1
            node2 = 2 * (-l2 - 1) + 1
            
        # Add implications:
        # If node1 is true, then node2 must be false => node1 -> NOT node2
        # If node2 is true, then node1 must be false => node2 -> NOT node1
        
        # In implication graph:
        # node1 -> NOT node2  is  node1 -> (node2^1)
        # node2 -> NOT node1  is  node2 -> (node1^1)
        
        adj[node1].append(node2 ^ 1)
        adj[node2].append(node1 ^ 1)
        
        rev_adj[node2 ^ 1].append(node1)
        rev_adj[node1 ^ 1].append(node2)
    
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
    
    # Construct solution
    # Assign values based on topological order of SCCs
    # Variables in later SCCs (higher id) are assigned True first
    assignment = [False] * n
    
    # Create a list of (scc_id, node) and sort by scc_id descending
    scc_order = [(scc_id[i], i) for i in range(2 * n)]
    scc_order.sort(reverse=True)
    
    assigned = [False] * n
    
    for _, node in scc_order:
        var = node // 2
        if assigned[var]:
            continue
        # If node is 2*var, it represents var=0
        # If node is 2*var+1, it represents var=1
        if node % 2 == 0:
            assignment[var] = False  # s[var] = 0
        else:
            assignment[var] = True   # s[var] = 1
        assigned[var] = True
    
    print("YES")
    print(' '.join(str(int(b)) for b in assignment))

threading.Thread(target=main).start()