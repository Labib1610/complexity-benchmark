import sys

def solve():
    input = sys.stdin.readline
    q, t = map(int, input().split())
    n = 3 * q
    triples = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        triples.append((a-1, b-1, c-1))
    
    # Group triples by first element for quick lookup
    by_person = [[] for _ in range(n)]
    for idx, (a, b, c) in enumerate(triples):
        by_person[a].append(idx)
        by_person[b].append(idx)
        by_person[c].append(idx)
    
    used = [False] * t
    chosen = []
    full_mask = (1 << n) - 1
    
    # Precompute masks for each triple
    masks = []
    for a, b, c in triples:
        masks.append((1 << a) | (1 << b) | (1 << c))
    
    def backtrack(covered_mask):
        if covered_mask == full_mask:
            return True
        # Find first uncovered person
        # We can use bit trick to find lowest zero bit
        inv = (~covered_mask) & full_mask
        # lowest set bit
        lsb = inv & -inv
        person = (lsb.bit_length() - 1)
        
        for idx in by_person[person]:
            if used[idx]:
                continue
            m = masks[idx]
            if covered_mask & m:
                continue
            used[idx] = True
            chosen.append(triples[idx])
            if backtrack(covered_mask | m):
                return True
            chosen.pop()
            used[idx] = False
        return False
    
    if backtrack(0):
        print("YES")
        for a, b, c in chosen:
            print(a+1, b+1, c+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()