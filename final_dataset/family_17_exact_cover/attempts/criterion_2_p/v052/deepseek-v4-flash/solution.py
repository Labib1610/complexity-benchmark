import sys
from collections import deque

def hopcroft_karp(adj, n_left, n_right):
    INF = 10**9
    pair_u = [-1] * (n_left)
    pair_v = [-1] * (n_right)
    dist = [0] * (n_left)

    def bfs():
        dq = deque()
        for u in range(n_left):
            if pair_u[u] == -1:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        found = False
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                pu = pair_v[v]
                if pu == -1:
                    found = True
                elif dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    dq.append(pu)
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
        for u in range(n_left):
            if pair_u[u] == -1 and dfs(u):
                matching += 1
    return matching, pair_u

def main():
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    t = int(data[1])
    adj = [[] for _ in range(q)]
    idx = 2
    for _ in range(t):
        a = int(data[idx]) - 1  # left node 0-based
        b = int(data[idx+1]) - q - 1  # right node 0-based
        adj[a].append(b)
        idx += 2

    n_left = q
    n_right = q
    matching_size, pair_u = hopcroft_karp(adj, n_left, n_right)

    if matching_size != q:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
        out_lines = []
        for u in range(q):
            v = pair_u[u] + q + 1
            out_lines.append(f"{u+1} {v}")
        sys.stdout.write("\n".join(out_lines) + "\n")

if __name__ == "__main__":
    main()