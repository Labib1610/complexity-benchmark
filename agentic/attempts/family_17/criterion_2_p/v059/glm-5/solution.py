import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0])
    t = int(data[1])
    edges = []
    idx = 2
    for _ in range(t):
        a = int(data[idx]); b = int(data[idx+1])
        idx += 2
        edges.append((a, b))

    # Hopcroft-Karp for bipartite matching
    # Left side: old units 1..q
    # Right side: new units q+1..2q, remapped to 1..q
    adj = [[] for _ in range(q+1)]
    for a, b in edges:
        adj[a].append(b - q)

    pair_u = [0] * (q + 1)
    pair_v = [0] * (q + 1)
    dist = [0] * (q + 1)
    INF = 10**9

    from collections import deque

    def bfs():
        dq = deque()
        found = False
        for u in range(1, q+1):
            if pair_u[u] == 0:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                pu = pair_v[v]
                if pu == 0:
                    found = True
                elif dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    dq.append(pu)
        return found

    def dfs(u):
        for v in adj[u]:
            pu = pair_v[v]
            if pu == 0 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(1, q+1):
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1

    if matching == q:
        out = ["YES"]
        for u in range(1, q+1):
            out.append(f"{u} {pair_u[u] + q}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == "__main__":
    main()