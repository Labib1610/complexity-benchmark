import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each rule (l1 OR l2), we create implications
    # If l1 is false, then l2 must be true
    # If l2 is false, then l1 must be true
    
    # Build implication graph
    # Node i represents variable i (1 to n)
    # Node -i represents NOT i
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        # l1 OR l2 is equivalent to (NOT l1 -> l2) AND (NOT l2 -> l1)
        # Add edges to implication graph
        graph[-l1].append(l2)
        graph[-l2].append(l1)
        reverse_graph[l2].append(-l1)
        reverse_graph[l1].append(-l2)
    
    # Kosaraju's algorithm for finding strongly connected components
    visited = set()
    order = []
    
    def dfs1(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs1(neighbor)
        order.append(node)
    
    # First DFS to determine finishing order
    all_nodes = set()
    for u in graph:
        all_nodes.add(u)
        for v in graph[u]:
            all_nodes.add(v)
    
    for node in all_nodes:
        if node not in visited:
            dfs1(node)
    
    # Second DFS on reverse graph in reverse order
    visited = set()
    scc = {}
    scc_id = 0
    
    def dfs2(node):
        if node in visited:
            return
        visited.add(node)
        scc[node] = scc_id
        for neighbor in reverse_graph[node]:
            dfs2(neighbor)
    
    while order:
        node = order.pop()
        if node not in visited:
            dfs2(node)
            scc_id += 1
    
    # Check if any variable and its negation are in the same SCC
    for i in range(1, n + 1):
        if i in scc and -i in scc and scc[i] == scc[-i]:
            print("NO")
            return
    
    # Assign values based on SCC topological order
    # Variables in later SCCs should be true
    assignment = [0] * (n + 1)  # 1-indexed
    
    # Create reverse SCC graph to determine topological order
    scc_graph = defaultdict(set)
    for u in graph:
        for v in graph[u]:
            if scc[u] != scc[v]:
                scc_graph[scc[u]].add(scc[v])
    
    # Topological sort of SCCs
    scc_in_degree = defaultdict(int)
    for u in scc_graph:
        for v in scc_graph[u]:
            scc_in_degree[v] += 1
    
    scc_nodes = set(scc.values())
    queue = deque()
    for scc_node in scc_nodes:
        if scc_in_degree[scc_node] == 0:
            queue.append(scc_node)
    
    scc_order = []
    while queue:
        current = queue.popleft()
        scc_order.append(current)
        for neighbor in scc_graph[current]:
            scc_in_degree[neighbor] -= 1
            if scc_in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Assign truth values: later SCCs in topological order are true
    scc_value = {}
    for i, scc_node in enumerate(scc_order):
        scc_value[scc_node] = 1 if i >= len(scc_order) // 2 else 0
    
    # Assign values to variables
    for i in range(1, n + 1):
        if i in scc:
            assignment[i] = scc_value[scc[i]]
        else:
            assignment[i] = 0  # Default value if not in any constraint
    
    print("YES")
    print(" ".join(str(assignment[i]) for i in range(1, n + 1)))

solve()