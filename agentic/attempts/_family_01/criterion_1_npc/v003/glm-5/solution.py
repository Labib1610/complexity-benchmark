import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [0] * (n + 1)
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    color = [0] * (n + 1)
    order = list(range(1, n + 1))
    order.sort(key=lambda x: bin(adj[x]).count('1'), reverse=True)

    def dfs(pos):
        if pos == len(order):
            return True
        u = order[pos]
        forbidden = 0
        for v in range(1, n + 1):
            if (adj[u] >> v) & 1 and color[v]:
                forbidden |= 1 << color[v]
        for c in range(1, 4):
            if not (forbidden >> c) & 1:
                color[u] = c
                if dfs(pos + 1):
                    return True
                color[u] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(color[i]) for i in range(1, n + 1)))
    else:
        print("NO")

solve()