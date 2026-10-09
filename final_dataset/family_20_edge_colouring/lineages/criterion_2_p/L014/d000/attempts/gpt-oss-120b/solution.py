import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N1 = int(next(it))
    N2 = int(next(it))
    M = int(next(it))
    edges = [(int(next(it)) - 1, int(next(it)) - 1) for _ in range(M)]

    deg1 = [0] * N1
    deg2 = [0] * N2
    for u, v in edges:
        deg1[u] += 1
        deg2[v] += 1
    K = max(max(deg1) if N1 else 0, max(deg2) if N2 else 0)

    # adjacency lists of incident edge indices
    adj1 = [[] for _ in range(N1)]
    adj2 = [[] for _ in range(N2)]
    for idx, (u, v) in enumerate(edges):
        adj1[u].append(idx)
        adj2[v].append(idx)

    # colors used at each vertex, stored as dict color->edge idx
    col1 = [{} for _ in range(N1)]
    col2 = [{} for _ in range(N2)]
    ans = [0] * M

    # helper to find a free color for a vertex
    def free_color(col_dict, max_c):
        for c in range(1, max_c + 1):
            if c not in col_dict:
                return c
        return max_c + 1  # should not happen

    # augmenting path DFS
    def dfs(u, target_color, visited_u, visited_v):
        # u is a primary vertex
        visited_u.add(u)
        # try to take an edge incident to u that is colored with target_color
        if target_color in col1[u]:
            e = col1[u][target_color]
            v = edges[e][1]
            if v in visited_v:
                return False
            visited_v.add(v)
            # try to recolor this edge with some other free color at v
            for c in range(1, K + 1):
                if c == target_color:
                    continue
                if c not in col2[v]:
                    # recolor edge e to c
                    del col1[u][target_color]
                    col1[u][c] = e
                    del col2[v][target_color]
                    col2[v][c] = e
                    ans[e] = c
                    return True
            # otherwise, try to move further
            for c in range(1, K + 1):
                if c == target_color:
                    continue
                if c in col2[v]:
                    e2 = col2[v][c]
                    u2 = edges[e2][0]
                    if u2 not in visited_u:
                        if dfs(u2, target_color, visited_u, visited_v):
                            # after recursion, recolor e to c
                            del col1[u][target_color]
                            col1[u][c] = e
                            del col2[v][target_color]
                            col2[v][c] = e
                            ans[e] = c
                            return True
            return False
        else:
            return True  # free at u

    for idx, (u, v) in enumerate(edges):
        # try to assign smallest possible color
        for c in range(1, K + 1):
            if c not in col1[u] and c not in col2[v]:
                col1[u][c] = idx
                col2[v][c] = idx
                ans[idx] = c
                break
        else:
            # need to recolor using augmenting path
            # find a color missing at u
            for c in range(1, K + 1):
                if c not in col1[u]:
                    missing_u = c
                    break
            # find a color missing at v
            for c in range(1, K + 1):
                if c not in col2[v]:
                    missing_v = c
                    break
            # we will try to make missing_u also missing at v via augmenting path
            visited_u = set()
            visited_v = set()
            if dfs(u, missing_u, visited_u, visited_v):
                # now missing_u is free at both ends
                col1[u][missing_u] = idx
                col2[v][missing_u] = idx
                ans[idx] = missing_u
            else:
                # fallback (should not happen)
                col1[u][missing_v] = idx
                col2[v][missing_v] = idx
                ans[idx] = missing_v

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()