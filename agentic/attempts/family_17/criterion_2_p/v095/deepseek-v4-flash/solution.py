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
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    graph = [[] for _ in range(q + 1)]
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        graph[a].append(b - q)  # map right side to 1..q

    matching_size, pair_u = hopcroft_karp(graph, q, q)
    if matching_size != q:
        sys.stdout.write("NO\n")
    else:
        out = ["YES"]
        for u in range(1, q + 1):
            v = pair_u[u] + q
            out.append(f"{u} {v}")
        sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()