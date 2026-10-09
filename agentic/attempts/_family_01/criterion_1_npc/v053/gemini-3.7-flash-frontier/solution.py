import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

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
        v = int(input_data[idx+1]) - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * n
    # mask[i] has bits 0, 1, 2 representing availability of colors 1, 2, 3
    mask = [7] * n
    
    # Precompute degrees for tie-breaking
    deg = [len(adj[i]) for i in range(n)]
    
    def backtrack(assigned_count):
        if assigned_count == n:
            return True
        
        # Select unassigned vertex with minimum available colors (MRV)
        best_u = -1
        min_c = 4
        max_d = -1
        
        for u in range(n):
            if color[u] == -1:
                c_cnt = (mask[u] & 1) + ((mask[u] >> 1) & 1) + ((mask[u] >> 2) & 1)
                if c_cnt < min_c:
                    min_c = c_cnt
                    best_u = u
                    max_d = deg[u]
                    if min_c == 0:
                        return False
                elif c_cnt == min_c:
                    if deg[u] > max_d:
                        best_u = u
                        max_d = deg[u]
        
        u = best_u
        u_mask = mask[u]
        
        for c in range(3):
            bit = 1 << c
            if u_mask & bit:
                color[u] = c + 1
                # Update neighbors
                changed = []
                for v in adj[u]:
                    if color[v] == -1 and (mask[v] & bit):
                        mask[v] ^= bit
                        changed.append(v)
                
                if backtrack(assigned_count + 1):
                    return True
                
                # Undo updates
                for v in changed:
                    mask[v] |= bit
                color[u] = -1
                
        return False

    if backtrack(0):
        print("YES")
        print(*(color[i] for i in range(n)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()