import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    k = int(input_data[0])
    t = int(input_data[1])
    triples = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx]); b = int(input_data[idx+1]); c = int(input_data[idx+2])
        idx += 3
        triples.append((a, b, c))
    
    # Group triples by a
    by_a = [[] for _ in range(k+1)]
    for a, b, c in triples:
        by_a[a].append((b, c))
    
    # Sort each group for deterministic order
    for i in range(1, k+1):
        by_a[i].sort()
    
    used_b = 0
    used_c = 0
    chosen = []
    
    # Backtracking
    def dfs(a):
        nonlocal used_b, used_c
        if a > k:
            return len(chosen) == k
        # Try to pick a triple for this a
        for b, c in by_a[a]:
            if not (used_b & (1 << (b-1))) and not (used_c & (1 << (c-1))):
                used_b |= (1 << (b-1))
                used_c |= (1 << (c-1))
                chosen.append((a, b, c))
                if dfs(a+1):
                    return True
                chosen.pop()
                used_b ^= (1 << (b-1))
                used_c ^= (1 << (c-1))
        # Also possible to skip this a (if we don't need to use all a values)
        # But we need exactly k triples, and there are k possible a values.
        # Since we need exactly k triples and each a can be used at most once,
        # we must use all a values 1..k exactly once.
        # So no skip.
        return False
    
    if dfs(1):
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()