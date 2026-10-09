import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    adj = [0] * n
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        idx += 2
        if u != v:
            adj[u] |= (1 << v)
            adj[v] |= (1 << u)
            
    # Check for self-loops
    # Problem says pairs, but if u == v was possible, it's handled or impossible if conflict with self.
    
    domains = [7] * n  # 7 = 0b111 (colors 1, 2, 3)
    color = [0] * n
    degree = [bin(adj[i]).count('1') for i in range(n)]
    
    # Precompute popcounts for masks 0..7
    popcnt = [0, 1, 1, 2, 1, 2, 2, 3]
    
    # Backtracking with MRV (Minimum Remaining Values)
    def backtrack(assigned_count):
        if assigned_count == n:
            return True
        
        # Find unassigned vertex with minimum domain size
        best_u = -1
        min_dom = 4
        max_deg = -1
        
        for u in range(n):
            if color[u] == 0:
                sz = popcnt[domains[u]]
                if sz < min_dom or (sz == min_dom and degree[u] > max_deg):
                    min_dom = sz
                    max_deg = degree[u]
                    best_u = u
                    if min_dom == 1:
                        break
        
        if min_dom == 0:
            return False
        
        u = best_u
        mask = domains[u]
        
        # Try available colors
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if mask & bit:
                color[u] = c
                # Forward checking
                changed = []
                valid = True
                u_adj = adj[u]
                
                # Check neighbors
                for v in range(n):
                    if (u_adj & (1 << v)) and color[v] == 0:
                        if domains[v] & bit:
                            domains[v] ^= bit
                            changed.append(v)
                            if domains[v] == 0:
                                valid = False
                
                if valid:
                    if backtrack(assigned_count + 1):
                        return True
                
                # Restore domains
                for v in changed:
                    domains[v] |= bit
                color[u] = 0
                
        return False

    if backtrack(0):
        print("YES")
        print(*(color[i] for i in range(n)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()