import sys
from collections import deque

def hopcroft_karp(n, m, adj):
    INF = 10**9
    pair_u = [-1] * (n + 1)
    pair_v = [-1] * (m + 1)
    dist = [0] * (n + 1)

    def bfs():
        q = deque()
        for u in range(1, n + 1):
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
                if pu != -1 and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
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
        for u in range(1, n + 1):
            if pair_u[u] == -1 and dfs(u):
                matching += 1
    return matching, pair_u

def main():
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    t = int(data[1])
    adj = [[] for _ in range(q + 1)]
    idx = 2
    for _ in range(t):
        a = int(data[idx])
        b = int(data[idx + 1])
        idx += 2
        adj[a].append(b - q)  # shift habitation module ids to 1..q

    matching_count, pair_u = hopcroft_karp(q, q, adj)
    if matching_count != q:
        print("NO")
        return

    print("YES")
    out = []
    for u in range(1, q + 1):
        v = pair_u[u]
        out.append(f"{u} {v + q}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()