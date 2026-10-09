import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    candidates = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        candidates.append((x, y, z))
    
    # Group by frequency for quick lookup
    by_freq = [[] for _ in range(k+1)]
    for idx, (x, y, z) in enumerate(candidates):
        by_freq[x].append(idx)
    
    used_key = [False]*(k+1)
    used_pol = [False]*(k+1)
    chosen = []
    
    # Backtracking over frequencies
    def dfs(freq):
        if freq > k:
            return len(chosen) == k
        # Try to pick a candidate with this frequency
        for idx in by_freq[freq]:
            x, y, z = candidates[idx]
            if not used_key[y] and not used_pol[z]:
                used_key[y] = True
                used_pol[z] = True
                chosen.append((x, y, z))
                if dfs(freq+1):
                    return True
                chosen.pop()
                used_key[y] = False
                used_pol[z] = False
        # Or skip this frequency (if we still have enough frequencies left)
        if (k - freq) >= (k - len(chosen)):
            if dfs(freq+1):
                return True
        return False
    
    if dfs(1):
        print("YES")
        for x, y, z in chosen:
            print(x, y, z)
    else:
        print("NO")

if __name__ == "__main__":
    solve()