import random
import sys
import time


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
        edges.append((u, v))
        idx += 2

    deg = [0] * n
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    for d in deg:
        if d != 3:
            print("NO")
            return

    start_time = time.time()
    TIME_LIMIT = 4.5

    while time.time() - start_time < TIME_LIMIT:
        color = [0] * m
        edge_at_vert = [[-1] * 4 for _ in range(n)]

        def set_edge_color(e_idx, c):
            color[e_idx] = c
            u, v = edges[e_idx]
            edge_at_vert[u][c] = e_idx
            edge_at_vert[v][c] = e_idx

        def clear_edge_color(e_idx):
            c = color[e_idx]
            if c != 0:
                u, v = edges[e_idx]
                edge_at_vert[u][c] = -1
                edge_at_vert[v][c] = -1
                color[e_idx] = 0

        edge_order = list(range(m))
        random.shuffle(edge_order)

        success = True
        for e in edge_order:
            curr_e = e
            steps = 0
            MAX_STEPS = 2000
            while curr_e is not None:
                steps += 1
                if steps > MAX_STEPS or time.time() - start_time > TIME_LIMIT:
                    success = False
                    break

                u, v = edges[curr_e]
                M_u = [c for c in (1, 2, 3) if edge_at_vert[u][c] == -1]
                M_v = [c for c in (1, 2, 3) if edge_at_vert[v][c] == -1]

                common = set(M_u) & set(M_v)
                if common:
                    c = random.choice(list(common))
                    set_edge_color(curr_e, c)
                    curr_e = None
                else:
                    c1 = random.choice(M_u)
                    c2 = random.choice(M_v)

                    curr = v
                    curr_c = c1
                    chain = []
                    while edge_at_vert[curr][curr_c] != -1:
                        e_idx = edge_at_vert[curr][curr_c]
                        chain.append(e_idx)
                        u_e, v_e = edges[e_idx]
                        curr = v_e if curr == u_e else u_e
                        curr_c = c2 if curr_c == c1 else c1

                    if curr != u:
                        for e_idx in chain:
                            old_c = color[e_idx]
                            new_c = c2 if old_c == c1 else c1
                            u_e, v_e = edges[e_idx]
                            edge_at_vert[u_e][old_c] = -1
                            edge_at_vert[v_e][old_c] = -1
                            color[e_idx] = new_c
                            edge_at_vert[u_e][new_c] = e_idx
                            edge_at_vert[v_e][new_c] = e_idx
                        set_edge_color(curr_e, c1)
                        curr_e = None
                    else:
                        if random.random() < 0.5:
                            e_kick = edge_at_vert[u][c2]
                            clear_edge_color(e_kick)
                            set_edge_color(curr_e, c2)
                            curr_e = e_kick
                        else:
                            e_kick = edge_at_vert[v][c1]
                            clear_edge_color(e_kick)
                            set_edge_color(curr_e, c1)
                            curr_e = e_kick

            if not success:
                break

        if success and all(color[i] in (1, 2, 3) for i in range(m)):
            print("YES")
            print(*(color[i] for i in range(m)))
            return

    print("NO")


solve()