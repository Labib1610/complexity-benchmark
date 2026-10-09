import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    bad = False
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            bad = True
        else:
            adj[u].append(v)
            adj[v].append(u)
    if bad:
        sys.stdout.write("NO\n")
        return

    color = [-1] * n
    out = [0] * n

    for i in range(n):
        if color[i] != -1:
            continue
        stack = [i]
        color[i] = 0
        comp = [i]
        while stack:
            v = stack.pop()
            cv = color[v]
            for w in adj[v]:
                if color[w] == -1:
                    color[w] = cv ^ 1
                    stack.append(w)
                    comp.append(w)
                elif color[w] == cv:
                    sys.stdout.write("NO\n")
                    return
        min_v = min(comp)
        p = color[min_v]
        for v in comp:
            out[v] = 1 if color[v] == p else 2

    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join(map(str, out)) + '\n')

if __name__ == "__main__":
    solve()