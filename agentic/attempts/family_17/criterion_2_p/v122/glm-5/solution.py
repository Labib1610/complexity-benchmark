import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0])
    t = int(data[1])
    n = 2 * q
    head = [-1] * (n + 1)
    to = [0] * (2 * t)
    nxt = [0] * (2 * t)
    edge_cnt = 0

    def add_edge(u, v):
        nonlocal edge_cnt
        to[edge_cnt] = v
        nxt[edge_cnt] = head[u]
        head[u] = edge_cnt
        edge_cnt += 1

    idx = 2
    for _ in range(t):
        a = int(data[idx]); b = int(data[idx + 1])
        idx += 2
        add_edge(a, b)
        add_edge(b, a)

    match = [0] * (n + 1)
    for i in range(1, n + 1):
        match[i] = i

    def augment(root):
        parent = [0] * (n + 1)
        base = list(range(n + 1))
        in_blossom = [False] * (n + 1)
        in_queue = [False] * (n + 1)
        queue = [root]
        in_queue[root] = True
        head_q = 0
        while head_q < len(queue):
            u = queue[head_q]
            head_q += 1
            e = head[u]
            while e != -1:
                v = to[e]
                e = nxt[e]
                if base[u] == base[v] or match[u] == v:
                    continue
                if v == root or (match[v] != v and parent[match[v]] != 0):
                    cur_base = lca(base, u, v, parent, in_blossom)
                    in_blossom = [False] * (n + 1)
                    mark_path(u, cur_base, v, parent, base, in_blossom, queue, in_queue)
                    mark_path(v, cur_base, u, parent, base, in_blossom, queue, in_queue)
                    nb = base[cur_base]
                    while in_blossom[nb]:
                        in_blossom[nb] = False
                        nb = base[nb]
                elif parent[v] == 0:
                    parent[v] = u
                    if match[v] != v:
                        nxt_node = match[v]
                        if not in_queue[nxt_node]:
                            in_queue[nxt_node] = True
                            queue.append(nxt_node)
                    else:
                        while v != root:
                            pv = parent[v]
                            ppv = match[pv]
                            match[v] = pv
                            match[pv] = v
                            v = ppv
                        match[root] = root
                        return True
        return False

    def lca(base, u, v, parent, in_blossom):
        used = [False] * (n + 1)
        while True:
            u = base[u]
            used[u] = True
            if match[u] == u:
                break
            u = parent[match[u]]
        while True:
            v = base[v]
            if used[v]:
                return v
            v = parent[match[v]]

    def mark_path(u, b, child, parent, base, in_blossom, queue, in_queue):
        while base[u] != b:
            in_blossom[base[u]] = True
            in_blossom[base[match[u]]] = True
            parent[u] = child
            child = match[u]
            if not in_queue[base[u]]:
                in_queue[base[u]] = True
                queue.append(base[u])
            u = parent[match[u]]

    for i in range(1, q + 1):
        if match[i] == i:
            augment(i)

    ok = True
    for i in range(1, q + 1):
        if match[i] == i or match[i] <= q:
            ok = False
            break
    if ok:
        for j in range(q + 1, 2 * q + 1):
            if match[j] == j or match[j] > q:
                ok = False
                break

    out = []
    if ok:
        out.append("YES")
        for i in range(1, q + 1):
            out.append(f"{i} {match[i]}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()