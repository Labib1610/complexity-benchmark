import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    adj = [[] for _ in range(k + 1)]          # 1‑based
    machine = [0] * (k + 1)                   # machine[x]

    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        machine[x] = y                         # all same for given x
        adj[x].append(z)

    # ---------- Hopcroft‑Karp ----------
    INF = 10 ** 9
    matchL = [0] * (k + 1)    # specialist -> time slot
    matchR = [0] * (k + 1)    # time slot -> specialist
    dist = [0] * (k + 1)

    def bfs() -> bool:
        q = deque()
        for x in range(1, k + 1):
            if matchL[x] == 0:
                dist[x] = 0
                q.append(x)
            else:
                dist[x] = INF
        reachable_free = False
        while q:
            x = q.popleft()
            for z in adj[x]:
                y = matchR[z]
                if y == 0:
                    reachable_free = True
                elif dist[y] == INF:
                    dist[y] = dist[x] + 1
                    q.append(y)
        return reachable_free

    sys.setrecursionlimit(10000)
    def dfs(x: int) -> bool:
        for z in adj[x]:
            y = matchR[z]
            if y == 0 or (dist[y] == dist[x] + 1 and dfs(y)):
                matchL[x] = z
                matchR[z] = x
                return True
        dist[x] = INF
        return False

    matching = 0
    while bfs():
        for x in range(1, k + 1):
            if matchL[x] == 0 and dfs(x):
                matching += 1

    # ---------- Output ----------
    out = []
    if matching == k:
        out.append(b"YES")
        for x in range(1, k + 1):
            out.append(f"{x} {machine[x]} {matchL[x]}".encode())
    else:
        out.append(b"NO")
    sys.stdout.buffer.write(b"\n".join(out))

if __name__ == "__main__":
    solve()