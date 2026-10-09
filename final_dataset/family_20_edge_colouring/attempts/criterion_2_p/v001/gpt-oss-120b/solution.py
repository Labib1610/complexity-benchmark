import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    nA = int(next(it))
    nB = int(next(it))
    m = int(next(it))
    edges = [(int(next(it)) - 1, int(next(it)) - 1) for _ in range(m)]

    degA = [0] * nA
    degB = [0] * nB
    for u, v in edges:
        degA[u] += 1
        degB[v] += 1
    Delta = max(max(degA, default=0), max(degB, default=0))

    # adjacency: for each vertex store {color: edge_id}
    usedA = [dict() for _ in range(nA)]
    usedB = [dict() for _ in range(nB)]
    # next free color pointer for each vertex
    nxtA = [1] * nA
    nxtB = [1] * nB

    ans = [0] * m

    # helper to get a free color for a vertex
    def free_color(used, nxt):
        while nxt[0] in used:
            nxt[0] += 1
        return nxt[0]

    # recursive recolor
    visited = [0] * (nA + nB)
    stamp = 1

    def dfs(u, need_color):
        nonlocal stamp
        if need_color not in usedA[u]:
            return True
        e = usedA[u][need_color]
        v = edges[e][1]
        if visited[nA + v] == stamp:
            return False
        visited[nA + v] = stamp
        # find a color free at v
        for c in range(1, Delta + 1):
            if c not in usedB[v]:
                # try to make v free c
                if dfsB(v, c):
                    # reassign edge e to color c
                    usedA[u].pop(need_color)
                    usedB[v][c] = e
                    usedA[u][c] = e
                    ans[e] = c
                    return True
        return False

    def dfsB(v, need_color):
        nonlocal stamp
        if need_color not in usedB[v]:
            return True
        e = usedB[v][need_color]
        u = edges[e][0]
        if visited[u] == stamp:
            return False
        visited[u] = stamp
        for c in range(1, Delta + 1):
            if c not in usedA[u]:
                if dfs(u, c):
                    usedB[v].pop(need_color)
                    usedA[u][c] = e
                    usedB[v][c] = e
                    ans[e] = c
                    return True
        return False

    for idx, (u, v) in enumerate(edges):
        # try to give a free color at u
        cu = free_color(usedA[u], [nxtA[u]])
        if cu not in usedB[v]:
            usedA[u][cu] = idx
            usedB[v][cu] = idx
            ans[idx] = cu
            continue
        # need recoloring
        stamp += 1
        if dfs(u, cu):
            continue
        # fallback (should not happen)
        print("NO")
        return

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()