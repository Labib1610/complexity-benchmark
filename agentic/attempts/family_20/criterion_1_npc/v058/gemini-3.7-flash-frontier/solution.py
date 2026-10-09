import sys

# Increase recursion depth for deep search trees
sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    
    idx = 2
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
        
    # Check if all degrees are 3
    for i in range(1, n + 1):
        if len(adj[i]) != 3:
            print("NO")
            return

    edge_color = [-1] * m
    vertex_mask = [0] * (n + 1)
    
    # Pre-calculate bit counts for masks 0..7
    # 7 & ~(mask_u | mask_v) gives available colors bitmask
    avail_colors_lookup = [[] for _ in range(8)]
    for mask in range(8):
        colors = []
        for c in range(3):
            if not (mask & (1 << c)):
                colors.append(c)
        avail_colors_lookup[mask] = colors

    # To quickly find an unassigned edge with MRV
    unassigned = set(range(m))
    
    def backtrack():
        if not unassigned:
            return True
        
        # MRV: Find edge with minimum available colors
        best_e = -1
        best_colors = None
        min_c = 4
        
        for e in unassigned:
            u, v = edges[e]
            mask = vertex_mask[u] | vertex_mask[v]
            avail = avail_colors_lookup[mask]
            c_len = len(avail)
            
            if c_len == 0:
                return False
            if c_len < min_c:
                min_c = c_len
                best_e = e
                best_colors = avail
                if min_c == 1:
                    break
        
        u, v = edges[best_e]
        unassigned.remove(best_e)
        
        for c in best_colors:
            bit = 1 << c
            edge_color[best_e] = c
            vertex_mask[u] |= bit
            vertex_mask[v] |= bit
            
            if backtrack():
                return True
            
            vertex_mask[u] &= ~bit
            vertex_mask[v] &= ~bit
            edge_color[best_e] = -1
            
        unassigned.add(best_e)
        return False

    if backtrack():
        print("YES")
        print(*(c + 1 for c in edge_color))
    else:
        print("NO")

if __name__ == '__main__':
    solve()