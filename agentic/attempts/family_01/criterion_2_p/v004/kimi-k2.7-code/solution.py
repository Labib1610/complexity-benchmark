import sys

def solve() -> None:
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
    ans = [0] * n

    for i in range(n):
        if color[i] != -1:
            continue
        comp = []
        stack = [i]
        color[i] = 0
        while stack:
            v = stack.pop()
            comp.append(v)
            cv = color[v]
            for w in adj[v]:
                if color[w] == -1:
                    color[w] = cv ^ 1
                    stack.append(w)
                elif color[w] == cv:
                    sys.stdout.write("NO")
                    return
        mn = min(comp)
        if color[mn] == 0:
            for v in comp:
                ans[v] = color[v] + 1
        else:
            for v in comp:
                ans[v] = 2 - color[v]

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, ans)))

if __name__ == "__main__":
    solve()