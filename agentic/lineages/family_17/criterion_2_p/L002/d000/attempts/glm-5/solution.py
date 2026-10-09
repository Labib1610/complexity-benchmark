import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    
    adj = [[] for _ in range(q + 1)]
    edges = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        edges.append((a, b))
    
    match_r = [0] * (2 * q + 1)
    match_l = [0] * (q + 1)
    
    def bfs():
        dist = [-1] * (q + 1)
        dq = deque()
        for u in range(1, q + 1):
            if match_l[u] == 0:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = -1
        found = False
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                m = match_r[v]
                if m != 0 and dist[m] == -1:
                    dist[m] = dist[u] + 1
                    dq.append(m)
                elif m == 0:
                    found = True
        return dist, found
    
    def dfs(u, dist):
        for v in adj[u]:
            m = match_r[v]
            if m == 0:
                match_l[u] = v
                match_r[v] = u
                return True
            elif dist[m] == dist[u] + 1:
                if dfs(m, dist):
                    match_l[u] = v
                    match_r[v] = u
                    return True
        dist[u] = -1
        return False
    
    while True:
        dist, found = bfs()
        if not found:
            break
        for u in range(1, q + 1):
            if match_l[u] == 0:
                dfs(u, dist)
    
    count = sum(1 for u in range(1, q + 1) if match_l[u] != 0)
    if count != q:
        print("NO")
    else:
        print("YES")
        for u in range(1, q + 1):
            print(u, match_l[u])

if __name__ == "__main__":
    solve()