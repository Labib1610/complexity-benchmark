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

    color = [0] * (n + 1)
    for i in range(1, n + 1):
        if color[i]:
            continue
        color[i] = 1
        stack = [i]
        while stack:
            u = stack.pop()
            cu = color[u]
            opp = 3 - cu
            for w in adj[u]:
                cw = color[w]
                if cw == 0:
                    color[w] = opp
                    stack.append(w)
                elif cw == cu:
                    sys.stdout.write("NO\n")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join(map(str, color[1:])))

if __name__ == "__main__":
    solve()