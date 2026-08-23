import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        if u != v:
            adj[v].append(u)
        else:
            # self-loop: keep it to detect impossibility
            adj[v].append(u)

    color = [-1] * n
    for start in range(n):
        if color[start] != -1:
            continue
        dq = deque([start])
        color[start] = 0
        while dq:
            v = dq.popleft()
            for to in adj[v]:
                if color[to] == -1:
                    color[to] = color[v] ^ 1
                    dq.append(to)
                elif color[to] == color[v]:
                    print("NO")
                    return

    out = ['YES']
    out.append(' '.join('1' if c == 0 else '2' for c in color))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()