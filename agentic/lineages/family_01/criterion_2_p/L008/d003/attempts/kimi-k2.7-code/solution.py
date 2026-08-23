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
    ans = [0] * n

    for start in range(n):
        if color[start] != -1:
            continue
        stack = [start]
        color[start] = 0
        comp = []
        min_node = start
        while stack:
            u = stack.pop()
            comp.append(u)
            if u < min_node:
                min_node = u
            cu = color[u]
            for w in adj[u]:
                if color[w] == -1:
                    color[w] = cu ^ 1
                    stack.append(w)
                elif color[w] == cu:
                    sys.stdout.write("NO\n")
                    return
        cmin = color[min_node]
        for v in comp:
            ans[v] = (color[v] ^ cmin) + 1

    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()