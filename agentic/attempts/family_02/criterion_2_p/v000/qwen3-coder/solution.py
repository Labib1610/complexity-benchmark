import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build implication graph
    # Each variable x_i has two nodes: 2*i (x_i = 0) and 2*i+1 (x_i = 1)
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        
        # Convert to 0-indexed variables
        if a > 0:
            var_a = a - 1
            val_a = 1
        else:
            var_a = -a - 1
            val_a = 0
            
        if b > 0:
            var_b = b - 1
            val_b = 1
        else:
            var_b = -b - 1
            val_b = 0
        
        # Add implications: NOT(a) -> b and NOT(b) -> a
        # NOT(var_a=val_a) means var_a=(1-val_a)
        node_not_a = 2 * var_a + (1 - val_a)
        node_b = 2 * var_b + val_b
        graph[node_not_a].append(node_b)
        reverse_graph[node_b].append(node_not_a)
        
        node_not_b = 2 * var_b + (1 - val_b)
        node_a = 2 * var_a + val_a
        graph[node_not_b].append(node_a)
        reverse_graph[node_a].append(node_not_b)
    
    # Kosaraju's algorithm for SCC
    def dfs1(node, visited, stack):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs1(neighbor, visited, stack)
        stack.append(node)
    
    def dfs2(node, visited, component):
        visited.add(node)
        component.append(node)
        for neighbor in reverse_graph[node]:
            if neighbor not in visited:
                dfs2(neighbor, visited, component)
    
    # First DFS pass
    visited = set()
    stack = []
    for i in range(2 * n):
        if i not in visited:
            dfs1(i, visited, stack)
    
    # Second DFS pass on transpose graph
    visited = set()
    scc = {}
    scc_id = 0
    
    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            dfs2(node, visited, component)
            for v in component:
                scc[v] = scc_id
            scc_id += 1
    
    # Check if satisfiable
    for i in range(n):
        if scc[2 * i] == scc[2 * i + 1]:
            print("NO")
            return
    
    # Assign values
    assignment = [-1] * n
    # Process SCCs in reverse topological order
    scc_order = []
    scc_nodes = defaultdict(list)
    
    for node in range(2 * n):
        scc_nodes[scc[node]].append(node)
    
    # Create SCC graph
    scc_graph = defaultdict(set)
    for node in range(2 * n):
        for neighbor in graph[node]:
            if scc[node] != scc[neighbor]:
                scc_graph[scc[node]].add(scc[neighbor])
    
    # Topological sort of SCCs
    in_degree = defaultdict(int)
    all_scc = set()
    for i in range(scc_id):
        all_scc.add(i)
    
    for u in scc_graph:
        for v in scc_graph[u]:
            in_degree[v] += 1
    
    queue = deque()
    for scc_node in all_scc:
        if in_degree[scc_node] == 0:
            queue.append(scc_node)
    
    while queue:
        current = queue.popleft()
        scc_order.append(current)
        for neighbor in scc_graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Assign truth values
    assigned = [False] * n
    for scc_idx in reversed(scc_order):
        for node in scc_nodes[scc_idx]:
            var = node // 2
            val = node % 2
            if not assigned[var]:
                assignment[var] = val
                assigned[var] = True
    
    print("YES")
    print(' '.join(map(str, assignment)))

solve()