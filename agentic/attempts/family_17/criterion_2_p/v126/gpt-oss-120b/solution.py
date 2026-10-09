import sys
import collections

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))

    adj = [[] for _ in range(q + 1)]          # 1‑based left side
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)                     # b is in [q+1, 2q]

    # Hopcroft‑Karp
    NIL = 0
    pairU = [NIL] * (q + 1)                  # left -> right
    pairV = {}                               # right -> left, use dict for sparse
    dist = [0] * (q + 1)

    def bfs() -> bool:
        qd = collections.deque()
        for u in range(1, q + 1):
            if pairU[u] == NIL:
                dist[u] = 0
                qd.append(u)
            else:
                dist[u] = -1
        found = False
        while qd:
            u = qd.popleft()
            for v in adj[u]:
                pu = pairV.get(v, NIL)
                if pu == NIL:
                    found = True               # we can reach a free right vertex
                elif dist[pu] == -1:
                    dist[pu] = dist[u] + 1
                    qd.append(pu)
        return found

    sys.setrecursionlimit(1 << 25)

    def dfs(u: int) -> bool:
        for v in adj[u]:
            pu = pairV.get(v, NIL)
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
        for u in range(1, q + 1):
            out.append(f"{u} {pairU[u]}".encode())
    else:
        out.append(b"NO")
    sys.stdout.buffer.write(b"\n".join(out))

if __name__ == "__main__":
    solve()