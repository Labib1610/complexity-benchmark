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

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        degL[u] += 1
        degR[v] += 1

    K = 0
    for d in degL[1:]:
        if d > K:
            K = d
    for d in degR[1:]:
        if d > K:
            K = d

    # colour maps
    colL = [dict() for _ in range(nL + 1)]
    colR = [dict() for _ in range(nR + 1)]

    ans = [0] * m

    # auxiliary structures for DFS
    visited = set()

    def dfs(u, want_c):
        """try to make colour want_c free at vertex u, returns True/False"""
        key = (u, want_c)
        if key in visited:
            return False
        visited.add(key)

        # if free already
        if u <= nL:
            if want_c not in colL[u]:
                return True
            e_id = colL[u][want_c]
            x, y = edges[e_id]
        else:
            v = u - nL
            if want_c not in colR[v]:
                return True
            e_id = colR[v][want_c]
            x, y = edges[e_id]

        # opposite vertex
        other = y if x == u else x
        # try to move this edge to another colour
        for c2 in range(1, K + 1):
            if c2 == want_c:
                continue
            # is c2 free at other?
            if other <= nL:
                if c2 not in colL[other]:
                    # recolour edge e_id to c2
                    # remove old
                    if u <= nL:
                        del colL[u][want_c]
                    else:
                        del colR[u - nL][want_c]
                    # add new
                    colL[other][c2] = e_id
                    colR[edges[e_id][1]][c2] = e_id
                    ans[e_id] = c2
                    return True
            else:
                if c2 not in colR[other - nL]:
                    # recolour
                    if u <= nL:
                        del colL[u][want_c]
                    else:
                        del colR[u - nL][want_c]
                    colR[other - nL][c2] = e_id
                    colL[edges[e_id][0]][c2] = e_id
                    ans[e_id] = c2
                    return True
            # otherwise c2 occupied at other, try to push further
            if dfs(other, c2):
                # now c2 is free at other, recolour
                if u <= nL:
                    del colL[u][want_c]
                else:
                    del colR[u - nL][want_c]
                colL[other][c2] = e_id
                colR[edges[e_id][1]][c2] = e_id
                ans[e_id] = c2
                return True
        return False

    for idx, (u, v) in enumerate(edges):
        # try smallest free colour at both ends
        found = False
        for c in range(1, K + 1):
            if c not in colL[u] and c not in colR[v]:
                colL[u][c] = idx
                colR[v][c] = idx
                ans[idx] = c
                found = True
                break
        if found:
            continue

        # pick a colour free at u (there is at least one)
        for c in range(1, K + 1):
            if c not in colL[u]:
                target_c = c
                break

        visited.clear()
        # free target_c at v
        dfs(v, target_c)

        # now it is free at both ends
        colL[u][target_c] = idx
        colR[v][target_c] = idx
        ans[idx] = target_c

    out = ['YES', ' '.join(map(str, ans))]
    sys.stdout.write('\n'.join(out))

if __name__ == '__main__':
    solve()