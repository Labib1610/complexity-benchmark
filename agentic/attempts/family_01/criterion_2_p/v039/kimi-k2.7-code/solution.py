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

    comp = [-1] * (n + 1)
    color = [-1] * (n + 1)
    comps = 0
    ok = True

    for i in range(1, n + 1):
        if comp[i] != -1:
            continue
        stack = [i]
        comp[i] = comps
        color[i] = 0
        while stack and ok:
            v = stack.pop()
            nxt = color[v] ^ 1
            for to in adj[v]:
                if comp[to] == -1:
                    comp[to] = comps
                    color[to] = nxt
                    stack.append(to)
                elif color[to] == color[v]:
                    ok = False
                    break
        if not ok:
            break
        comps += 1

    if not ok:
        sys.stdout.write("NO\n")
        return

    flip = [-1] * comps
    out = []
    for i in range(1, n + 1):
        cid = comp[i]
        f = flip[cid]
        if f == -1:
            f = color[i]
            flip[cid] = f
        out.append(str((color[i] ^ f) + 1))

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(out))
    sys.stdout.write("\n")

if __name__ == "__main__":
    solve()