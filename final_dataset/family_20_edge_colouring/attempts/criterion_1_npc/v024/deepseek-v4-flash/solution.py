import sys
sys.setrecursionlimit(1000000)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    adj = [[] for _ in range(n)]
    for idx in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        adj[u].append((v, idx))
        adj[v].append((u, idx))
    
    # Tarjan to find bridges
    tin = [-1]*n
    low = [-1]*n
    timer = 0
    is_bridge = [False]*m
    
    def dfs(v, p_edge):
        nonlocal timer
        tin[v] = low[v] = timer
        timer += 1
        for to, eid in adj[v]:
            if eid == p_edge:
                continue
            if tin[to] != -1:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    is_bridge[eid] = True
    
    for i in range(n):
        if tin[i] == -1:
            dfs(i, -1)
    
    if any(is_bridge):
        print("NO")
        return
    
    # Find perfect matching
    match_u = [-1]*n
    match_v = [-1]*n
    
    def try_kuhn(v, used):
        for to, eid in adj[v]:
            if match_u[to] == -1:
                match_u[to] = v
                match_v[v] = to
                return True
        for to, eid in adj[v]:
            if not used[to]:
                used[to] = True
                if match_u[to] != -1 and try_kuhn(match_u[to], used):
                    match_u[to] = v
                    match_v[v] = to
                    return True
        return False
    
    # Since the graph is cubic and bridgeless, perfect matching exists.
    # Simple augmenting path algorithm on general graph (not bipartite).
    # Use simple DFS-based matching for undirected graph.
    def augment(v, visited):
        visited[v] = True
        for to, eid in adj[v]:
            if match_v[to] == -1:
                match_v[v] = to
                match_v[to] = v
                return True
            if not visited[to]:
                if augment(to, visited):
                    match_v[v] = to
                    match_v[to] = v
                    return True
        return False
    
    for i in range(n):
        if match_v[i] == -1:
            visited = [False]*n
            augment(i, visited)
    
    # After matching, match_v contains the matched partner
    color = [0]*m
    # color matching edges with 3
    for i in range(n):
        j = match_v[i]
        if j > i:
            for to, eid in adj[i]:
                if to == j:
                    color[eid] = 3
                    break
    
    # remaining edges form cycles
    visited_edge = [False]*m
    for i in range(n):
        for to, eid in adj[i]:
            if color[eid] != 0:
                continue
            # start new cycle
            if not visited_edge[eid]:
                # traverse cycle
                cur_v = i
                prev_e = -1
                col = 1
                while True:
                    for nxt, eid2 in adj[cur_v]:
                        if eid2 == prev_e:
                            continue
                        if color[eid2] == 0:
                            color[eid2] = col
                            visited_edge[eid2] = True
                            prev_e = eid2
                            col = 3 - col  # switch between 1 and 2
                            cur_v = nxt
                            break
                    else:
                        break
                    if cur_v == i and prev_e == eid:
                        break
    
    # output
    print("YES")
    print(' '.join(str(color[i]) for i in range(m)))

if __name__ == "__main__":
    solve()