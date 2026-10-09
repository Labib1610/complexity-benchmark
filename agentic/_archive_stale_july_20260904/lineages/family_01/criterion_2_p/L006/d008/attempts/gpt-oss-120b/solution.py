import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [ -1 ] * (n + 1)   # -1 unvisited, 0 -> mode 1, 1 -> mode 2
    stack = []
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # start new component, assign smallest index (start) to color 0 (mode 1)
        color[start] = 0
        stack.append(start)
        while stack:
            u = stack.pop()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    stack.append(v)
                elif color[v] == cu:
                    # not bipartite
                    print("NO")
                    return
    # construct answer
    ans = [str(1 if color[i] == 0 else 2) for i in range(1, n + 1)]
    print("YES")
    print(' '.join(ans))

if __name__ == "__main__":
    solve()