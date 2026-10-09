import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    k = int(input_data[0])
    t = int(input_data[1])
    
    triples = []
    triple_masks = []
    
    # Pre-parse triples and assign bitmasks
    # Bits [0..k-1] for X, [k..2k-1] for Y, [2k..3k-1] for Z
    item_triples = [[] for _ in range(3 * k)]
    
    idx = 2
    for e in range(t):
        x = int(input_data[idx]) - 1
        y = int(input_data[idx + 1]) - 1
        z = int(input_data[idx + 2]) - 1
        idx += 3
        
        triples.append((x + 1, y + 1, z + 1))
        mask = (1 << x) | (1 << (k + y)) | (1 << (2 * k + z))
        triple_masks.append(mask)
        
        item_triples[x].append(e)
        item_triples[k + y].append(e)
        item_triples[2 * k + z].append(e)
        
    full_mask = (1 << (3 * k)) - 1
    solution = []
    
    def backtrack(used_mask):
        if used_mask == full_mask:
            return True
        
        best_item = -1
        best_candidates = None
        min_candidates = 999999
        
        # Find the uncovered item with the minimum number of valid candidates (MRV heuristic)
        for i in range(3 * k):
            if not (used_mask & (1 << i)):
                valid = [e for e in item_triples[i] if not (triple_masks[e] & used_mask)]
                count = len(valid)
                if count == 0:
                    return False
                if count < min_candidates:
                    min_candidates = count
                    best_candidates = valid
                    best_item = i
                    if min_candidates == 1:
                        break
        
        for e in best_candidates:
            solution.append(e)
            if backtrack(used_mask | triple_masks[e]):
                return True
            solution.pop()
            
        return False

    if backtrack(0):
        out = ["YES"]
        for e in solution:
            x, y, z = triples[e]
            out.append(f"{x} {y} {z}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == '__main__':
    solve()