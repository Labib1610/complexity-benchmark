import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # Build implication graph for 2-SAT
    # Variables: 0 to n-1 represent sensors 1 to n in low-gain (0)
    # Variables: n to 2n-1 represent sensors 1 to n in high-gain (1)
    # So variable i represents sensor i+1 in low-gain
    # And variable i+n represents sensor i+1 in high-gain
    
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        
        # Convert to 0-indexed variables
        # If l1 > 0, it's sensor l1 in high-gain (variable l1-1+n)
        # If l1 < 0, it's sensor |l1| in low-gain (variable |l1|-1)
        if l1 > 0:
            var1 = l1 - 1 + n  # high-gain
            not_var1 = l1 - 1  # low-gain
        else:
            var1 = -l1 - 1     # low-gain
            not_var1 = -l1 - 1 + n  # high-gain
            
        if l2 > 0:
            var2 = l2 - 1 + n  # high-gain
            not_var2 = l2 - 1  # low-gain
        else:
            var2 = -l2 - 1     # low-gain
            not_var2 = -l2 - 1 + n  # high-gain
        
        # Add implications: NOT var1 -> var2 and NOT var2 -> var1
        adj[not_var1].append(var2)
        adj[not_var2].append(var1)
        rev_adj[var2].append(not_var1)
        rev_adj[var1].append(not_var2)
    
    # Kosaraju's algorithm for finding SCCs
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
    
    # Check if any variable and its negation are in the same SCC
    for i in range(n):
        if scc_id[i] == scc_id[i + n]:
            print("NO")
            return
    
    # Assign values based on topological order of SCCs
    assignment = [-1] * n
    
    # Create SCC graph
    scc_graph = defaultdict(set)
    for u in range(2 * n):
        for v in adj[u]:
            if scc_id[u] != scc_id[v]:
                scc_graph[scc_id[u]].add(scc_id[v])
    
    # Topological sort of SCCs
    in_degree = [0] * scc_count
    for u in range(scc_count):
        for v in scc_graph[u]:
            in_degree[v] += 1
    
    queue = deque()
    for i in range(scc_count):
        if in_degree[i] == 0:
            queue.append(i)
    
    topo_order = []
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in scc_graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    # Assign truth values
    for scc in reversed(topo_order):
        for node in range(2 * n):
            if scc_id[node] == scc:
                if node < n:  # Low-gain variable
                    sensor = node
                    if assignment[sensor] == -1:
                        assignment[sensor] = 0
                else:  # High-gain variable
                    sensor = node - n
                    if assignment[sensor] == -1:
                        assignment[sensor] = 1
    
    print("YES")
    print(" ".join(map(str, assignment)))

solve()