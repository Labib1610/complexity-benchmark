import sys
from collections import deque

def hopcroft_karp(n, m, adj):
    # adj: list of lists for left side (size n), each entry is right node index (0-based)
    INF = 10**9
    pairU = [-1] * n
    pairV = [-1] * m
    dist = [0] * n

    def bfs():
        dq = deque()
        for u in range(n):
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
                if pu == -1:
                    found = True
                elif dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    dq.append(pu)
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
        for u in range(n):
            if pairU[u] == -1 and dfs(u):
                matching += 1
    return matching, pairU

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    adj = [[] for _ in range(q)]
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1  # 0-based for right side
        if (a + 1) + (b + 1) <= 3 * q:
            adj[a].append(b)
    # Remove duplicates
    for i in range(q):
        adj[i] = list(set(adj[i]))
    matching, pairU = hopcroft_karp(q, q, adj)
    if matching != q:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
        for u in range(q):
            v = pairU[u]
            sys.stdout.write(f"{u+1} {v+1}\n")

if __name__ == "__main__":
    main()