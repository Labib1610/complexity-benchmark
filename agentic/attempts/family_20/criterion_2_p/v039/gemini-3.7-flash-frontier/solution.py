import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n_U = int(input_data[0])
    n_D = int(input_data[1])
    m = int(input_data[2])

    if m == 0:
        sys.stdout.write("YES\n\n")
        return

    edges = []
    deg_U = [0] * (n_U + 1)
    deg_D = [0] * (n_D + 1)

    idx = 3
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        edges.append((u, v))
        deg_U[u] += 1
        deg_D[v] += 1

    K = max(max(deg_U), max(deg_D))

    if K == 0:
        sys.stdout.write("YES\n\n")
        return

    # Bin-pack vertices in U
    super_U = [0] * (n_U + 1)
    b = 1
    cur_sum = 0
    for u in range(1, n_U + 1):
        d = deg_U[u]
        if cur_sum + d > K:
            b += 1
            cur_sum = 0
        super_U[u] = b
        cur_sum += d
    N_U = b

    # Bin-pack vertices in D
    super_D = [0] * (n_D + 1)
    b = 1
    cur_sum = 0
    for v in range(1, n_D + 1):
        d = deg_D[v]
        if cur_sum + d > K:
            b += 1
            cur_sum = 0
        super_D[v] = b
        cur_sum += d
    N_D = b

    N = max(N_U, N_D)
    stride = K + 1
    total_size = (N + 2) * stride

    match_L = [0] * total_size
    match_R = [0] * total_size
    edge_L = [0] * total_size
    edge_R = [0] * total_size

    ans = [0] * m

    for e_id in range(m):
        orig_u, orig_v = edges[e_id]
        u = super_U[orig_u]
        v = super_D[orig_v]

        u_offset = u * stride
        v_offset = v * stride

        # Find free color c1 at u
        c1 = 1
        while match_L[u_offset + c1] != 0:
            c1 += 1

        # Check if c1 is free at v
        if match_R[v_offset + c1] == 0:
            c2 = c1
        else:
            # Find free color c2 at v
            c2 = 1
            while match_R[v_offset + c2] != 0:
                c2 += 1

        if c1 == c2:
            match_L[u_offset + c1] = v
            match_R[v_offset + c1] = u
            edge_L[u_offset + c1] = e_id
            edge_R[v_offset + c1] = e_id
            ans[e_id] = c1
        else:
            cur_v = v
            cur_u = match_R[cur_v * stride + c1]

            while cur_u != 0:
                next_v = match_L[cur_u * stride + c2]

                e_cur = edge_R[cur_v * stride + c1]

                match_R[cur_v * stride + c2] = cur_u
                edge_R[cur_v * stride + c2] = e_cur

                match_L[cur_u * stride + c2] = cur_v
                edge_L[cur_u * stride + c2] = e_cur
                ans[e_cur] = c2

                if next_v == 0:
                    match_L[cur_u * stride + c1] = 0
                    match_R[cur_v * stride + c1] = 0
                    break

                next_u = match_R[next_v * stride + c1]
                e_next = edge_R[next_v * stride + c2]

                match_L[cur_u * stride + c1] = next_v
                edge_L[cur_u * stride + c1] = e_next

                match_R[next_v * stride + c1] = cur_u
                edge_R[next_v * stride + c1] = e_next
                ans[e_next] = c1

                if next_u == 0:
                    match_R[next_v * stride + c2] = 0
                    break

                cur_v = next_v
                cur_u = next_u

            match_L[u_offset + c1] = v
            match_R[v_offset + c1] = u
            edge_L[u_offset + c1] = e_id
            edge_R[v_offset + c1] = e_id
            ans[e_id] = c1

    sys.stdout.write("YES\n" + " ".join(map(str, ans)) + "\n")


if __name__ == "__main__":
    solve()