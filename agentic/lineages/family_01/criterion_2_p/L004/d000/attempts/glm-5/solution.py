import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)
    out = ["YES\n"]
    parts = []
    parts.append("YES\n")

    for i in range(1, n + 1):
        if color[i] != 0:
            continue
        # BFS to 2-color the component
        color[i] = 1
        q = deque([i])
        comp = [i]
        ok = True
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - cu
                    q.append(v)
                    comp.append(v)
                elif color[v] == cu:
                    ok = False
                    # can't break early because we still need to drain queue, but we can mark
        if not ok:
            sys.stdout.write("NO\n")
            return
        # comp is not needed further; color already assigned

    # Build output string
    # Lexicographically smallest: we used color 1 for the first node of each component,
    # which gives the smallest assignment because flipping a component would make the
    # first encountered node 2, which is larger.
    res = [str(color[i]) for i in range(1, n + 1)]
    sys.stdout.write("YES\n" + " ".join(res) + "\n")

solve()