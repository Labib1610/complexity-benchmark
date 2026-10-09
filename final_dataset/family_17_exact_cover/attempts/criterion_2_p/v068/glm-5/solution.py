import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0])
    t = int(data[1])
    n = 2 * q
    head = [-1] * (n + 1)
    to = [0] * (2 * t)
    nxt = [0] * (2 * t)
    idx = 0
    for i in range(t):
        a = int(data[2 + 2 * i])
        b = int(data[2 + 2 * i + 1])
        to[idx] = b
        nxt[idx] = head[a]
        head[a] = idx
        idx += 1
        to[idx] = a
        nxt[idx] = head[b]
        head[b] = idx
        idx += 1

    match = [0] * (n + 1)
    visited = [False] * (n + 1)
    ans = []

    def dfs(u):
        e = head[u]
        while e != -1:
            v = to[e]
            if not visited[v]:
                visited[v] = True
                if match[v] == 0 or dfs(match[v]):
                    match[v] = u
                    match[u] = v
                    return True
            e = nxt[e]
        return False

    for i in range(1, q + 1):
        visited = [False] * (n + 1)
        if not dfs(i):
            print("NO")
            return

    print("YES")
    out = []
    for i in range(1, q + 1):
        out.append(f"{i} {match[i]}")
    sys.stdout.write("\n".join(out) + "\n")

solve()