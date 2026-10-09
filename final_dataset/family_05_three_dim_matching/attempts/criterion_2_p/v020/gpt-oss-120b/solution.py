import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    adj = [[] for _ in range(k + 1)]
    tag_of = [0] * (k + 1)          # tag_of[u] = v
    for _ in range(t):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        if tag_of[u] == 0:
            tag_of[u] = v
        # according to statement, all entries for same u have same v
        adj[u].append(w)

    # quick check: every container must have at least one possible vessel
    for u in range(1, k + 1):
        if not adj[u]:
            print("NO")
            return

    # Hopcroft–Karp
    INF = k + 5
    pair_u = [0] * (k + 1)   # matched vessel for container u
    pair_v = [0] * (k + 1)   # matched container for vessel w
    dist = [0] * (k + 1)

    def bfs() -> bool:
        q = deque()
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while q:
            u = q.popleft()
            if dist[u] < dist[0]:
                for w in adj[u]:
                    if pair_v[w] == 0:
                        if dist[0] == INF:
                            dist[0] = dist[u] + 1
                    elif dist[pair_v[w]] == INF:
                        dist[pair_v[w]] = dist[u] + 1
                        q.append(pair_v[w])
        return dist[0] != INF

    def dfs(u: int) -> bool:
        if u == 0:
            return True
        for w in adj[u]:
            pu = pair_v[w]
            if pu == 0 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pair_u[u] = w
                pair_v[w] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pair_u[u] == 0 and dfs(u):
                matching += 1

    if matching != k:
        print("NO")
        return

    print("YES")
    out_lines = []
    for u in range(1, k + 1):
        out_lines.append(f"{u} {tag_of[u]} {pair_u[u]}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()