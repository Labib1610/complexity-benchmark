import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    
    adj = [[] for _ in range(q + 1)]
    edges = []
    for i in range(t):
        a = int(next(it))
        b = int(next(it))
        adj[a].append((b, i))
        edges.append((a, b))
    
    match_c = [0] * (q + 1)
    match_p = [0] * (2 * q + 1)
    dist = [0] * (q + 1)
    
    def bfs():
        dq = deque()
        for u in range(1, q + 1):
            if match_c[u] == 0:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = -1
        found = False
        while dq:
            u = dq.popleft()
            for v, _ in adj[u]:
                pu = match_p[v]
                if pu != 0 and dist[pu] == -1:
                    dist[pu] = dist[u] + 1
                    dq.append(pu)
                elif pu == 0:
                    found = True
        return found
    
    def dfs(u):
        for v, idx in adj[u]:
            pu = match_p[v]
            if pu == 0 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                match_c[u] = v
                match_p[v] = u
                return True
        dist[u] = -1
        return False
    
    matching = 0
    while bfs():
        for u in range(1, q + 1):
            if match_c[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching != q:
        print("NO")
    else:
        print("YES")
        for u in range(1, q + 1):
            print(u, match_c[u])

if __name__ == "__main__":
    solve()