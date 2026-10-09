import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    nG = int(next(it))
    nA = int(next(it))
    m = int(next(it))

    edges = []
    deg = [0] * (nG + nA)
    for _ in range(m):
        u = int(next(it)) - 1          # generators 0..nG-1
        v = int(next(it)) - 1 + nG     # analyzers shifted
        edges.append((u, v))
        deg[u] += 1
        deg[v] += 1

    K = max(deg) if m else 0

    # for each vertex: colour -> edge id
    used = [{} for _ in range(nG + nA)]

    col_edge = [0] * m

    # DFS that tries to free colour c at vertex x
    def dfs(x: int, c: int, seen: set) -> bool:
        if c not in used[x]:
            return True
        if x in seen:
            return False
        seen.add(x)
        e_id = used[x][c]
        u, v = edges[e_id]
        other = v if x == u else u
        # try every colour that is free at 'other'
        for c2 in range(1, K + 1):
            if c2 == c:
                continue
            if c2 in used[other]:
                continue
            if dfs(other, c2, seen):
                # recolour edge e_id from c to c2
                used[other][c2] = e_id
                used[x].pop(c)
                return True
        return False

    for idx, (u, v) in enumerate(edges):
        for c in range(1, K + 1):
            if c not in used[u] and c not in used[v]:
                col_edge[idx] = c
                used[u][c] = idx
                used[v][c] = idx
                break
            if c not in used[u]:
                # free at u, occupied at v
                if dfs(v, c, set()):
                    col_edge[idx] = c
                    used[u][c] = idx
                    used[v][c] = idx
                    break
            # symmetric case will be handled when the loop reaches a colour
            # that is free at v but not at u
        else:
            # should never happen because K = Δ guarantees a colour
            print("NO")
            return

    out = ['YES\n', ' '.join(map(str, col_edge))]
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()