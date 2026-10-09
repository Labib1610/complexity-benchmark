import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N_in = int(next(it))
    N_out = int(next(it))
    M = int(next(it))

    edges = []
    deg_in = [0] * (N_in + 1)
    deg_out = [0] * (N_out + 1)

    for _ in range(M):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        deg_in[u] += 1
        deg_out[v] += 1

    D = max(max(deg_in), max(deg_out))
    # adjacency: for each vertex store list of (neighbor, edge_id)
    adj_in = [[] for _ in range(N_in + 1)]
    adj_out = [[] for _ in range(N_out + 1)]

    for idx, (u, v) in enumerate(edges):
        adj_in[u].append((v, idx))
        adj_out[v].append((u, idx))

    # current color of each edge, 0 = uncolored
    col = [0] * M

    # for each vertex, map color -> edge id that uses it
    used_in = [{} for _ in range(N_in + 1)]
    used_out = [{} for _ in range(N_out + 1)]

    # helper to get the opposite vertex
    def other(u_side, edge_id):
        u, v = edges[edge_id]
        return v if u_side == 0 else u  # 0: in, 1: out

    # DFS to free a color at a vertex
    def dfs(u, side, need_color, seen):
        key = (u, side)
        if key in seen:
            return False
        seen.add(key)

        # which dict to use
        used = used_in if side == 0 else used_out
        if need_color not in used[u]:
            return True  # free already

        e_id = used[u][need_color]
        w = other(side, e_id)          # neighbor vertex
        w_side = 1 - side

        # try to move this edge to another color
        for c in range(1, D + 1):
            if c == need_color:
                continue
            # check if c is free at both ends after potential move
            used_w = used_in if w_side == 0 else used_out
            if c in used_w[w]:
                continue
            # recurse: free c at u (current vertex) to allow moving edge
            if dfs(u, side, c, seen):
                # reassign edge e_id to color c
                col[e_id] = c
                # update structures
                del used[u][need_color]
                used[u][c] = e_id
                del used_w[w][c] if c in used_w[w] else None
                used_w[w][c] = e_id
                return True
        return False

    for idx, (u, v) in enumerate(edges):
        # try smallest free color at u
        used_u = used_in[u]
        used_v = used_out[v]
        for c in range(1, D + 1):
            if c not in used_u and c not in used_v:
                col[idx] = c
                used_u[c] = idx
                used_v[c] = idx
                break
        else:
            # need to recolor, pick any color missing at u
            for cu in range(1, D + 1):
                if cu not in used_u:
                    break
            # try to free cu at u by moving an existing edge
            seen = set()
            if dfs(u, 0, cu, seen):
                # now cu is free at u, assign it to current edge
                col[idx] = cu
                used_in[u][cu] = idx
                used_out[v][cu] = idx
            else:
                # fallback (should not happen per problem guarantee)
                for cv in range(1, D + 1):
                    if cv not in used_v:
                        break
                seen = set()
                if dfs(v, 1, cv, seen):
                    col[idx] = cv
                    used_in[u][cv] = idx
                    used_out[v][cv] = idx
                else:
                    # should never reach here
                    pass

    out = ['YES', ' '.join(map(str, col))]
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()