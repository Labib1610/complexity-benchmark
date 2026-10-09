import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)
    for start in range(1, n + 1):
        if color[start] == 0:
            color[start] = 1
            stack = [start]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        sys.stdout.write("NO\n")
                        return

    out = ["YES"]
    out.append(" ".join(map(str, color[1:])))
    sys.stdout.write("\n".join(out) + "\n")

solve()