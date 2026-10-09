import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    q = int(input_data[0])
    t = int(input_data[1])
    triples = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        triples.append((a, b, c))
    
    n = 3 * q
    # For each component, list of triple indices containing it
    comp_to_triples = [[] for _ in range(n+1)]
    for i, (a,b,c) in enumerate(triples):
        comp_to_triples[a].append(i)
        comp_to_triples[b].append(i)
        comp_to_triples[c].append(i)
    
    used_triple = [False] * t
    used_comp = [False] * (n+1)
    chosen = []
    
    # Recursive exact cover
    def backtrack():
        if len(chosen) == q:
            return True
        # Find component with fewest available triples
        best_comp = -1
        best_list = None
        for comp in range(1, n+1):
            if not used_comp[comp]:
                avail = [tri for tri in comp_to_triples[comp] if not used_triple[tri]]
                if best_comp == -1 or len(avail) < len(best_list):
                    best_comp = comp
                    best_list = avail
                    if len(best_list) == 0:
                        return False
                    if len(best_list) == 1:
                        break
        if best_comp == -1:
            return False
        # Try each candidate triple
        for tri_idx in best_list:
            a,b,c = triples[tri_idx]
            if used_comp[a] or used_comp[b] or used_comp[c]:
                continue
            # Choose
            used_triple[tri_idx] = True
            used_comp[a] = used_comp[b] = used_comp[c] = True
            chosen.append((a,b,c))
            if backtrack():
                return True
            # Undo
            chosen.pop()
            used_triple[tri_idx] = False
            used_comp[a] = used_comp[b] = used_comp[c] = False
        return False
    
    if backtrack():
        print("YES")
        for a,b,c in chosen:
            print(a,b,c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()