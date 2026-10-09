import sys
sys.setrecursionlimit(10000)

def find_bridges(n, edges, adj):
    # Tarjan bridge finding
    visited = [False] * (n + 1)
    tin = [-1] * (n + 1)
    low = [-1] * (n + 1)
    timer = [0]
    bridges = set()

    def dfs(v, p_edge):
        visited[v] = True
        tin[v] = low[v] = timer[0]
        timer[0] += 1
        for to, eid in adj[v]:
            if eid == p_edge:
                continue
            if visited[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridges.add(eid)
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, -1)
    return bridges

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    edges = []
    adj = [[] for _ in range(n + 1)]
    for eid in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        adj[u].append((v, eid))
        adj[v].append((u, eid))

    # Check degree = 3
    for v in range(1, n + 1):
        if len(adj[v]) != 3:
            print("NO")
            return

    # Check bridges
    bridges = find_bridges(n, edges, adj)
    if bridges:
        print("NO")
        return

    # Backtracking search
    color = [-1] * m
    used_at_vertex = [0] * (n + 1)  # bitmask of colors used

    # degree left = 3 - assigned count
    deg_left = [3] * (n + 1)

    def get_choices(edge_idx):
        u, v = edges[edge_idx]
        used_mask = used_at_vertex[u] | used_at_vertex[v]
        choices = []
        for c in (1, 2, 3):
            if not (used_mask & (1 << c)):
                choices.append(c)
        return choices

    # Heuristic: choose edge with fewest choices
    import heapq
    # We'll maintain a list of unassigned edges and pick next each time
    unassigned = list(range(m))
    
    def backtrack():
        if not unassigned:
            return True
        # Find edge with minimum choices
        best_e = -1
        best_cnt = 10
        best_choices = None
        for eid in unassigned:
            ch = get_choices(eid)
            if len(ch) == 0:
                return False
            if len(ch) < best_cnt:
                best_cnt = len(ch)
                best_e = eid
                best_choices = ch
                if best_cnt == 1:
                    break
        eid = best_e
        u, v = edges[eid]
        for c in best_choices:
            # place
            color[eid] = c
            used_at_vertex[u] |= (1 << c)
            used_at_vertex[v] |= (1 << c)
            deg_left[u] -= 1
            deg_left[v] -= 1
            unassigned.remove(eid)
            # check if any vertex's remaining degree <= used colors left
            ok = True
            for x in (u, v):
                if deg_left[x] < 0:
                    ok = False
                    break
                # count available colors for this vertex
                avail = 3 - bin(used_at_vertex[x]).count("1")
                if deg_left[x] > avail:
                    ok = False
                    break
            if ok:
                if backtrack():
                    return True
            # undo
            unassigned.append(eid)
            deg_left[u] += 1
            deg_left[v] += 1
            used_at_vertex[u] &= ~(1 << c)
            used_at_vertex[v] &= ~(1 << c)
            color[eid] = -1
        return False

    if backtrack():
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()