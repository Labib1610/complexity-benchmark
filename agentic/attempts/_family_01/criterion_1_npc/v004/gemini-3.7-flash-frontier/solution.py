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
            
    # Check self loops (though input is conflict pairs)
    # Connected components
    visited = [False] * n
    components = []
    for i in range(n):
        if not visited[i]:
            comp = []
            queue = [i]
            visited[i] = True
            for u in queue:
                comp.append(u)
                for v in range(n):
                    if (adj[u] & (1 << v)) and not visited[v]:
                        visited[v] = True
                        queue.append(v)
            components.append(comp)

    final_color = [-1] * n

    for comp in components:
        comp_mask = 0
        for u in comp:
            comp_mask |= (1 << u)
            
        color = [-1] * n
        forbidden = [0] * n
        
        # Precompute static degrees within component for tie-breaking
        deg = [bin(adj[u] & comp_mask).count('1') for u in range(n)]

        def backtrack(uncolored_count):
            if uncolored_count == 0:
                return True
            
            # Find vertex with maximum saturation degree (popcount of forbidden)
            best_u = -1
            max_sat = -1
            max_deg = -1
            
            for u in comp:
                if color[u] == -1:
                    f = forbidden[u]
                    sat = (f & 1) + ((f >> 1) & 1) + ((f >> 2) & 1)
                    if sat == 3:
                        return False  # No available colors
                    if sat > max_sat or (sat == max_sat and deg[u] > max_deg):
                        max_sat = sat
                        max_deg = deg[u]
                        best_u = u
            
            u = best_u
            f_u = forbidden[u]
            
            # Try available colors
            for c in range(3):
                if not (f_u & (1 << c)):
                    color[u] = c
                    # Update neighbors
                    changed = []
                    valid = True
                    nbrs = adj[u] & comp_mask
                    # Iterate over set bits in nbrs
                    curr = nbrs
                    while curr:
                        lsb = curr & -curr
                        v = (lsb).bit_length() - 1
                        curr ^= lsb
                        
                        if color[v] == -1:
                            if not (forbidden[v] & (1 << c)):
                                forbidden[v] |= (1 << c)
                                changed.append(v)
                                if forbidden[v] == 7:
                                    valid = False
                    
                    if valid and backtrack(uncolored_count - 1):
                        return True
                    
                    # Undo
                    for v in changed:
                        forbidden[v] ^= (1 << c)
                    color[u] = -1

            return False

        if not backtrack(len(comp)):
            print("NO")
            return
        
        for u in comp:
            final_color[u] = color[u] + 1  # 1-indexed

    print("YES")
    print(*(final_color[i] if final_color[i] != -1 else 1 for i in range(n)))

if __name__ == '__main__':
    solve()