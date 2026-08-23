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

    color = [0] * n
    stack = []
    for i in range(n):
        if color[i]:
            continue
        color[i] = 1
        stack.append(i)
        while stack:
            v = stack.pop()
            cv = color[v]
            opp = 3 - cv
            for nb in adj[v]:
                if color[nb] == 0:
                    color[nb] = opp
                    stack.append(nb)
                elif color[nb] == cv:
                    sys.stdout.write("NO")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, color)))

if __name__ == "__main__":
    solve()