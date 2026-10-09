import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

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
            
    # Check self-loops
    # If self-loop, no coloring possible
    # (Problem statement says pairs, simple graph usually, but let's be careful)

    # 3-coloring solver with MRV and degree tie-breaker
    # Domain bitmask: color 0 (1), color 1 (2), color 2 (4) -> mask in [0..7]
    
    # We maintain the forbidden mask for each vertex:
    # forbidden[v] has bit c set if some assigned neighbor of v has color c.
    forbidden = [0] * n
    assigned = [-1] * n
    
    # Precompute degrees
    deg = [bin(adj[i]).count('1') for i in range(n)]

    def backtrack(count):
        if count == n:
            return True
        
        # Pick unassigned vertex with max saturation (most forbidden colors), then max degree
        best_v = -1
        max_sat = -1
        max_d = -1
        
        for i in range(n):
            if assigned[i] == -1:
                sat = bin(forbidden[i]).count('1')
                if sat == 3:
                    return False
                if sat > max_sat or (sat == max_sat and deg[i] > max_d):
                    max_sat = sat
                    max_d = deg[i]
                    best_v = i
                    
        u = best_v
        u_forb = forbidden[u]
        
        # Try available colors
        for c in range(3):
            if not (u_forb & (1 << c)):
                assigned[u] = c
                # Update forbidden for neighbors
                # Keep track of which neighbors were updated
                updated = []
                c_mask = 1 << c
                mask = adj[u]
                while mask:
                    lsb = mask & -mask
                    v = (lsb).bit_length() - 1
                    mask ^= lsb
                    if assigned[v] == -1 and not (forbidden[v] & c_mask):
                        forbidden[v] |= c_mask
                        updated.append(v)
                
                if backtrack(count + 1):
                    return True
                
                # Undo
                for v in updated:
                    forbidden[v] ^= c_mask
                assigned[u] = -1
                
        return False

    if backtrack(0):
        print("YES")
        print(*(assigned[i] + 1 for i in range(n)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()