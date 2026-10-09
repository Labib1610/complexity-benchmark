import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    k = int(input_data[idx]); idx += 1

    orders = []
    for _ in range(k):
        s = int(input_data[idx]); idx += 1
        t = int(input_data[idx]); idx += 1
        d = int(input_data[idx]); idx += 1
        orders.append((s, t, d))

    edges = []
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        cap = int(input_data[idx]); idx += 1
        edges.append((u, v, cap))

    N = n + 2
    S = n
    T = n + 1
    M = m + 2 * k
    head = [-1] * N
    to = [0] * (2 * M)
    cap_arr = [0] * (2 * M)
    nxt = [0] * (2 * M)
    ecnt = 0

    def add_edge(u, v, c):
        nonlocal ecnt
        to[ecnt] = v
        cap_arr[ecnt] = c
        nxt[ecnt] = head[u]
        head[u] = ecnt
        ecnt += 1
        to[ecnt] = u
        cap_arr[ecnt] = 0
        nxt[ecnt] = head[v]
        head[v] = ecnt
        ecnt += 1

    edge_id_to_arc = [-1] * m
    for j in range(m):
        u, v, c = edges[j]
        edge_id_to_arc[j] = ecnt
        add_edge(u, v, c)

    order_arc = []
    for i in range(k):
        s, t, d = orders[i]
        add_edge(S, s, d)
        add_edge(t, T, d)
        order_arc.append((ecnt - 4, ecnt - 1))

    level = [0] * N
    q = [0] * N

    def bfs():
        for i in range(N):
            level[i] = -1
        level[S] = 0
        qh = 0
        qt = 0
        q[qt] = S
        qt += 1
        while qh < qt:
            u = q[qh]
            qh += 1
            e = head[u]
            while e != -1:
                v = to[e]
                if cap_arr[e] > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q[qt] = v
                    qt += 1
                e = nxt[e]
        return level[T] >= 0

    def dfs_flow():
        stack = [(S, 1 << 60)]
        path = []
        while stack:
            u, f = stack[-1]
            if u == T:
                return f
            advanced = False
            e = head[u]
            while e != -1:
                v = to[e]
                if cap_arr[e] > 0 and level[v] == level[u] + 1:
                    stack.append((v, min(f, cap_arr[e])))
                    path.append(e)
                    advanced = True
                    head[u] = nxt[e]
                    break
                e = nxt[e]
            if not advanced:
                stack.pop()
                if path:
                    path.pop()
                level[u] = -1
        return 0

    total_demand = sum(d for _, _, d in orders)
    flow = 0
    while flow < total_demand:
        if not bfs():
            break
        while True:
            f = dfs_flow()
            if f == 0:
                break
            flow += f
            for e in path:
                cap_arr[e] -= f
                cap_arr[e ^ 1] += f

    if flow < total_demand:
        print("NO")
        return

    print("YES")
    out_lines = []
    for i in range(k):
        src_arc, _ = order_arc[i]
        f = cap_arr[src_arc ^ 1]
        row = [0] * m
        for j in range(m):
            arc = edge_id_to_arc[j]
            row[j] = cap_arr[arc ^ 1]
        out_lines.append(' '.join(map(str, row)))
    sys.stdout.write('\n'.join(out_lines) + '\n')

solve()