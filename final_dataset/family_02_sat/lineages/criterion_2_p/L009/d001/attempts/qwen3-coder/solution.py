import sys
import threading

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    clauses = []
    index = 2
    for _ in range(m):
        l1 = int(data[index])
        l2 = int(data[index+1])
        index += 2
        clauses.append((l1, l2))
    
    # Create implication graph
    # Variables: 1 to n (positive), -1 to -n (negative)
    # We'll use node IDs: 1 to n for x_i, n+1 to 2n for NOT x_i
    adj = [[] for _ in range(2 * n + 1)]
    rev_adj = [[] for _ in range(2 * n + 1)]
    
    def var_to_node(x):
        if x > 0:
            return x
        else:
            return n + (-x)
    
    def node_to_var(node):
        if node <= n:
            return node
        else:
            return -(node - n)
    
    # For each clause (a OR b), we add edges:
    # NOT a -> b and NOT b -> a
    for l1, l2 in clauses:
        # NOT l1 -> l2
        # NOT l2 -> l1
        not_l1 = -l1
        not_l2 = -l2
        
        # Map literals to nodes
        # For literal x, node is x if x>0, else n+(-x)
        # For NOT literal, it's the opposite
        src1 = var_to_node(not_l1)
        dst1 = var_to_node(l2)
        
        src2 = var_to_node(not_l2)
        dst2 = var_to_node(l1)
        
        adj[src1].append(dst1)
        adj[src2].append(dst2)
        
        rev_adj[dst1].append(src1)
        rev_adj[dst2].append(src2)
    
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
    
    visited = [False] * (2 * n + 1)
    scc_id = [0] * (2 * n + 1)
    cid = [0]
    
    def dfs2(u, cid_val):
        visited[u] = True
        scc_id[u] = cid_val
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v, cid_val)
    
    order.reverse()
    current_cid = 1
    for u in order:
        if not visited[u]:
            dfs2(u, current_cid)
            current_cid += 1
    
    # Check if any variable and its negation are in the same SCC
    for i in range(1, n + 1):
        pos_node = var_to_node(i)       # x_i
        neg_node = var_to_node(-i)      # NOT x_i
        if scc_id[pos_node] == scc_id[neg_node]:
            print("NO")
            return
    
    # Assign values based on topological order of SCCs
    assignment = [0] * (n + 1)
    # Create list of (scc_id, node)
    scc_order = [(scc_id[u], u) for u in range(1, 2*n + 1)]
    scc_order.sort(reverse=True)  # Process from highest SCC id first
    
    assigned = [False] * (n + 1)
    for _, u in scc_order:
        var = node_to_var(u)
        idx = abs(var)
        if idx == 0:
            continue
        if not assigned[idx]:
            if var > 0:
                assignment[idx] = 1
            else:
                assignment[idx] = 0
            assigned[idx] = True
    
    print("YES")
    print(' '.join(str(assignment[i]) for i in range(1, n + 1)))

threading.Thread(target=main).start()