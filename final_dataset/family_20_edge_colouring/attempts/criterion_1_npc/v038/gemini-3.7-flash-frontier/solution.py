import sys

# Increase recursion depth just in case
sys.setrecursionlimit(100000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    
    idx = 2
    for e in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        edges.append((u, v))
        adj[u].append(e)
        adj[v].append(e)
        
    K = 2 * m // n
    if K != 3:
        # If degree is not 3, though problem says uniform K = 2m/n, m=3n/2 => K=3
        # Handle K != 3 if any
        print("NO")
        return

    # Check if every vertex has degree 3
    for i in range(1, n + 1):
        if len(adj[i]) != 3:
            print("NO")
            return

    # CSP variables: edge domains
    # Colors: 1, 2, 3 represented by bitmasks: 1 (0b001), 2 (0b010), 4 (0b100)
    # domain of edge: bitmask subset of 7 (0b111)
    
    domain = [7] * m
    
    def get_colors(mask):
        res = []
        if mask & 1: res.append(1)
        if mask & 2: res.append(2)
        if mask & 4: res.append(4)
        return res

    # Propagation queue
    def propagate():
        changed = True
        while changed:
            changed = False
            # Check edge domains
            for e in range(m):
                d = domain[e]
                if d == 0:
                    return False
            
            # Check vertices
            for v in range(1, n + 1):
                e1, e2, e3 = adj[v]
                d1, d2, d3 = domain[e1], domain[e2], domain[e3]
                
                # If an edge is fixed, remove its color from others
                # Check d1
                if d1 in (1, 2, 4):
                    if d2 & d1:
                        domain[e2] &= ~d1
                        if domain[e2] == 0: return False
                        changed = True
                    if d3 & d1:
                        domain[e3] &= ~d1
                        if domain[e3] == 0: return False
                        changed = True
                if d2 in (1, 2, 4):
                    if d1 & d2:
                        domain[e1] &= ~d2
                        if domain[e1] == 0: return False
                        changed = True
                    if d3 & d2:
                        domain[e3] &= ~d2
                        if domain[e3] == 0: return False
                        changed = True
                if d3 in (1, 2, 4):
                    if d1 & d3:
                        domain[e1] &= ~d3
                        if domain[e1] == 0: return False
                        changed = True
                    if d2 & d3:
                        domain[e2] &= ~d3
                        if domain[e2] == 0: return False
                        changed = True

                # Check if a color can only go to one edge among e1, e2, e3
                d1, d2, d3 = domain[e1], domain[e2], domain[e3]
                for c in (1, 2, 4):
                    cnt = (1 if (d1 & c) else 0) + (1 if (d2 & c) else 0) + (1 if (d3 & c) else 0)
                    if cnt == 0:
                        return False
                    if cnt == 1:
                        if (d1 & c) and d1 != c:
                            domain[e1] = c
                            changed = True
                        elif (d2 & c) and d2 != c:
                            domain[e2] = c
                            changed = True
                        elif (d3 & c) and d3 != c:
                            domain[e3] = c
                            changed = True
        return True

    if not propagate():
        print("NO")
        return

    def backtrack():
        # Pick an edge with domain size > 1 (MRV heuristic: size 2 first)
        best_e = -1
        min_size = 4
        for e in range(m):
            d = domain[e]
            sz = (1 if (d & 1) else 0) + (1 if (d & 2) else 0) + (1 if (d & 4) else 0)
            if 1 < sz < min_size:
                min_size = sz
                best_e = e
                if sz == 2:
                    break
        
        if best_e == -1:
            return True
        
        saved_domain = list(domain)
        colors = get_colors(saved_domain[best_e])
        
        for c in colors:
            domain[best_e] = c
            if propagate():
                if backtrack():
                    return True
            domain[:] = saved_domain
            
        return False

    if backtrack():
        print("YES")
        mask_to_val = {1: 1, 2: 2, 4: 3}
        ans = [str(mask_to_val[domain[e]]) for e in range(m)]
        print(" ".join(ans))
    else:
        print("NO")

if __name__ == '__main__':
    solve()