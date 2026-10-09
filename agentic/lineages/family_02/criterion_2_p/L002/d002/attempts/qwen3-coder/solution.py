import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # For each variable x_i, we have two nodes: 2*i (for x_i=0) and 2*i+1 (for x_i=1)
    # For literal l:
    #   if l > 0, then l corresponds to node 2*l + 1 (x_l = 1)
    #   if l < 0, then -l corresponds to node 2*(-l) (x_{-l} = 0)
    
    def lit_to_node(l):
        if l > 0:
            return 2 * l + 1
        else:
            return 2 * (-l)
    
    # Build implication graph
    # For each clause (l1 or l2), we add edges (!l1 -> l2) and (!l2 -> l1)
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    idx = 2
    for _ in range(m):
        l1 = int(data[idx])
        l2 = int(data[idx+1])
        idx += 2
        
        # clause (l1 or l2) is equivalent to (!l1 -> l2) and (!l2 -> l1)
        # !l1 is the negation of l1
        not_l1 = -l1
        not_l2 = -l2
        
        # Add edge: not_l1 -> l2
        u = lit_to_node(not_l1)
        v = lit_to_node(l2)
        adj[u].append(v)
        rev_adj[v].append(u)
        
        # Add edge: not_l2 -> l1
        u = lit_to_node(not_l2)
        v = lit_to_node(l1)
        adj[u].append(v)
        rev_adj[v].append(u)
    
    # Now we do 2-SAT solving using SCC
    # Nodes are numbered from 2 to 2*n+1
    
    # Kosaraju's algorithm
    visited = [False] * (2 * n + 2)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(2, 2*n + 2):
        if not visited[i]:
            dfs1(i)
    
    # Second DFS on reverse graph
    visited = [False] * (2 * n + 2)
    scc_id = [-1] * (2 * n + 2)
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
    
    # Check if for any variable x_i, both x_i=0 and x_i=1 are in the same SCC
    for i in range(1, n+1):
        node_0 = 2 * i       # x_i = 0
        node_1 = 2 * i + 1   # x_i = 1
        if scc_id[node_0] == scc_id[node_1]:
            print("NO")
            return
    
    # Assign values: if node for x_i=1 is in a later SCC than node for x_i=0, then x_i = 1
    result = [0] * (n + 1)
    for i in range(1, n+1):
        node_0 = 2 * i
        node_1 = 2 * i + 1
        if scc_id[node_1] > scc_id[node_0]:
            result[i] = 1
    
    print("YES")
    print(' '.join(map(str, result[1:])))

if __name__ == "__main__":
    main()