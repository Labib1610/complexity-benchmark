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

    edges = []
    idx = 3
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        edges.append((u, v))

    L_col = [{} for _ in range(nL + 1)]
    R_col = [{} for _ in range(nR + 1)]
    color_of_edge = [0] * m

    for i, (u, v) in enumerate(edges):
        # Find free color at u
        a = 1
        while a in L_col[u]:
            a += 1

        # Find free color at v
        b = 1
        while b in R_col[v]:
            b += 1

        if a == b:
            L_col[u][a] = (v, i)
            R_col[v][a] = (u, i)
            color_of_edge[i] = a
        else:
            # Trace alternating path starting at v with color a
            path = []
            cur = v
            cur_side = 1  # 1 = right, 0 = left
            c = a
            other_c = b

            while True:
                if cur_side == 1:
                    if c in R_col[cur]:
                        nxt, e = R_col[cur][c]
                        path.append((cur, nxt, e, 1, c))
                        cur = nxt
                        cur_side = 0
                        c, other_c = other_c, c
                    else:
                        break
                else:
                    if c in L_col[cur]:
                        nxt, e = L_col[cur][c]
                        path.append((cur, nxt, e, 0, c))
                        cur = nxt
                        cur_side = 1
                        c, other_c = other_c, c
                    else:
                        break

            for u_node, v_node, e, s, old_c in path:
                new_c = b if old_c == a else a
                color_of_edge[e] = new_c
                if s == 1:
                    del R_col[u_node][old_c]
                    del L_col[v_node][old_c]
                    R_col[u_node][new_c] = (v_node, e)
                    L_col[v_node][new_c] = (u_node, e)
                else:
                    del L_col[u_node][old_c]
                    del R_col[v_node][old_c]
                    L_col[u_node][new_c] = (v_node, e)
                    R_col[v_node][new_c] = (u_node, e)

            L_col[u][a] = (v, i)
            R_col[v][a] = (u, i)
            color_of_edge[i] = a

    sys.stdout.write("YES\n" + " ".join(map(str, color_of_edge)) + "\n")


if __name__ == "__main__":
    solve()