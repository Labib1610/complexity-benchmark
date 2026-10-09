import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    Nin = int(input_data[0])
    Nout = int(input_data[1])
    M = int(input_data[2])

    if M == 0:
        print("YES")
        print()
        return

    ans = [0] * M
    total_nodes = Nin + Nout + 1
    match = [{} for _ in range(total_nodes)]

    idx = 3
    for e_id in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx + 1]) + Nin
        idx += 2

        # Find first free color at u
        match_u = match[u]
        a = 1
        while a in match_u:
            a += 1

        # Find first free color at v
        match_v = match[v]
        b = 1
        while b in match_v:
            b += 1

        if a == b:
            match_u[a] = (v, e_id)
            match_v[a] = (u, e_id)
            ans[e_id] = a
        else:
            # Trace alternating path starting at v with colors a, b
            p_nodes = [v]
            p_edges = []
            curr = v
            c = a
            while c in match[curr]:
                nxt, nxt_eid = match[curr][c]
                p_nodes.append(nxt)
                p_edges.append(nxt_eid)
                curr = nxt
                c = b if c == a else a

            # Delete old color assignments along path
            for i, e in enumerate(p_edges):
                old_c = a if (i % 2 == 0) else b
                u_i = p_nodes[i]
                v_i = p_nodes[i + 1]
                del match[u_i][old_c]
                del match[v_i][old_c]

            # Re-insert with flipped colors
            for i, e in enumerate(p_edges):
                new_c = b if (i % 2 == 0) else a
                u_i = p_nodes[i]
                v_i = p_nodes[i + 1]
                match[u_i][new_c] = (v_i, e)
                match[v_i][new_c] = (u_i, e)
                ans[e] = new_c

            # Insert current edge (u, v) with color a
            match[u][a] = (v, e_id)
            match[v][a] = (u, e_id)
            ans[e_id] = a

    print("YES")
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    solve()