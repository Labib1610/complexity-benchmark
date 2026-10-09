import sys
sys.setrecursionlimit(1000000)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # For each variable x_i, we create two nodes:
    # Node 2*i represents x_i (positive literal)
    # Node 2*i + 1 represents not x_i (negative literal)
    # We'll build implication graph and find strongly connected components
    
    adj = [[] for _ in range(2 * (n + 1))]
    adj_rev = [[] for _ in range(2 * (n + 1))]
    
    index = 2
    for i in range(m):
        l1 = int(data[index])
        l2 = int(data[index + 1])
        index += 2
        
        # clause (l1 OR l2) is equivalent to (not l1 -> l2) AND (not l2 -> l1)
        # Convert literals to node indices
        if l1 > 0:
            node_l1_F = 2 * l1 + 1  # not x_{l1}
            node_l1_T = 2 * l1      # x_{l1}
        else:
            node_l1_F = 2 * (-l1)    # not (not x_{-l1}) = x_{-l1}
            node_l1_T = 2 * (-l1) + 1 # not x_{-l1}
            
        if l2 > 0:
            node_l2_F = 2 * l2 + 1   # not x_{l2}
            node_l2_T = 2 * l2       # x_{l2}
        else:
            node_l2_F = 2 * (-l2)     # not (not x_{-l2}) = x_{-l2}
            node_l2_T = 2 * (-l2) + 1 # not x_{-l2}
            
        # Add edges for implications
        adj[node_l1_F].append(node_l2_T)
        adj[node_l2_F].append(node_l1_T)
        adj_rev[node_l2_T].append(node_l1_F)
        adj_rev[node_l1_T].append(node_l2_F)
        
    # Kosaraju's algorithm for SCC
    visited = [False] * (2 * (n + 1))
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
        
    for i in range(2, 2 * (n + 1)):
        if not visited[i]:
            dfs1(i)
            
    # Second DFS on transpose graph
    visited = [False] * (2 * (n + 1))
    scc_id = [-1] * (2 * (n + 1))
    scc_count = 0
    
    def dfs2(u):
        visited[u] = True
        scc_id[u] = scc_count
        for v in adj_rev[u]:
            if not visited[v]:
                dfs2(v)
                
    while order:
        u = order.pop()
        if not visited[u]:
            dfs2(u)
            scc_count += 1
            
    # Check for contradiction: x_i and not x_i in same SCC
    for i in range(1, n + 1):
        pos = 2 * i
        neg = 2 * i + 1
        if scc_id[pos] == scc_id[neg]:
            print("NO")
            return
            
    # Assign values based on SCC topological order
    # Variables in later SCCs are assigned True
    assignment = [False] * (n + 1)
    scc_order = [-1] * scc_count
    for i in range(2, 2 * (n + 1)):
        scc = scc_id[i]
        if scc_order[scc] == -1:
            if i % 2 == 0:  # Positive literal x_j
                j = i // 2
                if scc_order[scc_id[2*j+1]] == -1:  # not x_j not yet ordered
                    scc_order[scc] = 0  # x_j gets False, not x_j gets True
                    scc_order[scc_id[2*j+1]] = 1
                else:
                    scc_order[scc] = 1 - scc_order[scc_id[2*j+1]]
            else:  # Negative literal not x_j
                j = (i - 1) // 2
                if scc_order[scc_id[2*j]] == -1:  # x_j not yet ordered
                    scc_order[scc] = 1  # not x_j gets True, x_j gets False
                    scc_order[scc_id[2*j]] = 0
                else:
                    scc_order[scc] = 1 - scc_order[scc_id[2*j]]
                    
    for i in range(1, n + 1):
        if scc_order[scc_id[2*i]] == 1:
            assignment[i] = True
        else:
            assignment[i] = False
            
    print("YES")
    result = []
    for i in range(1, n + 1):
        result.append('1' if assignment[i] else '0')
    print(' '.join(result))

if __name__ == "__main__":
    main()