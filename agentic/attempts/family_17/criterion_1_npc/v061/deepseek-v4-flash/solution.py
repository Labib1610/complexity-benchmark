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
        triples.append((a-1, b-1, c-1))  # 0-based

    n = 3 * q
    full_mask = (1 << n) - 1

    # Sort triples by first element for better pruning
    triples.sort()

    # We'll do backtracking
    used = 0
    chosen = []

    # Precompute for each triple a bitmask
    triple_masks = []
    for a,b,c in triples:
        triple_masks.append((1 << a) | (1 << b) | (1 << c))

    # Recursive search
    def dfs(count, used_mask):
        if count == q:
            return used_mask == full_mask
        # Try triples
        for i, (a,b,c) in enumerate(triples):
            mask = triple_masks[i]
            if used_mask & mask == 0:
                chosen.append((a+1,b+1,c+1))
                if dfs(count+1, used_mask | mask):
                    return True
                chosen.pop()
        return False

    if dfs(0, 0):
        print("YES")
        for a,b,c in chosen:
            print(a,b,c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()