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
    ans = [0] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != -1:
            continue

        stack = [start]
        color[start] = 0
        comp = [start]
        min_v = start

        while stack:
            u = stack.pop()
            cu = color[u]
            for w in adj[u]:
                cw = color[w]
                if cw == -1:
                    color[w] = cu ^ 1
                    stack.append(w)
                    comp.append(w)
                    if w < min_v:
                        min_v = w
                elif cw == cu:
                    sys.stdout.write("NO\n")
                    return

        flip = color[min_v]
        for v in comp:
            ans[v] = (color[v] ^ flip) + 1

    out = "YES\n" + " ".join(str(ans[i]) for i in range(1, n + 1)) + "\n"
    sys.stdout.write(out)

if __name__ == "__main__":
    solve()