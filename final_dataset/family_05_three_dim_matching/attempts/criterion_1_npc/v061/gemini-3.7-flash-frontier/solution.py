import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    k = int(input_data[0])
    t = int(input_data[1])
    
    triples = []
    idx = 2
    for _ in range(t):
        x = int(input_data[idx]) - 1
        y = int(input_data[idx+1]) - 1
        z = int(input_data[idx+2]) - 1
        idx += 3
        triples.append((x, y, z))
    
    # 3k elements to cover:
    # 0 .. k-1 for X
    # k .. 2k-1 for Y
    # 2k .. 3k-1 for Z
    
    # Pre-filter impossible elements: if any item has 0 triples, impossible immediately
    element_triples = [[] for _ in range(3 * k)]
    for i, (x, y, z) in enumerate(triples):
        element_triples[x].append(i)
        element_triples[k + y].append(i)
        element_triples[2 * k + z].append(i)
        
    for e in range(3 * k):
        if not element_triples[e]:
            print("NO")
            return

    # Backtracking with MRV (Minimum Remaining Values)
    # We can maintain the set of active triples or just check bitmasks of covered elements.
    
    mask_X = 0
    mask_Y = 0
    mask_Z = 0
    
    chosen = []
    
    def search(count):
        nonlocal mask_X, mask_Y, mask_Z
        if count == k:
            return True
        
        # Find uncovered element with minimum available valid triples
        best_elem = -1
        best_count = 1000000
        best_valid_triples = None
        
        # Check uncovered in X
        for x in range(k):
            if not (mask_X & (1 << x)):
                valid = []
                for tr_idx in element_triples[x]:
                    _, y, z = triples[tr_idx]
                    if not (mask_Y & (1 << y)) and not (mask_Z & (1 << z)):
                        valid.append(tr_idx)
                if len(valid) < best_count:
                    best_count = len(valid)
                    best_elem = x
                    best_valid_triples = valid
                    if best_count == 0:
                        return False
                    if best_count == 1:
                        break
        
        # If best_count > 1, check Y and Z as well to find smaller branching factor
        if best_count > 1:
            for y in range(k):
                if not (mask_Y & (1 << y)):
                    valid = []
                    for tr_idx in element_triples[k + y]:
                        x, _, z = triples[tr_idx]
                        if not (mask_X & (1 << x)) and not (mask_Z & (1 << z)):
                            valid.append(tr_idx)
                    if len(valid) < best_count:
                        best_count = len(valid)
                        best_elem = k + y
                        best_valid_triples = valid
                        if best_count == 0:
                            return False
                        if best_count == 1:
                            break
                            
        if best_count > 1:
            for z in range(k):
                if not (mask_Z & (1 << z)):
                    valid = []
                    for tr_idx in element_triples[2 * k + z]:
                        x, y, _ = triples[tr_idx]
                        if not (mask_X & (1 << x)) and not (mask_Y & (1 << y)):
                            valid.append(tr_idx)
                    if len(valid) < best_count:
                        best_count = len(valid)
                        best_elem = 2 * k + z
                        best_valid_triples = valid
                        if best_count == 0:
                            return False
                        if best_count == 1:
                            break
        
        if best_count == 0 or best_elem == -1:
            return False
            
        for tr_idx in best_valid_triples:
            x, y, z = triples[tr_idx]
            # Double check validity
            if (mask_X & (1 << x)) or (mask_Y & (1 << y)) or (mask_Z & (1 << z)):
                continue
            
            mask_X |= (1 << x)
            mask_Y |= (1 << y)
            mask_Z |= (1 << z)
            chosen.append(tr_idx)
            
            if search(count + 1):
                return True
                
            chosen.pop()
            mask_X &= ~(1 << x)
            mask_Y &= ~(1 << y)
            mask_Z &= ~(1 << z)
            
        return False

    if search(0):
        print("YES")
        out = []
        for tr_idx in chosen:
            x, y, z = triples[tr_idx]
            out.append(f"{x + 1} {y + 1} {z + 1}")
        print("\n".join(out))
    else:
        print("NO")

if __name__ == '__main__':
    solve()