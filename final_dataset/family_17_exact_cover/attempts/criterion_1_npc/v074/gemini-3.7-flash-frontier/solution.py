import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    q = int(input_data[0])
    t = int(input_data[1])
    
    if t < q:
        print("NO")
        return
        
    n = 3 * q
    
    raw_triples = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        raw_triples.append((a, b, c))
    
    # Remove duplicates
    unique_triples = sorted(list(set(raw_triples)))
    num_triples = len(unique_triples)
    
    elem_to_triples = [[] for _ in range(n + 1)]
    for i, (a, b, c) in enumerate(unique_triples):
        elem_to_triples[a].append(i)
        elem_to_triples[b].append(i)
        elem_to_triples[c].append(i)
        
    # Check if any element has no triples
    for i in range(1, n + 1):
        if not elem_to_triples[i]:
            print("NO")
            return

    elem_deg = [len(elem_to_triples[i]) for i in range(n + 1)]
    deleted_triples = [False] * num_triples
    
    uncovered = list(range(1, n + 1))
    pos_in_uncovered = [0] * (n + 1)
    for i, elem in enumerate(uncovered):
        pos_in_uncovered[elem] = i
        
    solution = []
    
    def remove_uncovered(elem):
        idx = pos_in_uncovered[elem]
        last_elem = uncovered[-1]
        uncovered[idx] = last_elem
        pos_in_uncovered[last_elem] = idx
        uncovered.pop()
        
    def restore_uncovered(elem):
        pos_in_uncovered[elem] = len(uncovered)
        uncovered.append(elem)

    def backtrack():
        if not uncovered:
            return True
            
        # MRV: Choose uncovered element with minimum degree
        min_deg = 10**9
        best_elem = -1
        for elem in uncovered:
            d = elem_deg[elem]
            if d < min_deg:
                min_deg = d
                best_elem = elem
                if d == 0:
                    break
                    
        if min_deg == 0:
            return False
            
        # Try all triples containing best_elem
        candidate_triples = [t_idx for t_idx in elem_to_triples[best_elem] if not deleted_triples[t_idx]]
        
        for t_idx in candidate_triples:
            u, v, w = unique_triples[t_idx]
            
            # Disable conflicting triples
            disabled_this_step = []
            for elem in (u, v, w):
                remove_uncovered(elem)
                for other_t in elem_to_triples[elem]:
                    if not deleted_triples[other_t]:
                        deleted_triples[other_t] = True
                        disabled_this_step.append(other_t)
                        ou, ov, ow = unique_triples[other_t]
                        elem_deg[ou] -= 1
                        elem_deg[ov] -= 1
                        elem_deg[ow] -= 1
            
            solution.append(t_idx)
            
            if backtrack():
                return True
                
            solution.pop()
            
            # Undo disabling
            for other_t in disabled_this_step:
                deleted_triples[other_t] = False
                ou, ov, ow = unique_triples[other_t]
                elem_deg[ou] += 1
                elem_deg[ov] += 1
                elem_deg[ow] += 1
                
            for elem in (w, v, u):
                restore_uncovered(elem)
                
        return False

    if backtrack():
        print("YES")
        out = []
        for t_idx in solution:
            a, b, c = unique_triples[t_idx]
            out.append(f"{a} {b} {c}")
        print("\n".join(out))
    else:
        print("NO")

if __name__ == '__main__':
    solve()