import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    q = int(input_data[0])
    t = int(input_data[1])
    
    if q == 0:
        print("YES")
        return
    
    trios = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx]) - 1
        b = int(input_data[idx+1]) - 1
        c = int(input_data[idx+2]) - 1
        idx += 3
        trios.append((a, b, c))
    
    n = 3 * q
    elem_trios = [[] for _ in range(n)]
    for i, (a, b, c) in enumerate(trios):
        elem_trios[a].append(i)
        elem_trios[b].append(i)
        elem_trios[c].append(i)
        
    trio_active = [True] * t
    elem_count = [len(elem_trios[i]) for i in range(n)]
    covered = [False] * n
    
    selected_trios = []
    
    def search(remaining):
        if remaining == 0:
            return True
        
        # Find uncovered element with minimum remaining candidate trios (MRV)
        best_elem = -1
        min_c = 10**9
        
        for u in range(n):
            if not covered[u]:
                c = elem_count[u]
                if c == 0:
                    return False
                if c < min_c:
                    min_c = c
                    best_elem = u
                    if c == 1:
                        break
        
        # Try trios covering best_elem
        # Copy the list because trio_active status will change
        candidates = [t_idx for t_idx in elem_trios[best_elem] if trio_active[t_idx]]
        
        for t_idx in candidates:
            a, b, c = trios[t_idx]
            if covered[a] or covered[b] or covered[c]:
                continue
            
            # Select t_idx
            selected_trios.append(t_idx)
            covered[a] = covered[b] = covered[c] = True
            
            # Deactivate all trios that share an element with this trio
            deactivated = []
            for u in (a, b, c):
                for other_t in elem_trios[u]:
                    if trio_active[other_t]:
                        trio_active[other_t] = False
                        deactivated.append(other_t)
                        for w in trios[other_t]:
                            elem_count[w] -= 1
            
            if search(remaining - 3):
                return True
            
            # Backtrack
            selected_trios.pop()
            covered[a] = covered[b] = covered[c] = False
            for other_t in deactivated:
                trio_active[other_t] = True
                for w in trios[other_t]:
                    elem_count[w] += 1
                    
        return False

    if search(n):
        print("YES")
        out = []
        for t_idx in selected_trios:
            a, b, c = trios[t_idx]
            out.append(f"{a+1} {b+1} {c+1}")
        print("\n".join(out))
    else:
        print("NO")

if __name__ == '__main__':
    solve()