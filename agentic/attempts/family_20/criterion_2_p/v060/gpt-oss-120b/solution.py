import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    import sys
    input = sys.stdin.readline
    nT, nP, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    degT = [0] * (nT + 1)
    degP = [0] * (nP + 1)
    for u, v in edges:
        degT[u] += 1
        degP[v] += 1
    K = max(max(degT), max(degP), 1)

    # adjacency with edge indices
    adjT = [[] for _ in range(nT + 1)]
    adjP = [[] for _ in range(nP + 1)]
    for idx, (u, v) in enumerate(edges):
        adjT[u].append((v, idx))
        adjP[v].append((u, idx))

    # color assignment, -1 uncolored
    col = [-1] * m

    # For each vertex keep set of used colors (as bitset via list of bool)
    usedT = [set() for _ in range(nT + 1)]
    usedP = [set() for _ in range(nP + 1)]

    # simple greedy with recoloring via DFS (alternating path)
    def dfs(u, target_color, visited):
        # try to recolor an edge incident to u (translator side)
        for v, eid in adjT[u]:
            if col[eid] == target_color:
                continue
            if col[eid] == -1:
                # free edge, assign
                col[eid] = target_color
                usedT[u].add(target_color)
                usedP[v].add(target_color)
                return True
            # edge has some other color c2, try to move it
            c2 = col[eid]
            if (u, c2) in visited:
                continue
            visited.add((u, c2))
            # find alternative color for this edge at the other endpoint
            if dfs(v, c2, visited):
                # now we can set current edge to target_color
                col[eid] = target_color
                usedT[u].add(target_color)
                usedP[v].add(target_color)
                usedT[u].discard(c2)
                usedP[v].discard(c2)
                return True
        return False

    # Process edges one by one
    for idx, (u, v) in enumerate(edges):
        # find smallest available color for this edge
        for c in range(1, K + 1):
            if c not in usedT[u] and c not in usedP[v]:
                col[idx] = c
                usedT[u].add(c)
                usedP[v].add(c)
                break
        else:
            # need recoloring
            for c in range(1, K + 1):
                if c in usedT[u]:
                    continue
                # try to free color c at v via alternating path
                visited = set()
                if dfs(v, c, visited):
                    col[idx] = c
                    usedT[u].add(c)
                    usedP[v].add(c)
                    break

    print("YES")
    print(' '.join(map(str, col)))

if __name__ == "__main__":
    solve()