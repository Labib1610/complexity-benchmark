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
        adj[v].append(u)

    color = [0] * (n + 1)
    possible = True

    for start in range(1, n + 1):
        if color[start] == 0:
            comp = []
            q = deque([start])
            color[start] = 1
            comp.append(start)
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        comp.append(v)
                        q.append(v)
                    elif color[v] == color[u]:
                        possible = False
            if not possible:
                break
            # Count ones and twos in this component
            ones = 0
            twos = 0
            for u in comp:
                if color[u] == 1:
                    ones += 1
                else:
                    twos += 1
            # Choose assignment that minimizes the concatenated integer
            # If more ones, keep as is (1 is smaller, and more leading positions get 1)
            # If more twos, flip the component
            # If equal, keep as is (1 is smaller)
            if twos > ones:
                for u in comp:
                    color[u] = 3 - color[u]

    if not possible:
        sys.stdout.write("NO\n")
    else:
        out = ["YES"]
        out.append(" ".join(str(color[i]) for i in range(1, n + 1)))
        sys.stdout.write("\n".join(out) + "\n")

solve()