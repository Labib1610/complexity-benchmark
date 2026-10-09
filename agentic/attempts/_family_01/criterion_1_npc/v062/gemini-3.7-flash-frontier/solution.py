import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj_mat = [[False] * n for _ in range(n)]
    adj = [set() for _ in range(n)]
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        if u != v and not adj_mat[u][v]:
            adj_mat[u][v] = adj_mat[v][u] = True
            adj[u].add(v)
            adj[v].add(u)
            
    # Degree <= 2 reduction
    degree = [len(adj[i]) for i in range(n)]
    active = [True] * n
    stack = []
    
    q = [i for i in range(n) if degree[i] <= 2]
    head = 0
    while head < len(q):
        u = q[head]
        head += 1
        if not active[u]:
            continue
        active[u] = False
        neighbors = [v for v in adj[u] if active[v]]
        stack.append((u, neighbors))
        for v in neighbors:
            degree[v] -= 1
            if degree[v] <= 2 and active[v]:
                q.append(v)
                
    remaining_vertices = [i for i in range(n) if active[i]]
    rem_n = len(remaining_vertices)
    rem_id = {v: i for i, v in enumerate(remaining_vertices)}
    
    rem_adj = [[] for _ in range(rem_n)]
    for u in remaining_vertices:
        for v in adj[u]:
            if active[v]:
                rem_adj[rem_id[u]].append(rem_id[v])
                
    # MRV + Forward Checking on remaining graph
    # Colors: 0 (bit 1), 1 (bit 2), 2 (bit 4), mask = 7
    color_assignment = [-1] * rem_n
    domain = [7] * rem_n # bitmask of available colors (1, 2, 4)
    
    def backtrack():
        # Find unassigned vertex with minimum remaining values
        min_rem = 4
        best_v = -1
        for i in range(rem_n):
            if color_assignment[i] == -1:
                mask = domain[i]
                cnt = bin(mask).count('1')
                if cnt == 0:
                    return False
                if cnt < min_rem:
                    min_rem = cnt
                    best_v = i
                    if cnt == 1:
                        break
                        
        if best_v == -1:
            return True
            
        cand_mask = domain[best_v]
        for c in range(3):
            bit = 1 << c
            if cand_mask & bit:
                color_assignment[best_v] = c
                # Save affected domains
                affected = []
                conflict = False
                for nei in rem_adj[best_v]:
                    if color_assignment[nei] == -1 and (domain[nei] & bit):
                        domain[nei] ^= bit
                        affected.append(nei)
                        if domain[nei] == 0:
                            conflict = True
                            
                if not conflict and backtrack():
                    return True
                    
                # Restore
                for nei in affected:
                    domain[nei] |= bit
                color_assignment[best_v] = -1
                
        return False

    if not backtrack():
        print("NO")
        return
        
    full_colors = [-1] * n
    for i, v in enumerate(remaining_vertices):
        full_colors[v] = color_assignment[i] + 1
        
    # Reconstruct for eliminated vertices
    while stack:
        u, neighbors = stack.pop()
        used = {full_colors[v] for v in neighbors if full_colors[v] != -1}
        for c in (1, 2, 3):
            if c not in used:
                full_colors[u] = c
                break
                
    print("YES")
    print(*(full_colors[i] for i in range(n)))

if __name__ == '__main__':
    solve()