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

    color = [-1] * (n + 1)   # 0 or 1
    ans = [0] * (n + 1)

    for i in range(1, n + 1):
        if color[i] != -1:
            continue
        # start new component
        dq = deque([i])
        color[i] = 0
        ans[i] = 1
        while dq:
            u = dq.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - cu
                    ans[v] = color[v] + 1
                    dq.append(v)
                elif color[v] == cu:
                    sys.stdout.write("NO")
                    return
    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()