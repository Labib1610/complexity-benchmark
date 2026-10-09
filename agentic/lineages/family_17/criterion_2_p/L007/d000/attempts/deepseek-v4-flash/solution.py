import sys
from collections import deque

def hopcroft_karp(n, m, adj):
    INF = 10**9
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
        for u in range(n):
            if pair_u[u] == -1 and dfs(u):
                matching += 1
    return matching, pair_u

def main():
    input_data = sys.stdin.buffer.read().split()
    q = int(input_data[0])
    t = int(input_data[1])
    adj = [[] for _ in range(q)]
    idx = 2
    for _ in range(t):
        a = int(input_data[idx]) - 1
        b = int(input_data[idx + 1]) - q - 1
        idx += 2
        adj[a].append(b)

    matching, pair_u = hopcroft_karp(q, q, adj)
    if matching != q:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
        out = []
        for u in range(q):
            out.append(f"{u+1} {pair_u[u]+q+1}")
        sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()