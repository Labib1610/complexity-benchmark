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
        if u != v:
            adj[v].append(u)

    colors = [0] * (n + 1)

    for i in range(1, n + 1):
        if colors[i] != 0:
            continue
        colors[i] = 1
        stack = [i]
        while stack:
            u = stack.pop()
            cu = colors[u]
            want = 3 - cu
            for v in adj[u]:
                cv = colors[v]
                if cv == 0:
                    colors[v] = want
                    stack.append(v)
                elif cv != want:
                    sys.stdout.write("NO")
                    return

    out = ["YES", " ".join(map(str, colors[1:]))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()