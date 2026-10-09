import sys

sys.setrecursionlimit(200000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])

    edges = []
    idx = 2
    adj = [[] for _ in range(n + 1)]
    for e in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        edges.append((u, v))
        adj[u].append(e)
        adj[v].append(e)

    for i in range(1, n + 1):
        if len(adj[i]) != 3:
            print("NO")
            return

    edge_col = [0] * m
    v_mask = [7] * (n + 1)

    visited = [False] * (n + 1)
    components = []
    for i in range(1, n + 1):
        if not visited[i]:
            comp_nodes = []
            q = [i]
            visited[i] = True
            for node in q:
                comp_nodes.append(node)
                for e in adj[node]:
                    u, v = edges[e]
                    other = u if node == v else v
                    if not visited[other]:
                        visited[other] = True
                        q.append(other)
            components.append(comp_nodes)

    initial_assigns = []
    for comp in components:
        root = comp[0]
        e0, e1, e2 = adj[root]
        initial_assigns.append((e0, 1))
        initial_assigns.append((e1, 2))
        initial_assigns.append((e2, 3))

    for e, c in initial_assigns:
        edge_col[e] = c
        u, v = edges[e]
        bit = 1 << (c - 1)
        v_mask[u] &= ~bit
        v_mask[v] &= ~bit

    unassigned = [e for e in range(m) if edge_col[e] == 0]

    def backtrack():
        forced_stack = []
        while True:
            min_c = 4
            best_e = -1
            best_mask = 0

            for e in unassigned:
                if edge_col[e] == 0:
                    u, v = edges[e]
                    mask = v_mask[u] & v_mask[v]
                    cnt = (mask & 1) + ((mask >> 1) & 1) + ((mask >> 2) & 1)
                    if cnt == 0:
                        for fe in reversed(forced_stack):
                            fc = edge_col[fe]
                            edge_col[fe] = 0
                            fu, fv = edges[fe]
                            fbit = 1 << (fc - 1)
                            v_mask[fu] |= fbit
                            v_mask[fv] |= fbit
                        return False
                    if cnt < min_c:
                        min_c = cnt
                        best_e = e
                        best_mask = mask
                        if cnt == 1:
                            break

            if best_e == -1:
                return True

            if min_c == 1:
                c = 1 if (best_mask & 1) else (2 if (best_mask & 2) else 3)
                edge_col[best_e] = c
                u, v = edges[best_e]
                bit = 1 << (c - 1)
                v_mask[u] &= ~bit
                v_mask[v] &= ~bit
                forced_stack.append(best_e)
            else:
                break

        choices = []
        if best_mask & 1:
            choices.append(1)
        if best_mask & 2:
            choices.append(2)
        if best_mask & 4:
            choices.append(3)

        u, v = edges[best_e]
        for c in choices:
            edge_col[best_e] = c
            bit = 1 << (c - 1)
            v_mask[u] &= ~bit
            v_mask[v] &= ~bit

            if backtrack():
                return True

            v_mask[u] |= bit
            v_mask[v] |= bit
            edge_col[best_e] = 0

        for fe in reversed(forced_stack):
            fc = edge_col[fe]
            edge_col[fe] = 0
            fu, fv = edges[fe]
            fbit = 1 << (fc - 1)
            v_mask[fu] |= fbit
            v_mask[fv] |= fbit
        return False

    if backtrack():
        print("YES")
        print(*(edge_col[e] for e in range(m)))
    else:
        print("NO")


if __name__ == "__main__":
    solve()