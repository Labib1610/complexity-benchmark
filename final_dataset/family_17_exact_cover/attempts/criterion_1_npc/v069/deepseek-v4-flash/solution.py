import sys

def solve():
    input = sys.stdin.readline
    q, t = map(int, input().split())
    n = 3 * q
    trios = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        if 6 <= a + b + c <= 9 * q - 3:
            trios.append((a, b, c))
    
    target_sum = n * (n + 1) // 2
    # Sort trios by sum for better pruning
    trios.sort(key=lambda x: x[0] + x[1] + x[2])
    
    # Precompute bitmask for each trio
    masks = []
    for a, b, c in trios:
        masks.append((1 << (a-1)) | (1 << (b-1)) | (1 << (c-1)))
    
    full_mask = (1 << n) - 1
    chosen = []
    
    # Backtracking
    def dfs(idx, used_mask, current_sum, count):
        if count == q:
            return used_mask == full_mask and current_sum == target_sum
        if idx >= len(trios):
            return False
        # Prune: if remaining trios can't cover remaining operators
        remaining_ops = n - bin(used_mask).count("1")
        if remaining_ops > (q - count) * 3:
            return False
        # Try including this trio
        mask = masks[idx]
        if (used_mask & mask) == 0:
            a, b, c = trios[idx]
            chosen.append((a, b, c))
            if dfs(idx + 1, used_mask | mask, current_sum + a + b + c, count + 1):
                return True
            chosen.pop()
        # Try skipping this trio
        return dfs(idx + 1, used_mask, current_sum, count)
    
    if dfs(0, 0, 0, 0):
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()