import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    q = int(input_data[0])
    t = int(input_data[1])
    n = 3 * q
    triples = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx]) - 1
        b = int(input_data[idx+1]) - 1
        c = int(input_data[idx+2]) - 1
        idx += 3
        triples.append((a, b, c))
    
    # Build list of triples that contain each item
    item_to_triples = [[] for _ in range(n)]
    for i, (a, b, c) in enumerate(triples):
        item_to_triples[a].append(i)
        item_to_triples[b].append(i)
        item_to_triples[c].append(i)
    
    # Backtracking
    used = [False] * t
    chosen = []
    covered = 0
    cover_mask = [0] * t
    for i, (a, b, c) in enumerate(triples):
        cover_mask[i] = (1 << a) | (1 << b) | (1 << c)
    
    # We'll use a recursive search with pruning
    def backtrack(covered_mask, start):
        if covered_mask == (1 << n) - 1:
            return True
        # Find first uncovered item
        # Use bit trick to find lowest zero bit
        inv = (~covered_mask) & ((1 << n) - 1)
        if inv == 0:
            return True
        # lowest set bit
        item = (inv & -inv).bit_length() - 1
        for tri_idx in item_to_triples[item]:
            if used[tri_idx]:
                continue
            a, b, c = triples[tri_idx]
            if (covered_mask >> a) & 1 or (covered_mask >> b) & 1 or (covered_mask >> c) & 1:
                continue
            used[tri_idx] = True
            chosen.append(tri_idx)
            if backtrack(covered_mask | cover_mask[tri_idx], start + 1):
                return True
            chosen.pop()
            used[tri_idx] = False
        return False
    
    if backtrack(0, 0):
        print("YES")
        for idx in chosen:
            a, b, c = triples[idx]
            print(a+1, b+1, c+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()