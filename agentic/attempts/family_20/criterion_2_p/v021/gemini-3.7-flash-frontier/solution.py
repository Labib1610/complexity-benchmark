import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    nL = int(input_data[0])
    nR = int(input_data[1])
    m = int(input_data[2])

    if m == 0:
        print("YES")
        print()
        return

    degL = [0] * (nL + 1)
    degR = [0] * (nR + 1)

    edges = []
    idx = 3
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        edges.append((u, v))
        degL[u] += 1
        degR[v] += 1

    delta = max(max(degL), max(degR))

    # match[node] maps color -> (neighbor, edge_index)
    match = [{} for _ in range(nL + nR + 1)]
    ans = [0] * m

    for i in range(m):
        u, v_orig = edges[i]
        v = v_orig + nL

        # Find free color at u
        match_u = match[u]
        c_u = 1
        while c_u in match_u:
            c_u += 1

        # Find free color at v
        match_v = match[v]
        c_v = 1
        while c_v in match_v:
            c_v += 1

        if c_u == c_v:
            match_u[c_u] = (v, i)
            match_v[c_u] = (u, i)
            ans[i] = c_u
        else:
            c1 = c_v
            c2 = c_u

            # Trace alternating (c1, c2) path starting from u
            curr = u
            c = c1
            path = []

            while c in match[curr]:
                nxt, edge_idx = match[curr][c]
                del match[curr][c]
                del match[nxt][c]
                other_c = c2 if c == c1 else c1
                path.append((curr, nxt, edge_idx, other_c))
                curr = nxt
                c = other_c

            for x, y, edge_idx, new_c in path:
                match[x][new_c] = (y, edge_idx)
                match[y][new_c] = (x, edge_idx)
                ans[edge_idx] = new_c

            match[u][c1] = (v, i)
            match[v][c1] = (u, i)
            ans[i] = c1

    print("YES")
    print(*(ans[i] for i in range(m)))


if __name__ == "__main__":
    solve()