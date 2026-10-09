import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        if u != v:
            adj[u].append(v)
            adj[v].append(u)

    # 3-coloring solver
    color = [0] * (n + 1)
    
    # Precompute mask of unavailable colors or neighbor colors
    # We can maintain available colors for each vertex using bitmask:
    # 1: color 1, 2: color 2, 4: color 3 -> initial available mask = 7 (1 | 2 | 4)
    avail = [7] * (n + 1)
    
    # Count of set bits
    bit_count = [0, 1, 1, 2, 1, 2, 2, 3]

    def backtrack(assigned_count):
        if assigned_count == n:
            return True
        
        # Select unassigned vertex with minimum available colors (MRV)
        # Tie breaker: maximum degree
        best_u = -1
        best_cnt = 4
        best_deg = -1
        
        for u in range(1, n + 1):
            if color[u] == 0:
                cnt = bit_count[avail[u]]
                if cnt < best_cnt:
                    best_cnt = cnt
                    best_u = u
                    best_deg = len(adj[u])
                    if cnt == 0:
                        return False
                elif cnt == best_cnt:
                    if len(adj[u]) > best_deg:
                        best_deg = len(adj[u])
                        best_u = u
        
        u = best_u
        u_avail = avail[u]
        
        for c in (1, 2, 3):
            c_mask = 1 << (c - 1)
            if u_avail & c_mask:
                color[u] = c
                # Update neighbors
                changed = []
                for v in adj[u]:
                    if color[v] == 0 and (avail[v] & c_mask):
                        avail[v] ^= c_mask
                        changed.append(v)
                
                if backtrack(assigned_count + 1):
                    return True
                
                # Undo
                for v in changed:
                    avail[v] |= c_mask
                color[u] = 0
                
        return False

    if backtrack(0):
        print("YES")
        print(*(color[i] for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()