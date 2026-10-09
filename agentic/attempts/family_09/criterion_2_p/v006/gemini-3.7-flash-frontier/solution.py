import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    sys.setrecursionlimit(300000)
    
    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])
    
    adj = [[] for _ in range(n + 1)]
    idx = 3
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    color = [-1] * (n + 1)
    L = []
    R = []
    
    for i in range(1, n + 1):
        if color[i] == -1:
            color[i] = 0
            stack = [i]
            while stack:
                u = stack.pop()
                if color[u] == 0:
                    L.append(u)
                else:
                    R.append(u)
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        stack.append(v)

    pair_u = [0] * (n + 1)
    pair_v = [0] * (n + 1)
    dist = [0] * (n + 1)
    INF = float('inf')

    def bfs():
        from collections import deque
        queue = deque()
        for u in L:
            if pair_u[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while queue:
            u = queue.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    pv = pair_v[v]
                    if dist[pv] == INF:
                        dist[pv] = dist[u] + 1
                        queue.append(pv)
        return dist[0] != INF

    def dfs(u):
        if u != 0:
            for v in adj[u]:
                pv = pair_v[v]
                if dist[pv] == dist[u] + 1:
                    if dfs(pv):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = INF
            return False
        return True

    while bfs():
        for u in L:
            if pair_u[u] == 0:
                dfs(u)

    from collections import deque
    visited = [False] * (n + 1)
    q = deque()
    for u in L:
        if pair_u[u] == 0:
            visited[u] = True
            q.append(u)

    while q:
        curr = q.popleft()
        if color[curr] == 0:
            for v in adj[curr]:
                if v != pair_u[curr] and not visited[v]:
                    visited[v] = True
                    q.append(v)
        else:
            pv = pair_v[curr]
            if pv != 0 and not visited[pv]:
                visited[pv] = True
                q.append(pv)

    mis = []
    for u in L:
        if visited[u]:
            mis.append(u)
    for v in R:
        if not visited[v]:
            mis.append(v)

    if len(mis) >= k:
        print("YES")
        print(*(mis[:k]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()