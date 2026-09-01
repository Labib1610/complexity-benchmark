import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        g[u].append(v)
        g[v].append(u)

    col = [-1] * (n + 1)          # -1 = unvisited, 0 -> band 1, 1 -> band 2
    for start in range(1, n + 1):
        if col[start] != -1:
            continue
        col[start] = 0
        q = deque([start])
        while q:
            x = q.popleft()
            cx = col[x]
            for y in g[x]:
                if col[y] == -1:
                    col[y] = cx ^ 1
                    q.append(y)
                elif col[y] == cx:
                    sys.stdout.write("NO")
                    return

    # success
    out = ['YES\n']
    out.append(' '.join('1' if col[i] == 0 else '2' for i in range(1, n + 1)))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()