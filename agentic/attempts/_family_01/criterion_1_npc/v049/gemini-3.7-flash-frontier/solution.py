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
            
    # Quick check: self-loop
    # Since input is simple graph, no self-loops unless m has it, but standard input u != v.
    
    avail = [7] * n  # 7 is binary 111 (colors 0, 1, 2 available)
    color = [-1] * n
    
    # Precompute popcount for 0..7
    popcount = [0, 1, 1, 2, 1, 2, 2, 3]

    def backtrack(uncolored_count):
        if uncolored_count == 0:
            return True
        
        # Choose vertex with minimum available colors > 0
        best_v = -1
        min_c = 4
        
        for i in range(n):
            if color[i] == -1:
                c = popcount[avail[i]]
                if c < min_c:
                    min_c = c
                    best_v = i
                    if min_c == 1:
                        break
        
        if min_c == 0:
            return False
        
        v = best_v
        v_avail = avail[v]
        
        for c in range(3):
            if (v_avail & (1 << c)):
                # Try assigning color c to v
                color[v] = c
                
                # Forward checking
                conflict = False
                affected = []
                mask = adj[v]
                
                # Iterate through neighbors
                while mask:
                    lsb = mask & -mask
                    u = (lsb).bit_length() - 1
                    mask ^= lsb
                    
                    if color[u] == -1 and (avail[u] & (1 << c)):
                        avail[u] ^= (1 << c)
                        affected.append(u)
                        if avail[u] == 0:
                            conflict = True
                
                if not conflict:
                    if backtrack(uncolored_count - 1):
                        return True
                
                # Backtrack
                for u in affected:
                    avail[u] |= (1 << c)
                color[v] = -1
                
        return False

    if backtrack(n):
        print("YES")
        print(*(color[i] + 1 for i in range(n)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()