import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [0] * n
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        if u != v:
            adj[u] |= (1 << v)
            adj[v] |= (1 << u)
            
    # Check for self-loops (handled by u != v, but if u == v original constraint is impossible)
    # The problem statement says simple graph since m <= n(n-1)/2.

    # 3-coloring using DSATUR / MRV
    # Colors will be 1, 2, 4 (bitmask of used colors)
    color = [0] * n
    forbidden = [0] * n  # mask of forbidden colors for each vertex

    def get_best_vertex():
        best_v = -1
        min_avail = 4
        max_deg = -1
        
        for i in range(n):
            if color[i] == 0:
                # number of available colors = 3 - popcount(forbidden[i])
                avail = 3 - bin(forbidden[i]).count('1')
                if avail < min_avail:
                    min_avail = avail
                    best_v = i
                    max_deg = bin(adj[i]).count('1')
                elif avail == min_avail:
                    deg = bin(adj[i]).count('1')
                    if deg > max_deg:
                        max_deg = deg
                        best_v = i
        return best_v, min_avail

    def backtrack(assigned_count):
        if assigned_count == n:
            return True
        
        v, avail = get_best_vertex()
        if avail == 0:
            return False
        
        for c in (1, 2, 4):
            if not (forbidden[v] & c):
                color[v] = c
                # Update forbidden for neighbors
                changed = []
                mask = adj[v]
                while mask > 0:
                    u = (mask & -mask).bit_length() - 1
                    mask &= mask - 1
                    if color[u] == 0 and not (forbidden[u] & c):
                        forbidden[u] |= c
                        changed.append(u)
                
                if backtrack(assigned_count + 1):
                    return True
                
                # Rollback
                for u in changed:
                    forbidden[u] &= ~c
                color[v] = 0
                
        return False

    if backtrack(0):
        c_map = {1: 1, 2: 2, 4: 3}
        res = [c_map[color[i]] for i in range(n)]
        print("YES")
        print(*(res))
    else:
        print("NO")

if __name__ == '__main__':
    solve()