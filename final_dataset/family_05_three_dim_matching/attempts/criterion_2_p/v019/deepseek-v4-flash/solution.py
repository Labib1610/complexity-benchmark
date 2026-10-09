import sys
from collections import deque

def hopcroft_karp(graph, n_left, n_right):
    INF = 10**9
    pair_u = [-1] * (n_left + 1)
    pair_v = [-1] * (n_right + 1)
    dist = [0] * (n_left + 1)

    def bfs():
        q = deque()
        for u in range(1, n_left + 1):
            if pair_u[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        found = False
        while q:
            u = q.popleft()
            for v in graph[u]:
                pu = pair_v[v]
                if pu != -1 and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
                elif pu == -1:
                    found = True
        return found

    def dfs(u):
        for v in graph[u]:
            pu = pair_v[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(1, n_left + 1):
            if pair_u[u] == -1 and dfs(u):
                matching += 1
    return matching, pair_u

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    # pilot -> mission adjacency
    graph = [[] for _ in range(k + 1)]
    # store original triples for output
    triples = {}
    for _ in range(t):
        p = int(next(it))
        s = int(next(it))
        m = int(next(it))
        graph[p].append(m)
        triples[(p, m)] = (p, s, m)

    matching_size, pair_u = hopcroft_karp(graph, k, k)

    if matching_size != k:
        print("NO")
        return

    print("YES")
    for p in range(1, k + 1):
        m = pair_u[p]
        print(*triples[(p, m)])

if __name__ == "__main__":
    main()