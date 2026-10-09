import sys
import collections

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))

    G = [[] for _ in range(q + 1)]          # 1‑based left side
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        G[a].append(b)                     # b is in [q+1, 2q]

    # Hopcroft‑Karp
    NIL = 0
    pairU = [NIL] * (q + 1)                 # left -> right
    pairV = [NIL] * (2 * q + 1)              # right -> left
    dist = [0] * (q + 1)

    def bfs() -> bool:
        dq = collections.deque()
        for u in range(1, q + 1):
            if pairU[u] == NIL:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = -1
        found = False
        while dq:
            u = dq.popleft()
            for v in G[u]:
                pu = pairV[v]
                if pu == NIL:
                    found = True
                elif dist[pu] == -1:
                    dist[pu] = dist[u] + 1
                    dq.append(pu)
        return found

    sys.setrecursionlimit(1 << 25)
    def dfs(u: int) -> bool:
        for v in G[u]:
            pu = pairV[v]
            if pu == NIL or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = -1
        return False

    matching = 0
    while bfs():
        for u in range(1, q + 1):
            if pairU[u] == NIL and dfs(u):
                matching += 1

    out = []
    if matching == q:
        out.append(b"YES")
        for a in range(1, q + 1):
            out.append(f"{a} {pairU[a]}".encode())
    else:
        out.append(b"NO")
    sys.stdout.buffer.write(b"\n".join(out))

if __name__ == "__main__":
    solve()