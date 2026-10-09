import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # For each rule (l1 OR l2), we create implications
    # If l1 is False, then l2 must be True
    # If l2 is False, then l1 must be True
    
    # We'll use 2-SAT
    # Variables: 0 to 2*n-1
    # For variable i (0-based), 
    #    node 2*i represents flag i+1 = 0 (OFF)
    #    node 2*i+1 represents flag i+1 = 1 (ON)
    
    adj = [[] for _ in range(2 * n)]
    adj_rev = [[] for _ in range(2 * n)]
    
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        # l1 is at index (abs(l1)-1)
        # l2 is at index (abs(l2)-1)
        
        # Convert to 0-based indexing
        idx1 = abs(l1) - 1
        idx2 = abs(l2) - 1
        
        # If l1 > 0, it means flag idx1 should be 1
        # If l1 < 0, it means flag idx1 should be 0
        # Same for l2
        
        # The rule is (l1 OR l2)
        # Which is equivalent to (NOT l1 -> l2) AND (NOT l2 -> l1)
        
        # NOT l1 -> l2
        # If l1 > 0, NOT l1 is flag idx1 = 0, which is node 2*idx1
        # If l1 < 0, NOT l1 is flag idx1 = 1, which is node 2*idx1+1
        # If l2 > 0, l2 is flag idx2 = 1, which is node 2*idx2+1
        # If l2 < 0, l2 is flag idx2 = 0, which is node 2*idx2
        
        not_l1_node = 2 * idx1 if l1 > 0 else 2 * idx1 + 1
        l2_node = 2 * idx2 + 1 if l2 > 0 else 2 * idx2
        
        not_l2_node = 2 * idx2 if l2 > 0 else 2 * idx2 + 1
        l1_node = 2 * idx1 + 1 if l1 > 0 else 2 * idx1
        
        adj[not_l1_node].append(l2_node)
        adj_rev[l2_node].append(not_l1_node)
        
        adj[not_l2_node].append(l1_node)
        adj_rev[l1_node].append(not_l2_node)
    
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
    
    # Second DFS on transpose graph
    visited = [False] * (2 * n)
    components = [-1] * (2 * n)
    comp_id = 0
    
    def dfs2(u):
        visited[u] = True
        components[u] = comp_id
        for v in adj_rev[u]:
            if not visited[v]:
                dfs2(v)
    
    for i in reversed(order):
        if not visited[i]:
            dfs2(i)
            comp_id += 1
    
    # Check if for every variable, x and NOT x are in different SCCs
    for i in range(n):
        if components[2*i] == components[2*i + 1]:
            print("NO")
            return
    
    # If satisfiable, reconstruct solution
    # In the implication graph, if SCC of x is after SCC of NOT x in topological order, 
    # then x should be True
    
    # We need the topological order of SCCs
    scc_graph = [[] for _ in range(comp_id)]
    in_degree = [0] * comp_id
    
    for u in range(2 * n):
        for v in adj[u]:
            if components[u] != components[v]:
                scc_graph[components[u]].append(components[v])
    
    # Remove duplicates
    for i in range(comp_id):
        scc_graph[i] = list(set(scc_graph[i]))
        
    for i in range(comp_id):
        for j in scc_graph[i]:
            in_degree[j] += 1
    
    # Topological sort of SCCs
    from collections import deque
    queue = deque()
    for i in range(comp_id):
        if in_degree[i] == 0:
            queue.append(i)
    
    scc_order = []
    while queue:
        u = queue.popleft()
        scc_order.append(u)
        for v in scc_graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    scc_pos = [0] * comp_id
    for i in range(comp_id):
        scc_pos[scc_order[i]] = i
    
    # Assign values
    assignment = [0] * n
    for i in range(n):
        if scc_pos[components[2*i]] > scc_pos[components[2*i + 1]]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    print("YES")
    print(' '.join(map(str, assignment)))

threading.Thread(target=main).start()