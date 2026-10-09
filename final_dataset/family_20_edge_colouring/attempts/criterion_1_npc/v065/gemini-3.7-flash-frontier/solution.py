import sys
import random
import time

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    edges = []
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))

    start_time = time.time()
    
    # Run the Kempe-chain heuristic to find a 3-edge-coloring
    # Try up to a few restarts if needed
    for attempt in range(5):
        if time.time() - start_time > 4.2:
            break

        edge_color = [0] * m
        node_color_edge = [[-1] * 4 for _ in range(n + 1)]
        
        uncolored = list(range(m))
        random.shuffle(uncolored)

        steps = 0
        max_steps = 100000 + m * 50

        while uncolored and steps < max_steps:
            steps += 1
            if steps % 1000 == 0 and time.time() - start_time > 4.2:
                break

            e_idx = uncolored.pop()
            if edge_color[e_idx] != 0:
                continue

            u, v = edges[e_idx]

            # Missing colors at u and v
            missing_u = [c for c in (1, 2, 3) if node_color_edge[u][c] == -1]
            missing_v = [c for c in (1, 2, 3) if node_color_edge[v][c] == -1]

            # Common missing color?
            common = set(missing_u) & set(missing_v)
            if common:
                c = random.choice(list(common))
                edge_color[e_idx] = c
                node_color_edge[u][c] = e_idx
                node_color_edge[v][c] = e_idx
                continue

            # Try Kempe chain swaps
            found_kempe = False
            # Shuffle missing colors to randomize
            random.shuffle(missing_u)
            random.shuffle(missing_v)

            for cu in missing_u:
                for cv in missing_v:
                    # Trace (cu, cv) alternating path starting at v
                    path = []
                    curr = v
                    curr_c = cu
                    while True:
                        e_next = node_color_edge[curr][curr_c]
                        if e_next == -1:
                            break
                        path.append(e_next)
                        nu, nv = edges[e_next]
                        curr = nu if curr == nv else nv
                        curr_c = cv if curr_c == cu else cu

                    if curr != u:
                        # Success! Flip path
                        for ep in path:
                            c_old = edge_color[ep]
                            eu, ev = edges[ep]
                            node_color_edge[eu][c_old] = -1
                            node_color_edge[ev][c_old] = -1

                        for ep in path:
                            c_old = edge_color[ep]
                            c_new = cu if c_old == cv else cv
                            edge_color[ep] = c_new
                            eu, ev = edges[ep]
                            node_color_edge[eu][c_new] = ep
                            node_color_edge[ev][c_new] = ep

                        edge_color[e_idx] = cu
                        node_color_edge[u][cu] = e_idx
                        node_color_edge[v][cu] = e_idx
                        found_kempe = True
                        break
                if found_kempe:
                    break

            if not found_kempe:
                # Forced move: pick a random missing color at u, assign to e,
                # and uncolor the conflicting edge at v
                cu = random.choice(missing_u)
                conflicting_edge = node_color_edge[v][cu]

                # Uncolor conflicting_edge
                edge_color[conflicting_edge] = 0
                cu_u, cu_v = edges[conflicting_edge]
                node_color_edge[cu_u][cu] = -1
                node_color_edge[cu_v][cu] = -1

                # Color e_idx with cu
                edge_color[e_idx] = cu
                node_color_edge[u][cu] = e_idx
                node_color_edge[v][cu] = e_idx

                uncolored.append(conflicting_edge)

        if not uncolored and all(c > 0 for c in edge_color):
            print("YES")
            print(*(edge_color[i] for i in range(m)))
            return

    print("NO")

if __name__ == '__main__':
    solve()