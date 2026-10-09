import sys
import random

# Increase recursion depth just in case
sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    edge_u = [0] * m
    edge_v = [0] * m
    adj = [[] for _ in range(n + 1)]

    idx = 2
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        edge_u[i] = u
        edge_v[i] = v
        adj[u].append((v, i))
        adj[v].append((u, i))

    # Check for bridges using Tarjan's bridge-finding algorithm
    # Any cubic graph with a bridge cannot have a 3-edge-coloring (1-factorization).
    tin = [0] * (n + 1)
    low = [0] * (n + 1)
    visited = [False] * (n + 1)
    timer = 0
    has_bridge = False

    def dfs(u, p_edge):
        nonlocal timer, has_bridge
        visited[u] = True
        timer += 1
        tin[u] = low[u] = timer
        for to, e_idx in adj[u]:
            if e_idx == p_edge:
                continue
            if visited[to]:
                low[u] = min(low[u], tin[to])
            else:
                dfs(to, e_idx)
                low[u] = min(low[u], low[to])
                if low[to] > tin[u]:
                    has_bridge = True

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, -1)

    if has_bridge:
        print("NO")
        return

    # Randomized Kempe-chain edge coloring
    # We attempt up to a certain number of restarts / iterations.
    max_restarts = 5
    max_steps_per_restart = 100000

    for restart in range(max_restarts):
        edge_color = [0] * m
        # color_edge[u][c] = edge_idx of color c incident to u, or -1
        color_edge = [[-1] * 4 for _ in range(n + 1)]

        uncolored_edges = list(range(m))
        random.shuffle(uncolored_edges)

        steps = 0
        success = True

        while uncolored_edges:
            e = uncolored_edges.pop()
            if edge_color[e] != 0:
                continue

            curr_e = e
            while curr_e != -1:
                steps += 1
                if steps > max_steps_per_restart:
                    success = False
                    break

                u = edge_u[curr_e]
                v = edge_v[curr_e]

                # Find free colors at u and v
                free_u = -1
                for c in (1, 2, 3):
                    if color_edge[u][c] == -1:
                        free_u = c
                        break

                free_v = -1
                for c in (1, 2, 3):
                    if color_edge[v][c] == -1:
                        free_v = c
                        break

                if free_u == free_v:
                    c = free_u
                    edge_color[curr_e] = c
                    color_edge[u][c] = curr_e
                    color_edge[v][c] = curr_e
                    curr_e = -1
                else:
                    a = free_u
                    b = free_v

                    # Trace (a, b)-chain starting from u
                    # Since 'a' is free at u, we look for an incident edge of color 'b'
                    curr = u
                    want_color = b
                    path_edges = []
                    while True:
                        e_idx = color_edge[curr][want_color]
                        if e_idx == -1:
                            break
                        path_edges.append(e_idx)
                        nxt = edge_u[e_idx] if edge_v[e_idx] == curr else edge_v[e_idx]
                        curr = nxt
                        want_color = a if want_color == b else b

                    if curr != v:
                        # Chain does not reach v: swap colors along the chain
                        for pe in path_edges:
                            old_c = edge_color[pe]
                            new_c = b if old_c == a else a
                            u1, v1 = edge_u[pe], edge_v[pe]
                            color_edge[u1][old_c] = -1
                            color_edge[v1][old_c] = -1
                            edge_color[pe] = new_c
                            color_edge[u1][new_c] = pe
                            color_edge[v1][new_c] = pe

                        # Now 'b' is free at both u and v
                        edge_color[curr_e] = b
                        color_edge[u][b] = curr_e
                        color_edge[v][b] = curr_e
                        curr_e = -1
                    else:
                        # Chain reaches v: pick randomly choice A or choice B
                        if random.random() < 0.5:
                            # Uncolor the edge with color b at u
                            e_uncolor = color_edge[u][b]
                            w = edge_u[e_uncolor] if edge_v[e_uncolor] == u else edge_v[e_uncolor]
                            edge_color[e_uncolor] = 0
                            color_edge[u][b] = -1
                            color_edge[w][b] = -1

                            edge_color[curr_e] = b
                            color_edge[u][b] = curr_e
                            color_edge[v][b] = curr_e
                            curr_e = e_uncolor
                        else:
                            # Uncolor the edge with color a at v
                            e_uncolor = color_edge[v][a]
                            z = edge_u[e_uncolor] if edge_v[e_uncolor] == v else edge_v[e_uncolor]
                            edge_color[e_uncolor] = 0
                            color_edge[v][a] = -1
                            color_edge[z][a] = -1

                            edge_color[curr_e] = a
                            color_edge[u][a] = curr_e
                            color_edge[v][a] = curr_e
                            curr_e = e_uncolor

            if not success:
                break

        if success:
            print("YES")
            print(*(edge_color[i] for i in range(m)))
            return

    print("NO")

if __name__ == '__main__':
    solve()