def solve():
    k, e = map(int, input().split())
    allowed = []
    for _ in range(e):
        x, y = map(int, input().split())
        allowed.append((x, y))
    
    adj = [[] for _ in range(k + 1)]
    for x, y in allowed:
        adj[x].append(y)
    
    match = [0] * (k + 1)
    visited = [False] * (k + 1)
    
    def dfs(worker):
        for task in adj[worker]:
            if not visited[task]:
                visited[task] = True
                if match[task] == 0 or dfs(match[task]):
                    match[task] = worker
                    return True
        return False
    
    count = 0
    for i in range(1, k + 1):
        visited = [False] * (k + 1)
        if dfs(i):
            count += 1
    
    if count == k:
        assignment = [0] * k
        for i in range(1, k + 1):
            assignment[i-1] = match[i]
        print("YES")
        print(*assignment)
    else:
        print("NO")

solve()