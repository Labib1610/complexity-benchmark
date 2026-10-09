import sys

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    edges = []
    adj_edges = [[] for _ in range(n + 1)]
    
    idx = 2
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        edges.append((u, v))
        adj_edges[u].append(i)
        adj_edges[v].append(i)
        
    # Check if graph is bipartite
    color_v = [-1] * (n + 1)
    is_bipartite = True
    for start in range(1, n + 1):
        if color_v[start] == -1:
            color_v[start] = 0
            q = [start]
            while q:
                u = q.pop()
                for e_idx in adj_edges[u]:
                    v = edges[e_idx][0] if edges[e_idx][1] == u else edges[e_idx][1]
                    if color_v[v] == -1:
                        color_v[v] = 1 - color_v[u]
                        q.append(v)
                    elif color_v[v] == color_v[u]:
                        is_bipartite = False
                        break
                if not is_bipartite:
                    break
        if not is_bipartite:
            break
            
    if is_bipartite:
        # Bipartite 3-regular graph is always 3-edge-colorable.
        # Step 1: Find a perfect matching using Hopcroft-Karp / Dinic
        # Left vertices: color_v == 0, Right vertices: color_v == 1
        left = [i for i in range(1, n + 1) if color_v[i] == 0]
        
        pair_u = [0] * (n + 1)
        pair_v = [0] * (n + 1)
        dist = [0] * (n + 1)
        
        def bfs():
            q = []
            for u in left:
                if pair_u[u] == 0:
                    dist[u] = 0
                    q.append(u)
                else:
                    dist[u] = float('inf')
            dist[0] = float('inf')
            head = 0
            while head < len(q):
                u = q[head]
                head += 1
                if dist[u] < dist[0]:
                    for e_idx in adj_edges[u]:
                        v = edges[e_idx][0] if edges[e_idx][1] == u else edges[e_idx][1]
                        if dist[pair_v[v]] == float('inf'):
                            dist[pair_v[v]] = dist[u] + 1
                            q.append(pair_v[v])
            return dist[0] != float('inf')

        def dfs(u):
            if u != 0:
                for e_idx in adj_edges[u]:
                    v = edges[e_idx][0] if edges[e_idx][1] == u else edges[e_idx][1]
                    if dist[pair_v[v]] == dist[u] + 1:
                        if dfs(pair_v[v]):
                            pair_v[v] = u
                            pair_u[u] = v
                            return True
                dist[u] = float('inf')
                return False
            return True

        matching = 0
        while bfs():
            for u in left:
                if pair_u[u] == 0:
                    if dfs(u):
                        matching += 1
                        
        # Shift 1: The edges in the matching
        ans = [0] * m
        matched_edges = set()
        for u in left:
            v = pair_u[u]
            for e_idx in adj_edges[u]:
                if (edges[e_idx][0] == u and edges[e_idx][1] == v) or (edges[e_idx][0] == v and edges[e_idx][1] == u):
                    ans[e_idx] = 1
                    matched_edges.add(e_idx)
                    break
                    
        # The remaining edges form a 2-factor (collection of cycles of even length)
        # 2-color each cycle with shifts 2 and 3
        rem_adj = [[] for _ in range(n + 1)]
        for i in range(m):
            if i not in matched_edges:
                u, v = edges[i]
                rem_adj[u].append((v, i))
                rem_adj[v].append((u, i))
                
        visited_edge = [False] * m
        for start in range(1, n + 1):
            for neighbor, e_idx in rem_adj[start]:
                if not visited_edge[e_idx]:
                    # Trace cycle
                    cur = start
                    cur_e = e_idx
                    col = 2
                    while not visited_edge[cur_e]:
                        visited_edge[cur_e] = True
                        ans[cur_e] = col
                        col = 3 if col == 2 else 2
                        nxt = edges[cur_e][0] if edges[cur_e][1] == cur else edges[cur_e][1]
                        cur = nxt
                        # find next edge
                        for nxt_neighbor, nxt_e in rem_adj[cur]:
                            if not visited_edge[nxt_e]:
                                cur_e = nxt_e
                                break
                                
        print("YES")
        print(*(ans))
        return

    # If not bipartite, use MRV Backtracking with constraint propagation
    # Build incident edges for each edge
    adj_for_edge = [[] for _ in range(m)]
    for u in range(1, n + 1):
        for e1 in adj_edges[u]:
            for e2 in adj_edges[u]:
                if e1 != e2:
                    adj_for_edge[e1].append(e2)
    for i in range(m):
        adj_for_edge[i] = list(set(adj_for_edge[i]))
        
    mask = [7] * m  # 7 is binary 111 (colors 1, 2, 3 available)
    ans = [0] * m

    def solve_general():
        # Find unassigned edge with minimum remaining values
        min_c = 4
        best_e = -1
        for i in range(m):
            if ans[i] == 0:
                c = bin(mask[i]).count('1')
                if c == 0:
                    return False
                if c < min_c:
                    min_c = c
                    best_e = i
                    if min_c == 1:
                        break
        
        if best_e == -1:
            return True
            
        avail = mask[best_e]
        for color in (1, 2, 3):
            if avail & (1 << (color - 1)):
                # Try assigning color
                ans[best_e] = color
                changes = []
                conflict = False
                for neighbor in adj_for_edge[best_e]:
                    if ans[neighbor] == 0:
                        if mask[neighbor] & (1 << (color - 1)):
                            mask[neighbor] &= ~(1 << (color - 1))
                            changes.append(neighbor)
                            if mask[neighbor] == 0:
                                conflict = True
                
                if not conflict:
                    if solve_general():
                        return True
                        
                # Backtrack
                for neighbor in changes:
                    mask[neighbor] |= (1 << (color - 1))
                ans[best_e] = 0
                
        return False

    if solve_general():
        print("YES")
        print(*(ans))
    else:
        print("NO")

if __name__ == '__main__':
    solve()