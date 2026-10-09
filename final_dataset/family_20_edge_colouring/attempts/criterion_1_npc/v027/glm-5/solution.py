import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    edges = []
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for i in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)

    color = [0] * m
    for v in range(1, n + 1):
        used = {color[e] for e in adj[v]}
        for e in adj[v]:
            if color[e] == 0:
                for c in (1, 2, 3):
                    if c not in used:
                        color[e] = c
                        used.add(c)
                        break

    ok = True
    for v in range(1, n + 1):
        seen = set()
        for e in adj[v]:
            c = color[e]
            if c == 0 or c in seen:
                ok = False
                break
            seen.add(c)
        if not ok:
            break

    out = []
    if ok:
        out.append("YES")
        out.append(" ".join(map(str, color)))
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

solve()