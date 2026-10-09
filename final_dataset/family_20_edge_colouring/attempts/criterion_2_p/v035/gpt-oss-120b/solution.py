import sys
sys.setrecursionlimit(1 << 25)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    nL = int(next(it)); nR = int(next(it)); m = int(next(it))
    edges = [(int(next(it)) - 1, int(next(it)) - 1) for _ in range(m)]

    # compute degrees and Δ
    degL = [0] * nL
    degR = [0] * nR
    for u, v in edges:
        degL[u] += 1
        degR[v] += 1
    k = max(max(degL) if nL else 0, max(degR) if nR else 0)
    if k == 0:
        print("YES")
        print()
        return

    # adjacency: for each vertex store dict color->edge id
    col_edge_L = [dict() for _ in range(nL)]
    col_edge_R = [dict() for _ in range(nR)]
    # current color of each edge, 0 means uncolored
    edge_color = [0] * m

    # helper to find smallest unused color at a vertex
    def smallest_unused(used_dict):
        c = 1
        while c in used_dict:
            c += 1
        return c

    # recursive function to make color c free at vertex v
    def make_free(v, side, c, visited):
        # side 0 = left, 1 = right
        key = (v, side, c)
        if key in visited:
            return False
        visited.add(key)

        used = col_edge_L[v] if side == 0 else col_edge_R[v]
        if c not in used:
            return True
        e = used[c]
        u, w = edges[e]
        other_v = w if side == 0 else u
        other_side = 1 - side

        # try to move this edge to another color
        for nc in range(1, k + 1):
            if nc == c:
                continue
            used_other = col_edge_L[other_v] if other_side == 0 else col_edge_R[other_v]
            if nc not in used_other:
                # reassign edge e to nc
                # remove old
                del used[c]
                del used_other[c] if c in used_other else None
                # assign new
                used[nc] = e
                used_other[nc] = e
                edge_color[e] = nc
                return True

        # try to free nc recursively
        for nc in range(1, k + 1):
            if nc == c:
                continue
            used_other = col_edge_L[other_v] if other_side == 0 else col_edge_R[other_v]
            if nc in used_other:
                if make_free(other_v, other_side, nc, visited):
                    # now nc is free at other_v, reassign
                    del used[c]
                    used[nc] = e
                    used_other[nc] = e
                    edge_color[e] = nc
                    return True
        return False

    for idx, (u, v) in enumerate(edges):
        # find smallest unused colors at both ends
        c1 = smallest_unused(col_edge_L[u])
        c2 = smallest_unused(col_edge_R[v])
        if c1 == c2:
            col_edge_L[u][c1] = idx
            col_edge_R[v][c1] = idx
            edge_color[idx] = c1
        else:
            # try to assign c1, freeing it at v if needed
            if c1 not in col_edge_R[v]:
                col_edge_L[u][c1] = idx
                col_edge_R[v][c1] = idx
                edge_color[idx] = c1
            else:
                visited = set()
                if make_free(v, 1, c1, visited):
                    col_edge_L[u][c1] = idx
                    col_edge_R[v][c1] = idx
                    edge_color[idx] = c1
                else:
                    # fallback assign c2 (symmetrically)
                    visited = set()
                    if make_free(u, 0, c2, visited):
                        col_edge_L[u][c2] = idx
                        col_edge_R[v][c2] = idx
                        edge_color[idx] = c2
                    else:
                        # should not happen as per problem guarantee
                        print("NO")
                        return

    print("YES")
    print(' '.join(map(str, edge_color)))

if __name__ == "__main__":
    main()