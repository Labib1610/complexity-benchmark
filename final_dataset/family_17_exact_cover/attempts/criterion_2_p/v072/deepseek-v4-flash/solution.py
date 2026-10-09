import sys
from collections import deque

input = sys.stdin.readline

def hopcroft_karp(q, adj):
    INF = float('inf')
    pair_u = [-1] * (q + 1)
    pair_v = [-1] * (q + 1)
    dist = [0] * (q + 1)

    def bfs():
        q_ = deque()
        for u in range(1, q + 1):
            if pair_u[u] == -1:
                dist[u] = 0
                q_.append(u)
            else:
                dist[u] = INF
        found = False
        while q_:
            u = q_.popleft()
            for v in adj[u]:
                pu = pair_v[v]
                if pu != -1 and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    q_.append(pu)
                elif pu == -1:
                    found = True
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
        for u in range(1, q + 1):
            if pair_u[u] == -1 and dfs(u):
                matching += 1
    return matching, pair_u

def main():
    q, t = map(int, input().split())
    adj = [[] for _ in range(q + 1)]
    for _ in range(t):
        a, b = map(int, input().split())
        adj[a].append(b)

    matching, pair_u = hopcroft_karp(q, adj)
    if matching != q:
        print("NO")
    else:
        print("YES")
        for u in range(1, q + 1):
            print(u, pair_u[u])

if __name__ == "__main__":
    main()