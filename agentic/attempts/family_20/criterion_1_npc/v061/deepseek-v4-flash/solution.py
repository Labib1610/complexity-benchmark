import sys
sys.setrecursionlimit(1000000)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    adj = [[] for _ in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    color = [-1] * m
    # degree is 3 for all vertices
    # We'll try backtracking with MRV heuristic
    
    # Precompute for each edge the two vertices
    # We'll order edges by degree of endpoints (all 3, so no difference)
    # But we can order by number of already colored neighbors
    
    # We'll use a recursive backtracking
    # Since n <= 2000, m <= 3000, worst-case might be okay if we prune well.
    
    # Check if graph is 3-edge-colorable using backtracking
    # We'll try to color edges in order
    
    # For each vertex, keep track of used colors
    used = [0]*n  # bitmask of used colors (bits 0,1,2)
    
    # Sort edges by some heuristic: maybe by degree of endpoints (all same)
    # We'll just use input order but with MRV: choose edge with fewest available colors
    
    def backtrack(idx):
        if idx == m:
            return True
        # Find uncolored edge with fewest available colors
        best_edge = -1
        best_avail = 4
        best_mask = 0
        for i in range(m):
            if color[i] == -1:
                u, v = edges[i]
                mask = used[u] | used[v]
                avail = 3 - bin(mask).count("1")
                if avail < best_avail:
                    best_avail = avail
                    best_edge = i
                    best_mask = mask
                    if avail == 0:
                        break
        if best_avail == 0:
            return False
        i = best_edge
        u, v = edges[i]
        for c in range(3):
            if not (used[u] & (1<<c)) and not (used[v] & (1<<c)):
                color[i] = c
                used[u] |= (1<<c)
                used[v] |= (1<<c)
                if backtrack(idx+1):
                    return True
                used[u] ^= (1<<c)
                used[v] ^= (1<<c)
                color[i] = -1
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(str(c+1) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    solve()