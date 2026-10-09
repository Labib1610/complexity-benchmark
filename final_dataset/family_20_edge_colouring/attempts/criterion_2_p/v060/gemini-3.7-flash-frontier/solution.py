import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n_T = int(input_data[0])
    n_P = int(input_data[1])
    m = int(input_data[2])

    if m == 0:
        print("YES")
        print()
        return

    deg_T = [0] * (n_T + 1)
    deg_P = [0] * (n_P + 1)

    edges = []
    idx = 3
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        edges.append((u, v))
        deg_T[u] += 1
        deg_P[v] += 1

    K = max(max(deg_T), max(deg_P))

    total_vertices = n_T + n_P + 1
    match = [{} for _ in range(total_vertices)]
    ans = [0] * m

    for i, (u, v) in enumerate(edges):
        pv = n_T + v

        # Find first free color for u
        match_u = match[u]
        c1 = 1
        while c1 in match_u:
            c1 += 1

        # Find first free color for pv
        match_pv = match[pv]
        c2 = 1
        while c2 in match_pv:
            c2 += 1

        if c1 == c2:
            match[u][c1] = (pv, i)
            match[pv][c1] = (u, i)
            ans[i] = c1
        else:
            path = []
            curr = pv
            c_a, c_b = c1, c2
            while c_a in match[curr]:
                nxt, edge_idx = match[curr][c_a]
                path.append((curr, nxt, edge_idx, c_a, c_b))
                curr = nxt
                c_a, c_b = c_b, c_a

            for x, y, edge_idx, old_c, new_c in path:
                del match[x][old_c]
                del match[y][old_c]

            for x, y, edge_idx, old_c, new_c in path:
                match[x][new_c] = (y, edge_idx)
                match[y][new_c] = (x, edge_idx)
                ans[edge_idx] = new_c

            match[u][c1] = (pv, i)
            match[pv][c1] = (u, i)
            ans[i] = c1

    print("YES")
    print(*(ans[i] for i in range(m)))


if __name__ == "__main__":
    solve()