import sys

def solve():
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
    for i in range(n):
        if color[i] != -1:
            continue
        color[i] = 0
        stack = [i]
        while stack:
            u = stack.pop()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    stack.append(v)
                elif color[v] == cu:
                    sys.stdout.write("NO")
                    return

    out = ["YES"]
    out.append(' '.join(str(c + 1) for c in color))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()