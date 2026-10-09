import sys
from collections import deque

input = sys.stdin.readline

def hopcroft_karp(n, m, adj):
    INF = float('inf')
    pair_u = [-1] * n
    pair_v = [-1] * m
    dist = [0] * n

    def bfs():
        q = deque()
        for u in range(n):
            if pair_u[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        found = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                pu = pair_v[v]
                if pu == -1:
                    found = True
                elif dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
        return found

    def dfs(u):
        for v in adj[u]:
            pu = pair_v[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(n):
            if pair_u[u] == -1 and dfs(u):
                matching += 1
    return pair_u, matching

def main():
    q, t = map(int, input().split())
    adj = [[] for _ in range(q)]
    for _ in range(t):
        a, b = map(int, input().split())
        adj[a - 1].append(b - q - 1)  # convert to zero-based

    pair_u, matching = hopcroft_karp(q, q, adj)

    if matching != q:
        print("NO")
    else:
        print("YES")
        for i in range(q):
            print(i + 1, pair_u[i] + q + 1)

if __name__ == "__main__":
    main()