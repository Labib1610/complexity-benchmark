import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)  # 0 or 1 relative color

    for i in range(1, n + 1):
        if color[i] != -1:
            continue
        # start new component
        dq = deque([i])
        color[i] = 0
        while dq:
            u = dq.popleft()
            cu = color[u]
            for v in adj[u]:
                cv = color[v]
                if cv == -1:
                    color[v] = cu ^ 1
                    dq.append(v)
                elif cv == cu:
                    sys.stdout.write("NO\n")
                    return

    # build result: 1 if relative color 0 else 2
    res = ['1' if color[i] == 0 else '2' for i in range(1, n + 1)]
    out = "YES\n" + ' '.join(res) + '\n'
    sys.stdout.write(out)

if __name__ == "__main__":
    solve()