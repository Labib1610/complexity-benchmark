import sys
from collections import deque

input = sys.stdin.readline

def hopcroft_karp(q, adj):
    # adj: list of lists, size q+1, indexed 1..q
    pair_u = [0] * (q + 1)
    pair_v = [0] * (2 * q + 1)
    dist = [0] * (q + 1)

    INF = 10**9

    def bfs():
        dq = deque()
        for u in range(1, q + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while dq:
            u = dq.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        dq.append(pair_v[v])
        return dist[0] != INF

    def dfs(u):
        if u != 0:
            for v in adj[u]:
                if dist[pair_v[v]] == dist[u] + 1 and dfs(pair_v[v]):
                    pair_v[v] = u
                    pair_u[u] = v
                    return True
            dist[u] = INF
            return False
        return True

    matching = 0
    while bfs():
        for u in range(1, q + 1):
            if pair_u[u] == 0 and dfs(u):
                matching += 1
    return matching, pair_u

def main():
    q, t = map(int, input().split())
    adj = [[] for _ in range(q + 1)]
    for _ in range(t):
        a, b = map(int, input().split())
        adj[a].append(b)

    matching, pair_u = hopcroft_karp(q, adj)

    if matching == q:
        print("YES")
        for u in range(1, q + 1):
            print(u, pair_u[u])
    else:
        print("NO")

if __name__ == "__main__":
    main()