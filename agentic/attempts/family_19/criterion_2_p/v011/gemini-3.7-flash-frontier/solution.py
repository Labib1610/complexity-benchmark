from collections import deque
import sys

# Increase recursion depth just in case
sys.setrecursionlimit(200000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    _ = next(it)

    s = int(next(it))
    t = int(next(it))
    d = int(next(it))

    head = [-1] * (n + 1)
    to = []
    cap = []
    nxt = []
    orig_cap = []

    def add_edge(u, v, c):
        to.append(v)
        cap.append(c)
        nxt.append(head[u])
        head[u] = len(to) - 1

        to.append(u)
        cap.append(0)
        nxt.append(head[v])
        head[v] = len(to) - 1

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        c = int(next(it))
        orig_cap.append(c)
        add_edge(u, v, c)

    if s == t:
        if d == 0:
            print("YES")
            print(" ".join(["0"] * m))
        else:
            print("NO")
        return

    level = [-1] * (n + 1)
    ptr = [0] * (n + 1)

    def bfs():
        for i in range(n + 1):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            e = head[v]
            while e != -1:
                u = to[e]
                if cap[e] > 0 and level[u] < 0:
                    level[u] = level[v] + 1
                    q.append(u)
                e = nxt[e]
        return level[t] != -1

    def dfs(v, pushed):
        if pushed == 0:
            return 0
        if v == t:
            return pushed
        e = ptr[v]
        while e != -1:
            u = to[e]
            tr = cap[e]
            if level[v] + 1 == level[u] and tr > 0:
                push = dfs(u, min(pushed, tr))
                if push > 0:
                    cap[e] -= push
                    cap[e ^ 1] += push
                    return push
            e = nxt[e]
            ptr[v] = e
        return 0

    total_flow = 0
    while total_flow < d and bfs():
        for i in range(n + 1):
            ptr[i] = head[i]
        while total_flow < d:
            pushed = dfs(s, d - total_flow)
            if pushed == 0:
                break
            total_flow += pushed

    if total_flow < d:
        print("NO")
    else:
        print("YES")
        ans = []
        for i in range(m):
            ans.append(str(orig_cap[i] - cap[2 * i]))
        print(" ".join(ans))


if __name__ == "__main__":
    solve()