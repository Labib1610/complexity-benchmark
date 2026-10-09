import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    nL = int(next(it))
    nR = int(next(it))
    m = int(next(it))
    edges = []
    degL = [0] * (nL + 1)
    degR = [0] * (nR + 1)
    adjL = [[] for _ in range(nL + 1)]
    adjR = [[] for _ in range(nR + 1)]
    for idx in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        degL[u] += 1
        degR[v] += 1
        adjL[u].append(idx)
        adjR[v].append(idx)

    Delta = max(max(degL), max(degR))

    # for each vertex, map color -> edge index (only one edge per color)
    colL = [{} for _ in range(nL + 1)]
    colR = [{} for _ in range(nR + 1)]
    edge_color = [0] * m

    visited_edge = [0] * m
    stamp = 1

    def dfs(e_idx: int, wanted_color: int) -> bool:
        """try to place edge e_idx with wanted_color, possibly moving other edges."""
        nonlocal stamp
        if visited_edge[e_idx] == stamp:
            return False
        visited_edge[e_idx] = stamp
        u, v = edges[e_idx]

        # if the edge already has this color, done
        if edge_color[e_idx] == wanted_color:
            return True

        # check current occupancy
        occ_u = colL[u].get(wanted_color)
        occ_v = colR[v].get(wanted_color)

        if occ_u is None and occ_v is None:
            # free on both sides
            edge_color[e_idx] = wanted_color
            colL[u][wanted_color] = e_idx
            colR[v][wanted_color] = e_idx
            return True

        # try to push the occupying edge on u side
        if occ_u is not None:
            # try to find another color for occ_u
            for new_c in range(1, Delta + 1):
                if new_c == wanted_color:
                    continue
                if new_c not in colL[u] and new_c not in colR[edges[occ_u][1]]:
                    # can move directly
                    edge_color[occ_u] = new_c
                    colL[u][new_c] = occ_u
                    colR[edges[occ_u][1]][new_c] = occ_u
                    del colL[u][wanted_color]
                    del colR[v][wanted_color]
                    edge_color[e_idx] = wanted_color
                    colL[u][wanted_color] = e_idx
                    colR[v][wanted_color] = e_idx
                    return True
                # else try recursive move
                if new_c not in colL[u]:
                    stamp += 1
                    if dfs(occ_u, new_c):
                        del colL[u][wanted_color]
                        del colR[v][wanted_color]
                        edge_color[e_idx] = wanted_color
                        colL[u][wanted_color] = e_idx
                        colR[v][wanted_color] = e_idx
                        return True

        # try to push the occupying edge on v side
        if occ_v is not None:
            for new_c in range(1, Delta + 1):
                if new_c == wanted_color:
                    continue
                if new_c not in colR[v] and new_c not in colL[edges[occ_v][0]]:
                    edge_color[occ_v] = new_c
                    colR[v][new_c] = occ_v
                    colL[edges[occ_v][0]][new_c] = occ_v
                    del colL[u][wanted_color]
                    del colR[v][wanted_color]
                    edge_color[e_idx] = wanted_color
                    colL[u][wanted_color] = e_idx
                    colR[v][wanted_color] = e_idx
                    return True
                if new_c not in colR[v]:
                    stamp += 1
                    if dfs(occ_v, new_c):
                        del colL[u][wanted_color]
                        del colR[v][wanted_color]
                        edge_color[e_idx] = wanted_color
                        colL[u][wanted_color] = e_idx
                        colR[v][wanted_color] = e_idx
                        return True

        return False

    # main coloring loop
    for idx in range(m):
        if edge_color[idx]:
            continue
        u, v = edges[idx]
        # try colors 1..Delta
        for c in range(1, Delta + 1):
            if c not in colL[u] and c not in colR[v]:
                edge_color[idx] = c
                colL[u][c] = idx
                colR[v][c] = idx
                break
        else:
            # need to rearrange
            for c in range(1, Delta + 1):
                stamp += 1
                if dfs(idx, c):
                    break

    # output
    out = ['YES', ' '.join(str(edge_color[i]) for i in range(m))]
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()