import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * n
    domain = [7] * n  # bitmask of available colors: bit 0, 1, 2 (1, 2, 4)
    deg = [len(adj[i]) for i in range(n)]
    
    # Pre-check for self-loops (friction with oneself, though standard graphs don't have this)
    # Also handle components or general search
    
    popcount = [0, 1, 1, 2, 1, 2, 2, 3]

    max_c_used = -1

    def backtrack(assigned_count, max_c):
        if assigned_count == n:
            return True
        
        # Select unassigned vertex with minimum domain size (MRV)
        # Tie-breaker: maximum degree
        best_u = -1
        min_dom = 4
        max_d = -1
        
        for u in range(n):
            if color[u] == -1:
                d_size = popcount[domain[u]]
                if d_size < min_dom or (d_size == min_dom and deg[u] > max_d):
                    min_dom = d_size
                    max_d = deg[u]
                    best_u = u
                    if min_dom <= 1:
                        break
        
        if min_dom == 0:
            return False
        
        u = best_u
        u_domain = domain[u]
        
        # Try available colors for u
        for c in range(3):
            if not (u_domain & (1 << c)):
                continue
            if c > max_c + 1:
                continue
            
            # Try assigning color c to u
            color[u] = c
            
            # Forward check: remove c from neighbors' domains
            affected = []
            possible = True
            c_mask = ~(1 << c)
            for v in adj[u]:
                if color[v] == -1:
                    if domain[v] & (1 << c):
                        affected.append(v)
                        domain[v] &= c_mask
                        if domain[v] == 0:
                            possible = False
            
            if possible:
                if backtrack(assigned_count + 1, max(max_c, c)):
                    return True
            
            # Restore domains
            for v in affected:
                domain[v] |= (1 << c)
            color[u] = -1
        
        return False

    if backtrack(0, -1):
        print("YES")
        print(*(color[i] + 1 for i in range(n)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()