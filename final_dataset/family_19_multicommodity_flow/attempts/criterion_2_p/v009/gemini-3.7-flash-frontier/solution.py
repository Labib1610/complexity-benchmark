from collections import deque
import sys

# Increase recursion depth for deep DFS in Dinic's algorithm
sys.setrecursionlimit(300000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    # input_data[2] is the constant 1 from 'n m 1'

    s = int(input_data[3])
    t = int(input_data[4])
    d = int(input_data[5])

    idx = 6

    head = [-1] * (n + 1)
    to = []
    cap = []
    nxt = []
    edge_idx = []

    def add_edge(u, v, c, e_idx):
        nxt.append(head[u])
        head[u] = len(to)
        to.append(v)
        cap.append(c)
        edge_idx.append(e_idx)

        nxt.append(head[v])
        head[v] = len(to)
        to.append(u)
        cap.append(0)
        edge_idx.append(-1)

    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        c = int(input_data[idx + 2])
        idx += 3
        add_edge(u, v, c, i)

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
                if cap[e] > 0 and level[to[e]] < 0:
                    level[to[e]] = level[v] + 1
                    q.append(to[e])
                e = nxt[e]
        return level[t] != -1

    def dfs(v, pushed):
        if pushed == 0:
            return 0
        if v == t:
            return pushed
        e = ptr[v]
        while e != -1:
            trg = to[e]
            if level[v] + 1 == level[trg] and cap[e] > 0:
                tr = dfs(trg, min(pushed, cap[e]))
                if tr > 0:
                    cap[e] -= tr
                    cap[e ^ 1] += tr
                    return tr
            e = nxt[e]
            ptr[v] = e
        return 0

    flow = 0
    while flow < d and bfs():
        for i in range(n + 1):
            ptr[i] = head[i]
        while flow < d:
            pushed = dfs(s, d - flow)
            if pushed == 0:
                break
            flow += pushed

    if flow < d:
        print("NO")
    else:
        print("YES")
        ans = [0] * m
        for e in range(0, 2 * m, 2):
            ans[edge_idx[e]] = cap[e ^ 1]
        print(*(ans))


if __name__ == "__main__":
    solve()