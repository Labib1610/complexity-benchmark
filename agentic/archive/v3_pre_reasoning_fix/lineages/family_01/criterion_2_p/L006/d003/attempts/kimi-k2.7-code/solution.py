import sys

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

    color = [-1] * (n + 1)
    stack = []

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        color[start] = 0
        stack.append(start)
        while stack:
            u = stack.pop()
            cu = color[u]
            for v in adj[u]:
                cv = color[v]
                if cv == -1:
                    color[v] = cu ^ 1
                    stack.append(v)
                elif cv == cu:
                    sys.stdout.write("NO\n")
                    return

    out = ['YES', ' '.join(str(color[i] + 1) for i in range(1, n + 1))]
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()