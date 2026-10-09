import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    k = int(input_data[0])
    t = int(input_data[1])
    
    c_of_d = [0] * (k + 1)
    adj = [[] for _ in range(k + 1)]
    
    idx = 2
    for _ in range(t):
        d = int(input_data[idx])
        c = int(input_data[idx+1])
        f = int(input_data[idx+2])
        idx += 3
        c_of_d[d] = c
        adj[d].append(f)
        
    pair_u = [0] * (k + 1)
    pair_v = [0] * (k + 1)
    dist = [0] * (k + 1)
    
    INF = 10**9
    
    from collections import deque
    
    def bfs():
        q = deque()
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        
        while q:
            u = q.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        q.append(pair_v[v])
        return dist[0] != INF

    def dfs(u):
        if u != 0:
            for v in adj[u]:
                if dist[pair_v[v]] == dist[u] + 1:
                    if dfs(pair_v[v]):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = INF
            return False
        return True

    matching = 0
    sys.setrecursionlimit(max(2000, k + 50))
    
    while bfs():
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1
                    
    if matching == k:
        out = ["YES"]
        for u in range(1, k + 1):
            out.append(f"{u} {c_of_d[u]} {pair_u[u]}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == '__main__':
    solve()