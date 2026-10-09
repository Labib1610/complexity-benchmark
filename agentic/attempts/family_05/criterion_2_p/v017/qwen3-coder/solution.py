from collections import defaultdict

def solve():
    k, t = map(int, input().split())
    
    # Group configurations by operator
    configs = []
    operator_configs = defaultdict(list)
    terminal_to_operator = {}
    
    for _ in range(t):
        x, y, z = map(int, input().split())
        configs.append((x, y, z))
        operator_configs[x].append((x, y, z))
        terminal_to_operator[y] = x
    
    # Build bipartite graph: operators on left, windows on right
    # Edge exists if there's a configuration with that operator and window
    from collections import deque
    
    # For each operator, we need to match it to a window
    # This is a maximum bipartite matching problem
    
    # Build adjacency list for operators -> possible windows
    adj = defaultdict(list)
    for config in configs:
        x, y, z = config
        adj[x].append(z)
    
    # Maximum bipartite matching using Hungarian algorithm / DFS
    def dfs(u, match_right, match_left, visited):
        for v in adj[u]:
            if visited[v]:
                continue
            visited[v] = True
            
            if match_right[v] == -1 or dfs(match_right[v], match_right, match_left, visited):
                match_right[v] = u
                match_left[u] = v
                return True
        return False
    
    # Initialize matching arrays
    match_right = [-1] * (k + 1)  # window -> operator
    match_left = [-1] * (k + 1)   # operator -> window
    
    matched = 0
    for operator in range(1, k + 1):
        if operator in adj:  # If operator has any possible configurations
            visited = [False] * (k + 1)
            if dfs(operator, match_right, match_left, visited):
                matched += 1
    
    if matched != k:
        print("NO")
        return
    
    print("YES")
    # Reconstruct the solution
    result = []
    for window in range(1, k + 1):
        if match_right[window] != -1:
            operator = match_right[window]
            # Find the terminal for this operator
            terminal = operator_configs[operator][0][1]  # All configs for this operator have same terminal
            result.append((operator, terminal, window))
    
    for item in result:
        print(item[0], item[1], item[2])

solve()