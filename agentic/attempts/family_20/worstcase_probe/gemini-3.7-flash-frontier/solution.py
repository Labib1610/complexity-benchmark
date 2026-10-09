import sys

sys.setrecursionlimit(10000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])

    edges = []
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        edges.append((u, v))

    v_edges = [[] for _ in range(n)]
    for e_idx, (u, v) in enumerate(edges):
        v_edges[u].append(e_idx)
        v_edges[v].append(e_idx)

    for v in range(n):
        if len(v_edges[v]) != 3:
            print("NO")
            return

    line_adj = [[] for _ in range(m)]
    for e_idx, (u, v) in enumerate(edges):
        nbrs = set()
        for e2 in v_edges[u]:
            if e2 != e_idx:
                nbrs.add(e2)
        for e2 in v_edges[v]:
            if e2 != e_idx:
                nbrs.add(e2)
        line_adj[e_idx] = list(nbrs)

    color = [-1] * m
    color_cnt = [[0, 0, 0] for _ in range(m)]
    avail_mask = [7] * m

    bucket = [set() for _ in range(4)]
    for i in range(m):
        bucket[3].add(i)

    def set_color(u, c):
        color[u] = c
        old_k = bin(avail_mask[u]).count("1")
        if u in bucket[old_k]:
            bucket[old_k].remove(u)

        affected = []
        for nbr in line_adj[u]:
            if color[nbr] == -1:
                if color_cnt[nbr][c] == 0:
                    old_mask = avail_mask[nbr]
                    old_k = bin(old_mask).count("1")
                    new_mask = old_mask & ~(1 << c)
                    avail_mask[nbr] = new_mask
                    bucket[old_k].remove(nbr)
                    new_k = bin(new_mask).count("1")
                    if new_k > 0:
                        bucket[new_k].add(nbr)
                    affected.append((nbr, True))
                else:
                    affected.append((nbr, False))
                color_cnt[nbr][c] += 1
        return affected

    def unset_color(u, c, affected):
        for nbr, mask_changed in affected:
            color_cnt[nbr][c] -= 1
            if color[nbr] == -1 and mask_changed:
                old_mask = avail_mask[nbr]
                old_k = bin(old_mask).count("1")
                if old_k > 0:
                    bucket[old_k].remove(nbr)
                new_mask = old_mask | (1 << c)
                avail_mask[nbr] = new_mask
                new_k = bin(new_mask).count("1")
                bucket[new_k].add(nbr)

        color[u] = -1
        k = bin(avail_mask[u]).count("1")
        bucket[k].add(u)

    backtracks = 0
    max_backtracks = 500000

    def dfs(uncolored):
        nonlocal backtracks
        if uncolored == 0:
            return True
        backtracks += 1
        if backtracks > max_backtracks:
            return False

        if len(bucket[1]) + len(bucket[2]) + len(bucket[3]) != uncolored:
            return False

        if bucket[1]:
            u = next(iter(bucket[1]))
        elif bucket[2]:
            u = next(iter(bucket[2]))
        else:
            u = next(iter(bucket[3]))

        mask = avail_mask[u]
        for c in range(3):
            if (mask >> c) & 1:
                affected = set_color(u, c)
                if dfs(uncolored - 1):
                    return True
                unset_color(u, c, affected)
        return False

    u0 = 0
    e_inc = v_edges[u0]
    set_color(e_inc[0], 0)
    set_color(e_inc[1], 1)
    set_color(e_inc[2], 2)

    if dfs(m - 3):
        print("YES")
        print(*(color[i] + 1 for i in range(m)))
    else:
        print("NO")


if __name__ == "__main__":
    solve()