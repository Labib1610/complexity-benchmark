import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    blocks = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        blocks.append((x, y, z))
    
    # Group blocks by shape
    by_shape = [[] for _ in range(k+1)]
    for x, y, z in blocks:
        by_shape[x].append((y, z))
    
    # Pre-check: each shape must have at least one block
    for s in range(1, k+1):
        if not by_shape[s]:
            print("NO")
            return
    
    # Backtracking
    chosen = [None] * (k+1)
    used_color = 0
    used_material = 0
    
    # Sort shapes by number of options (smallest first) for pruning
    order = list(range(1, k+1))
    order.sort(key=lambda s: len(by_shape[s]))
    
    def dfs(idx):
        nonlocal used_color, used_material
        if idx == k:
            return True
        s = order[idx]
        for y, z in by_shape[s]:
            if (used_color >> (y-1)) & 1:
                continue
            if (used_material >> (z-1)) & 1:
                continue
            chosen[s] = (s, y, z)
            used_color |= (1 << (y-1))
            used_material |= (1 << (z-1))
            if dfs(idx+1):
                return True
            used_color ^= (1 << (y-1))
            used_material ^= (1 << (z-1))
            chosen[s] = None
        return False
    
    if dfs(0):
        print("YES")
        for s in range(1, k+1):
            print(*chosen[s])
    else:
        print("NO")

if __name__ == "__main__":
    solve()