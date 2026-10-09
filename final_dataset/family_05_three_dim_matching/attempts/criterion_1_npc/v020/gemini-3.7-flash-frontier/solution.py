import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    k = int(input_data[0])
    t = int(input_data[1])
    
    if k == 0:
        print("YES")
        return
    
    triples = []
    idx = 2
    for _ in range(t):
        e = int(input_data[idx]) - 1
        s = int(input_data[idx+1]) - 1
        p = int(input_data[idx+2]) - 1
        idx += 3
        triples.append((e, s, p))
    
    # 3k items: 0..k-1 for e, k..2k-1 for s, 2k..3k-1 for p
    # Each triple covers items: e, k + s, 2k + p
    
    # Map item to list of triple indices
    item_triples = [[] for _ in range(3 * k)]
    for i, (e, s, p) in enumerate(triples):
        item_triples[e].append(i)
        item_triples[k + s].append(i)
        item_triples[2 * k + p].append(i)
        
    # Quick check: does every item have at least one triple?
    for i in range(3 * k):
        if not item_triples[i]:
            print("NO")
            return

    # Backtracking with Algorithm X (DLX style using bitsets/lists)
    used_items = [False] * (3 * k)
    used_triples = [False] * len(triples)
    solution = []
    
    def search(rem_k):
        if rem_k == 0:
            return True
        
        # Find unused item with minimum remaining candidates
        best_item = -1
        min_candidates = 999999
        
        for i in range(3 * k):
            if not used_items[i]:
                # Count available candidates
                count = 0
                for tri_idx in item_triples[i]:
                    if not used_triples[tri_idx]:
                        count += 1
                if count < min_candidates:
                    min_candidates = count
                    best_item = i
                    if count == 0:
                        return False
                    if count == 1:
                        break
                        
        if best_item == -1 or min_candidates == 0:
            return False
            
        # Try each valid triple containing best_item
        # Collect candidates first to avoid iterator modification issues
        candidates = [tri_idx for tri_idx in item_triples[best_item] if not used_triples[tri_idx]]
        
        for tri_idx in candidates:
            e, s, p = triples[tri_idx]
            i_e, i_s, i_p = e, k + s, 2 * k + p
            
            # Check if valid (none of the 3 items should be used)
            if used_items[i_e] or used_items[i_s] or used_items[i_p]:
                continue
                
            # Cover
            used_items[i_e] = True
            used_items[i_s] = True
            used_items[i_p] = True
            
            # Deactivate conflicting triples
            conflicted = []
            for item in (i_e, i_s, i_p):
                for other_tri in item_triples[item]:
                    if not used_triples[other_tri]:
                        used_triples[other_tri] = True
                        conflicted.append(other_tri)
                        
            solution.append(tri_idx)
            
            if search(rem_k - 1):
                return True
                
            # Backtrack
            solution.pop()
            for other_tri in conflicted:
                used_triples[other_tri] = False
            used_items[i_e] = False
            used_items[i_s] = False
            used_items[i_p] = False
            
        return False

    sys.setrecursionlimit(2000)
    if search(k):
        print("YES")
        for tri_idx in solution:
            e, s, p = triples[tri_idx]
            print(f"{e + 1} {s + 1} {p + 1}")
    else:
        print("NO")

if __name__ == '__main__':
    solve()