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
        adj[v].append(u)

    color = [-1] * n
    ans = [0] * n

    for start in range(n):
        if color[start] != -1:
            continue
        q = deque([start])
        color[start] = 0
        comp = []
        minv = start
        while q:
            v = q.popleft()
            comp.append(v)
            if v < minv:
                minv = v
            cv = color[v]
            for w in adj[v]:
                if color[w] == -1:
                    color[w] = cv ^ 1
                    q.append(w)
                elif color[w] == cv:
                    sys.stdout.write("NO")
                    return

        # Make the smallest-index vertex in this component equal to 1.
        if color[minv] == 0:
            for v in comp:
                ans[v] = color[v] + 1
        else:
            for v in comp:
                ans[v] = 2 - color[v]

    out = ["YES", " ".join(map(str, ans))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()