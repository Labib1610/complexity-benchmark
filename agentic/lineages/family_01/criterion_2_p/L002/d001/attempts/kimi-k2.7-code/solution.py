import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    g = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        g[u].append(v)
        g[v].append(u)

    color = [-1] * n
    for i in range(n):
        if color[i] != -1:
            continue
        color[i] = 0
        stack = [i]
        while stack:
            v = stack.pop()
            cv = color[v]
            opp = cv ^ 1
            for to in g[v]:
                c = color[to]
                if c == -1:
                    color[to] = opp
                    stack.append(to)
                elif c == cv:
                    sys.stdout.write("NO\n")
                    return

    assignment = ' '.join(str(c + 1) for c in color)
    sys.stdout.write("YES\n" + assignment + "\n")

if __name__ == "__main__":
    solve()