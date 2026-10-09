import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    k = next(it)
    t = next(it)

    adj = [[] for _ in range(k)]          # pilot -> list of windows (0‑based)
    aircraft = [0] * k
    have_aircraft = [False] * k

    for _ in range(t):
        p = next(it) - 1
        a = next(it)
        w = next(it) - 1
        if not have_aircraft[p]:
            aircraft[p] = a
            have_aircraft[p] = True
        adj[p].append(w)

    # quick impossibility test
    for p in range(k):
        if not adj[p]:
            print("NO")
            return

    # ---------- Hopcroft‑Karp ----------
    INF = 10 ** 9
    pairU = [-1] * k          # pilot -> window
    pairV = [-1] * k          # window -> pilot
    dist = [0] * k

    def bfs() -> bool:
        q = deque()
        for u in range(k):
            if pairU[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        found = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                pu = pairV[v]
                if pu != -1 and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
                elif pu == -1:
                    found = True
        return found

    sys.setrecursionlimit(10000)

    def dfs(u: int) -> bool:
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
        for u in range(k):
            if pairU[u] == -1 and dfs(u):
                matching += 1

    # ---------- output ----------
    if matching == k:
        out_lines = ["YES"]
        for p in range(k):
            out_lines.append(f"{p+1} {aircraft[p]} {pairU[p]+1}")
        sys.stdout.write("\n".join(out_lines))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()