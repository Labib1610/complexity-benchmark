import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    adj = [[] for _ in range(k + 1)]          # edges from specialist x to window z
    spec_to_mach = [0] * (k + 1)              # y for each x
    for _ in range(t):
        x = int(next(it)); y = int(next(it)); z = int(next(it))
        if spec_to_mach[x] == 0:
            spec_to_mach[x] = y
        # else y is same by problem guarantee
        adj[x].append(z)

    # quick check: every specialist must have at least one possible window
    for x in range(1, k + 1):
        if not adj[x]:
            print("NO")
            return

    # Hopcroft–Karp
    NIL = 0
    pairU = [NIL] * (k + 1)   # match for x
    pairV = [NIL] * (k + 1)   # match for z
    dist = [0] * (k + 1)

    def bfs() -> bool:
        q = deque()
        for u in range(1, k + 1):
            if pairU[u] == NIL:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = -1
        found = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                pu = pairV[v]
                if pu == NIL:
                    found = True
                elif dist[pu] == -1:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
        return found

    def dfs(u: int) -> bool:
        for v in adj[u]:
            pu = pairV[v]
            if pu == NIL or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = -1
        return False

    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pairU[u] == NIL and dfs(u):
                matching += 1

    if matching != k:
        print("NO")
        return

    print("YES")
    out_lines = []
    for x in range(1, k + 1):
        y = spec_to_mach[x]
        z = pairU[x]
        out_lines.append(f"{x} {y} {z}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()