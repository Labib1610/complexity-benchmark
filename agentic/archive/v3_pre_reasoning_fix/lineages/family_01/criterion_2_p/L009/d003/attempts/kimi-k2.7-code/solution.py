import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    val = [0] * (n + 1)  # 0 unvisited, otherwise 1 or 2

    for i in range(1, n + 1):
        if val[i] != 0:
            continue
        val[i] = 1
        dq = deque([i])
        while dq:
            u = dq.popleft()
            need = 3 - val[u]
            for w in adj[u]:
                if val[w] == 0:
                    val[w] = need
                    dq.append(w)
                elif val[w] != need:
                    sys.stdout.write("NO")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, val[1:])))

if __name__ == "__main__":
    solve()