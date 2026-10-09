import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); m = int(data[1])
    nbr = [0]*n
    idx = 2
    for _ in range(m):
        u = int(data[idx])-1; v = int(data[idx+1])-1; idx += 2
        if u != v:
            nbr[u] |= 1 << v
            nbr[v] |= 1 << u
    deg = [bin(nbr[i]).count('1') for i in range(n)]
    
    PC3 = (0,1,1,2,1,2,2,3)
    
    # Peel degree <= 2
    degc = deg[:]
    removed = [False]*n
    peel = []
    stack = [v for v in range(n) if degc[v] <= 2]
    while stack:
        v = stack.pop()
        if removed[v]:
            continue
        # degc[v] should be <= 2 (might have decreased further; fine)
        removed[v] = True
        peel.append(v)
        w = nbr[v]
        while w:
            b = w & -w; w ^= b
            u = b.bit_length()-1
            if not removed[u]:
                degc[u] -= 1
                if degc[u] <= 2:
                    stack.append(u)
    core = [v for v in range(n) if not removed[v]]
    
    assigned = [-1]*n
    
    if core:
        # K4 check on core (or whole graph; core suffices since K4 has min degree 3)
        # Actually check whole graph? K4 vertices all have degree >=3 in whole graph... 
        # A K4 in the peeled-away part? Peeled vertices have degree<=2 at peel time; 
        # K4 vertices have 3 neighbors within K4 -> degree >=3 always -> never peeled. 
        # So checking core is sufficient. But simpler: check whole graph.
        def has_k4():
            for x in range(n):
                A = nbr[x]
                while A:
                    ab = A & -A; A ^= ab
                    y = ab.bit_length()-1
                    if y < x: continue  # avoid double work; not necessary
                    B = nbr[x] & nbr[y]
                    while B:
                        bb = B & -B; B ^= bb
                        z = bb.bit_length()-1
                        if nbr[z] & B:
                            return True
            return False
        # hmm wait, this checks: x,y adjacent, z in common neighbors, and z adjacent to 
        # another common neighbor w (w in B after removing z) -> x,y,z,w K4? 
        # x,y adjacent; z adjacent to x,y; w adjacent to x,y; z~w. Yes K4. ✓
        if has_k4():
            print("NO")
            return
        # components of core
        in_core = [False]*n
        for v in core: in_core[v] = True
        visited = [False]*n
        comps = []
        for s in core:
            if not visited[s]:
                comp = []
                dq = [s]; visited[s] = True
                while dq:
                    x = dq.pop()
                    comp.append(x)
                    w = nbr[x]
                    while w:
                        b = w & -w; w ^= b
                        u = b.bit_length()-1
                        if in_core[u] and not visited[u]:
                            visited[u] = True
                            dq.append(u)
                comps.append(comp)
        # solve each component
        for comp in comps:
            if not solve_component(comp, nbr, deg, assigned, PC3):
                print("NO")
                return
    # reconstruct peeled
    for v in reversed(peel):
        blocked = 0
        w = nbr[v]
        while w:
            b = w & -w; w ^= b
            u = b.bit_length()-1
            c = assigned[u]
            if c >= 0:
                blocked |= 1 << c
        av = 7 & ~blocked
        assigned[v] = (av & -av).bit_length() - 1
    print("YES")
    print(' '.join(str(c+1) for c in assigned))