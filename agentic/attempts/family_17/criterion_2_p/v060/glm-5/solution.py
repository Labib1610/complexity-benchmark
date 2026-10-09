import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0])
    t = int(data[1])
    n = 2 * q + 2
    S = 2 * q + 1
    T = 2 * q + 2

    head = [-1] * n
    to = []
    cap = []
    nxt = []

    def add_edge(u, v, c):
        head.append(0)
        head[u] = len(to)
        to.append(v)
        cap.append(c)
        nxt.append(-1)
        head[u] = len(to) - 1

        head.append(0)
        head[v] = len(to)
        to.append(u)
        cap.append(0)
        nxt.append(-1)
        head[v] = len(to) - 1

    idx = 2
    for _ in range(t):
        a = int(data[idx]); b = int(data[idx + 1]); idx += 2
        add_edge(a, b, 1)

    for a in range(1, q + 1):
        add_edge(S, a, 1)
    for b in range(q + 1, 2 * q + 1):
        add_edge(b, T, 1)

    level = [-1] * n
    ptr = [0] * n
    from collections import deque

    def bfs():
        for i in range(n):
            level[i] = -1
        level[S] = 0
        dq = deque([S])
        while dq:
            u = dq.popleft()
            e = head[u]
            while e != -1:
                v = to[e]
                if cap[e] > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    dq.append(v)
                e = nxt[e]
        return level[T] >= 0

    def dfs(u, f):
        if u == T:
            return f
        e = ptr[u]
        while e != -1:
            v = to[e]
            if cap[e] > 0 and level[v] == level[u] + 1:
                pushed = dfs(v, f if f < cap[e] else cap[e])
                if pushed > 0:
                    cap[e] -= pushed
                    cap[e ^ 1] += pushed
                    return pushed
            e = nxt[e]
            ptr[u] = e
        return 0

    flow = 0
    while bfs():
        for i in range(n):
            ptr[i] = head[i]
        while True:
            pushed = dfs(S, 1 << 30)
            if pushed == 0:
                break
            flow += pushed

    out = []
    if flow == q:
        out.append("YES")
        for u in range(1, q + 1):
            e = head[u]
            while e != -1:
                v = to[e]
                if q < v <= 2 * q and cap[e] == 0:
                    out.append(f"{u} {v}")
                    break
                e = nxt[e]
    else:
        out.append("NO")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()