import sys
from collections import deque

input = sys.stdin.readline

def hopcroft_karp(n, m, adj):
    # n = number of left nodes (ground arrays)
    # m = number of right nodes (orbital relays)
    INF = 10**9
    pairU = [-1] * (n + 1)
    pairV = [-1] * (m + 1)
    dist = [0] * (n + 1)

    def bfs():
        dq = deque()
        for u in range(1, n + 1):
            if pairU[u] == -1:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        found = False
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                pu = pairV[v]
                if pu != -1 and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    dq.append(pu)
                elif pu == -1:
                    found = True
        return found

    def dfs(u):
        for v in adj[u]:
            pu = pairV[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(1, n + 1):
            if pairU[u] == -1 and dfs(u):
                matching += 1
    return matching, pairU

def main():
    q, t = map(int, input().split())
    adj = [[] for _ in range(q + 1)]
    for _ in range(t):
        a, b = map(int, input().split())
        adj[a].append(b - q)  # store right node as 1..q

    matching, pairU = hopcroft_karp(q, q, adj)
    if matching != q:
        print("NO")
    else:
        print("YES")
        for u in range(1, q + 1):
            v = pairU[u] + q
            print(u, v)

if __name__ == "__main__":
    main()