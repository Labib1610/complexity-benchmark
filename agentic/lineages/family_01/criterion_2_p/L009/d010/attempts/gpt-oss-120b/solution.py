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
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    col = [0] * (n + 1)          # 0 = uncoloured, 1 or 2 otherwise

    for start in range(1, n + 1):
        if col[start]:
            continue
        col[start] = 1            # smallest vertex of this component → 1
        q = deque([start])
        while q:
            u = q.popleft()
            cu = col[u]
            for w in adj[u]:
                if col[w] == 0:
                    col[w] = 3 - cu
                    q.append(w)
                elif col[w] == cu:
                    sys.stdout.write("NO")
                    return

    out = ["YES"]
    out.append(' '.join(str(col[i]) for i in range(1, n + 1)))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()