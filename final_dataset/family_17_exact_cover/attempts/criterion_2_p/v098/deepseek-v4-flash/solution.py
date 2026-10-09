import sys
from collections import deque

def hopcroft_karp(n, adj, pair_u, pair_v, dist):
    INF = float('inf')
    q = deque()
    for u in range(1, n+1):
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

def dfs(u, adj, pair_u, pair_v, dist):
    if u != 0:
        for v in adj[u]:
            if dist[pair_v[v]] == dist[u] + 1:
                if dfs(pair_v[v], adj, pair_u, pair_v, dist):
                    pair_v[v] = u
                    pair_u[u] = v
                    return True
        dist[u] = float('inf')
        return False
    return True

def main():
    input = sys.stdin.readline
    q, t = map(int, input().split())
    adj = [[] for _ in range(q+1)]
    for _ in range(t):
        a, b = map(int, input().split())
        adj[a].append(b - q)  # store platform index as 1..q

    pair_u = [0] * (q+1)
    pair_v = [0] * (q+1)
    dist = [0] * (q+1)

    matching = 0
    while hopcroft_karp(q, adj, pair_u, pair_v, dist):
        for u in range(1, q+1):
            if pair_u[u] == 0:
                if dfs(u, adj, pair_u, pair_v, dist):
                    matching += 1

    if matching != q:
        print("NO")
    else:
        print("YES")
        for u in range(1, q+1):
            print(u, pair_u[u] + q)

if __name__ == "__main__":
    main()