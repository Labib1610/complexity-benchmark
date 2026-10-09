import sys

def solve():
    data = sys.stdin.read().split()
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
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    full_mask = (1 << n) - 1
    color = [0] * n
    visited = 0
    
    for start in range(n):
        if visited & (1 << start):
            continue
        
        # Find connected component containing 'start'
        comp = 0
        stack = [start]
        comp |= 1 << start
        while stack:
            u = stack.pop()
            nb = adj[u] & ~comp
            while nb:
                v = (nb & -nb).bit_length() - 1
                comp |= 1 << v
                stack.append(v)
                nb &= nb - 1
        
        # Enumerate all valid 3-colorings of this component
        nodes = []
        temp = comp
        while temp:
            v = (temp & -temp).bit_length() - 1
            nodes.append(v)
            temp &= temp - 1
        
        k = len(nodes)
        best = None
        
        # Try all 3^k colorings
        for state in range(3**k):
            valid = True
            c = [0] * k
            s = state
            for i in range(k):
                c[i] = s % 3
                s //= 3
            
            for i in range(k):
                u = nodes[i]
                cu = c[i]
                for j in range(i+1, k):
                    v = nodes[j]
                    if (adj[u] >> v) & 1:
                        if c[j] == cu:
                            valid = False
                            break
                if not valid:
                    break
            
            if valid:
                if best is None:
                    best = c[:]
                else:
                    # Compare lexicographically by original node index order
                    better = False
                    for i in range(k):
                        if c[i] < best[i]:
                            better = True
                            break
                        elif c[i] > best[i]:
                            break
                    if better:
                        best = c[:]
        
        if best is None:
            print("NO")
            return
        
        for i, v in enumerate(nodes):
            color[v] = best[i] + 1
        
        visited |= comp
    
    print("YES")
    print(' '.join(map(str, color)))

solve()