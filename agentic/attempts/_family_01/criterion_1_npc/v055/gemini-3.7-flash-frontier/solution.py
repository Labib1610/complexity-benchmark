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
    adj_mask = [0] * n
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        if u == v:
            print("NO")
            return
        if not (adj_mask[u] & (1 << v)):
            adj[u].append(v)
            adj[v].append(u)
            adj_mask[u] |= (1 << v)
            adj_mask[v] |= (1 << u)
            
    # Degree of each vertex
    degree = [len(adj[i]) for i in range(n)]
    
    # Available colors mask for each vertex: bits 0, 1, 2 for colors 1, 2, 3
    # 7 is binary 111
    avail = [7] * n
    assignment = [0] * n
    
    # Precompute bit count for mask 0..7
    popcount = [0, 1, 1, 2, 1, 2, 2, 3]
    
    def backtrack(assigned_count):
        if assigned_count == n:
            return True
        
        # Choose unassigned vertex with MRV (minimum remaining values)
        # Tie break by maximum degree
        best_v = -1
        min_choices = 4
        max_deg = -1
        
        for i in range(n):
            if assignment[i] == 0:
                c = popcount[avail[i]]
                if c < min_choices:
                    min_choices = c
                    max_deg = degree[i]
                    best_v = i
                elif c == min_choices:
                    if degree[i] > max_deg:
                        max_deg = degree[i]
                        best_v = i
                        
        if min_choices == 0:
            return False
        
        u = best_v
        u_avail = avail[u]
        
        for color_idx in range(3):
            c_bit = 1 << color_idx
            if u_avail & c_bit:
                assignment[u] = color_idx + 1
                
                # Forward check: remove c_bit from neighbors
                changed = []
                possible = True
                for v in adj[u]:
                    if assignment[v] == 0:
                        if avail[v] & c_bit:
                            avail[v] ^= c_bit
                            changed.append(v)
                            if avail[v] == 0:
                                possible = False
                
                if possible:
                    if backtrack(assigned_count + 1):
                        return True
                
                # Undo changes
                for v in changed:
                    avail[v] |= c_bit
                assignment[u] = 0
                
        return False

    if backtrack(0):
        print("YES")
        print(*(assignment[i] for i in range(n)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()