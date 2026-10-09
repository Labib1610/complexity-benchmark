import sys
from collections import defaultdict

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    try:
        N1 = int(next(it))
        N2 = int(next(it))
        M = int(next(it))
    except StopIteration:
        return
    
    tasks = []
    deg_u = defaultdict(int)
    deg_v = defaultdict(int)
    
    for _ in range(M):
        u = int(next(it))
        v = int(next(it))
        tasks.append((u, v))
        deg_u[u] += 1
        deg_v[v] += 1
    
    if M == 0:
        print("YES")
        print()
        return
    
    K = 0
    if deg_u:
        K = max(K, max(deg_u.values()))
    if deg_v:
        K = max(K, max(deg_v.values()))
    
    if K == 0:
        print("YES")
        print()
        return
    
    adj_u = defaultdict(list)
    adj_v = defaultdict(list)
    for i, (u, v) in enumerate(tasks):
        adj_u[u].append(i)
        adj_v[v].append(i)
    
    match_u = {}
    match_v = {}
    
    def dfs(u, visited):
        for task_idx in adj_u[u]:
            if visited[task_idx]:
                continue
            visited[task_idx] = True
            v = tasks[task_idx][1]
            if v not in match_v or dfs(match_v[v], visited):
                match_u[u] = task_idx
                match_v[v] = task_idx
                return True
        return False
    
    for u in deg_u:
        dfs(u, [False] * M)
    
    color = [0] * M
    
    def dfs_color(u, c):
        task_idx = match_u[u]
        color[task_idx] = c
        v = tasks[task_idx][1]
        for t2 in adj_v[v]:
            if color[t2] == 0:
                u2 = tasks[t2][0]
                dfs_color(u2, c)
    
    for u in match_u:
        if match_u[u] in match_u:
            if color[match_u[u]] == 0:
                dfs_color(u, 1)
    
    for i in range(M):
        if color[i] == 0:
            color[i] = 1
    
    print("YES")
    print(' '.join(map(str, color)))

if __name__ == "__main__":
    solve()