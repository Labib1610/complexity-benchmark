import sys
from collections import deque

def hopcroft_karp(n, m, adj):
    # n: number of left nodes (transmitters) 1..n
    # m: number of right nodes (receivers) 1..m, but we'll use 0..m-1 internally
    # adj[u] = list of v (0-indexed right nodes)
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
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))

    adj = [[] for _ in range(q + 1)]
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        # b is in [q+1, 2q], convert to 0-indexed right node: b - (q+1)
        adj[a].append(b - (q + 1))

    # Run Hopcroft-Karp
    matching_size, pairU = hopcroft_karp(q, q, adj)

    if matching_size != q:
        print("NO")
        return

    print("YES")
    # pairU[u] gives the matched receiver index (0-based) for transmitter u
    for u in range(1, q + 1):
        b = pairU[u] + q + 1
        print(u, b)

if __name__ == "__main__":
    main()