import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    nL = int(next(it))
    nR = int(next(it))
    m = int(next(it))

    edges = []
    degL = [0] * (nL + 1)
    degR = [0] * (nR + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        degL[u] += 1
        degR[v] += 1

    Δ = 0
    for d in degL[1:]:
        if d > Δ:
            Δ = d
    for d in degR[1:]:
        if d > Δ:
            Δ = d

    # colour of each edge (0 = not coloured yet)
    col_edge = [0] * m

    # for each vertex: colour -> edge id
    col_at_L = [{} for _ in range(nL + 1)]
    col_at_R = [{} for _ in range(nR + 1)]

    # helper to get structures by side
    def get_maps(side, idx):
        return (col_at_L, col_at_R)[side][idx]

    # DFS to make colour c free at vertex (side, idx)
    visited = [0] * (nL + nR + 2)
    stamp = 1

    def dfs(side, idx, c):
        nonlocal stamp
        vid = idx if side == 0 else nL + idx
        if visited[vid] == stamp:
            return False
        visited[vid] = stamp
        mp = get_maps(side, idx)
        if c not in mp:          # colour already free
            return True
        e_id = mp[c]             # edge that currently uses colour c
        u, v = edges[e_id]
        # opposite vertex
        if side == 0:
            nside, nidx = 1, v
        else:
            nside, nidx = 0, u
        # try to move this edge to another colour
        # iterate over colours not used at current vertex
        used_here = mp.keys()
        for c2 in range(1, Δ + 1):
            if c2 == c:
                continue
            if c2 in used_here:
                continue
            stamp += 1
            if dfs(nside, nidx, c2):
                # recolour edge e_id to c2
                mp.pop(c)
                get_maps(nside, nidx)[c2] = e_id
                col_at_L[u][c2] = e_id if side == 0 else col_at_R[v][c2] = e_id
                col_edge[e_id] = c2
                return True
        return False

    for eid, (u, v) in enumerate(edges):
        # find a colour free at u
        used_u = col_at_L[u]
        for c in range(1, Δ + 1):
            if c not in used_u:
                break
        # try to assign c to (u,v)
        if c not in col_at_R[v]:
            # free at both ends
            col_at_L[u][c] = eid
            col_at_R[v][c] = eid
            col_edge[eid] = c
            continue
        # need to free c at v
        stamp += 1
        if not dfs(1, v, c):
            # according to theorem this never happens
            print("NO")
            return
        # now c is free at v
        col_at_L[u][c] = eid
        col_at_R[v][c] = eid
        col_edge[eid] = c

    out = ['YES', ' '.join(map(str, col_edge))]
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()