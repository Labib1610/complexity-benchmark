import sys
sys.setrecursionlimit(1000000)

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
    
    # Build implication graph
    # Variables: 1 to n (positive), -1 to -n (negative)
    # Nodes: 0 to 2n-1 representing variables 1 to n and their negations
    # node i represents variable i+1, node i+n represents negation of variable i+1
    
    adj = [[] for _ in range(2 * n)]
    rev_adj = [[] for _ in range(2 * n)]
    
    # For clause (a OR b), we add edges (~a -> b) and (~b -> a)
    for l1, l2 in clauses:
        # Convert to 0-based indexing
        # l1 positive: variable l1, node l1-1
        # l1 negative: variable -l1, node (-l1-1)+n = n-l1-1
        if l1 > 0:
            node_not_l1 = n + l1 - 1  # ~l1
            if l2 > 0:
                node_l2 = l2 - 1
            else:
                node_l2 = n - (-l2) - 1
        else:
            node_not_l1 = -l1 - 1  # ~l1 (which is l1)
            if l2 > 0:
                node_l2 = l2 - 1
            else:
                node_l2 = n - (-l2) - 1
        
        if l2 > 0:
            node_not_l2 = n + l2 - 1  # ~l2
            if l1 > 0:
                node_l1 = l1 - 1
            else:
                node_l1 = n - (-l1) - 1
        else:
            node_not_l2 = -l2 - 1  # ~l2 (which is l2)
            if l1 > 0:
                node_l1 = l1 - 1
            else:
                node_l1 = n - (-l1) - 1
                
        adj[node_not_l1].append(node_l2)
        adj[node_not_l2].append(node_l1)
        rev_adj[node_l2].append(node_not_l1)
        rev_adj[node_l1].append(node_not_l2)
    
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
            
    # Check if x and ~x are in the same SCC
    for i in range(n):
        if scc_id[i] == scc_id[n + i]:
            print("NO")
            return
            
    print("YES")
    
    # Assign values based on topological order of SCCs
    # Variables in later SCCs (higher id) should be assigned False first
    assignment = [-1] * n
    scc_to_vars = [[] for _ in range(scc_count)]
    
    for i in range(2 * n):
        scc_to_vars[scc_id[i]].append(i)
        
    for comp_id in reversed(range(scc_count)):
        for node in scc_to_vars[comp_id]:
            if node < n:  # Positive variable
                var = node
                if assignment[var] == -1:
                    assignment[var] = 0
            else:  # Negative variable
                var = node - n
                if assignment[var] == -1:
                    assignment[var] = 1
                    
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    main()