import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    paths_by_x = [[] for _ in range(k+1)]
    for _ in range(t):
        x, y, z = map(int, input().split())
        paths_by_x[x].append((y, z))
    
    # If any x has no paths, impossible
    for x in range(1, k+1):
        if not paths_by_x[x]:
            print("NO")
            return
    
    # Sort each list maybe for deterministic order
    for x in range(1, k+1):
        paths_by_x[x].sort()
    
    used_y = 0
    used_z = 0
    chosen = [None] * (k+1)
    
    # Precompute for pruning: for each x, list of (y,z) pairs
    # We'll do DFS
    sys.setrecursionlimit(1000000)
    
    def dfs(x):
        nonlocal used_y, used_z
        if x > k:
            return True
        # Prune: if remaining x's cannot be matched because not enough unused y or z
        remaining = k - x + 1
        if bin(used_y).count('1') + remaining > k or bin(used_z).count('1') + remaining > k:
            return False
        for y, z in paths_by_x[x]:
            if not (used_y >> (y-1)) & 1 and not (used_z >> (z-1)) & 1:
                used_y |= (1 << (y-1))
                used_z |= (1 << (z-1))
                chosen[x] = (x, y, z)
                if dfs(x+1):
                    return True
                used_y ^= (1 << (y-1))
                used_z ^= (1 << (z-1))
        return False
    
    if dfs(1):
        print("YES")
        for x in range(1, k+1):
            print(*chosen[x])
    else:
        print("NO")

if __name__ == "__main__":
    solve()