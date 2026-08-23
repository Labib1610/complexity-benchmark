import sys
from collections import deque

def solve():
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
        if u != v:
            adj[v].append(u)

    color = [0] * (n + 1)
    ans = [0] * (n + 1)
    possible = True

    for i in range(1, n + 1):
        if color[i]:
            continue
        dq = deque([i])
        color[i] = 1
        ans[i] = 1
        comp = []
        while dq:
            u = dq.popleft()
            comp.append(u)
            cu = color[u]
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - cu
                    ans[v] = 1 if color[v] == 1 else 2
                    dq.append(v)
                elif color[v] == cu:
                    possible = False
                    dq.clear()
                    break
            if not possible:
                break
        if not possible:
            break

    out = []
    if not possible:
        out.append("NO")
    else:
        out.append("YES")
        out.append(' '.join(str(ans[i]) for i in range(1, n + 1)))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()