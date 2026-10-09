import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    nP = int(next(it))
    nS = int(next(it))
    m = int(next(it))
    U = [0] * m
    V = [0] * m
    degP = [0] * (nP + 1)
    degS = [0] * (nS + 1)
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        U[i] = u
        V[i] = v
        degP[u] += 1
        degS[v] += 1
    Delta = 0
    for d in degP[1:]:
        if d > Delta:
            Delta = d
    for d in degS[1:]:
        if d > Delta:
            Delta = d
    # structures
    # for each vertex store dict color->edge
    col_edge_P = [{} for _ in range(nP + 1)]
    col_edge_S = [{} for _ in range(nS + 1)]
    # edge colors, 0 = uncolored
    edge_col = [0] * m

    # helper to get dict for a vertex
    def get_dict(isP, idx):
        return col_edge_P[idx] if isP else col_edge_S[idx]

    # find smallest free color for a vertex
    def first_free(col_dict):
        # colors are 1..Delta, we can keep a pointer per vertex
        # but Delta up to 1e5, linear scan acceptable overall because total scans = O(m*Δ) worst.
        # Use while loop with stored pointer
        ptr = col_dict.get('_ptr', 1)
        while ptr in col_dict:
            ptr += 1
        col_dict['_ptr'] = ptr
        return ptr

    for i in range(m):
        u = U[i]
        v = V[i]
        dict_u = col_edge_P[u]
        dict_v = col_edge_S[v]

        c_u = first_free(dict_u)
        c_v = first_free(dict_v)

        if c_u == c_v:
            col = c_u
            edge_col[i] = col
            dict_u[col] = i
            dict_v[col] = i
            continue

        # we will try to recolor using colors c_u and c_v
        # start from u with color c_u, aim to free c_u at v
        cur_vertex = u
        cur_isP = True
        cur_color = c_u
        other_color = c_v

        while True:
            # if the opposite vertex (v) has free other_color, we can place the original edge
            if cur_isP:
                opp_dict = col_edge_S[v]
                opp_free = first_free(opp_dict)
                if opp_free == other_color:
                    # assign original edge
                    edge_col[i] = other_color
                    dict_u[other_color] = i
                    opp_dict[other_color] = i
                    break
            else:
                opp_dict = col_edge_P[u]
                opp_free = first_free(opp_dict)
                if opp_free == other_color:
                    edge_col[i] = other_color
                    dict_v[other_color] = i
                    opp_dict[other_color] = i
                    break

            # there is an edge incident to cur_vertex with cur_color
            cur_dict = dict_u if cur_isP else dict_v
            e_idx = cur_dict[cur_color]          # existing edge with this color
            # recolor that edge to other_color
            edge_col[e_idx] = other_color
            # update mappings for its two endpoints
            eu = U[e_idx]
            ev = V[e_idx]
            d_u = col_edge_P[eu]
            d_v = col_edge_S[ev]
            # remove old color entry
            del d_u[cur_color]
            del d_v[cur_color]
            # add new color entry
            d_u[other_color] = e_idx
            d_v[other_color] = e_idx

            # move to the other endpoint of that edge
            if cur_isP:
                cur_vertex = ev
                cur_isP = False
            else:
                cur_vertex = eu
                cur_isP = True
            # swap colors for next step
            cur_color, other_color = other_color, cur_color

    # all edges colored
    out = ['YES', '\n', ' '.join(str(c) for c in edge_col)]
    sys.stdout.write(''.join(out))

if __name__ == "__main__":
    solve()