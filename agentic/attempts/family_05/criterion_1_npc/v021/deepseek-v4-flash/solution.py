import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    points_by_x = [[] for _ in range(k + 1)]
    for _ in range(t):
        x, y, z = map(int, input().split())
        points_by_x[x].append((y, z))
    
    # If any x has no points, impossible
    for x in range(1, k + 1):
        if not points_by_x[x]:
            print("NO")
            return
    
    used_y = 0
    used_z = 0
    chosen = [None] * (k + 1)
    
    # Sort points by x to have deterministic order
    for x in range(1, k + 1):
        points_by_x[x].sort()
    
    def dfs(x):
        nonlocal used_y, used_z
        if x > k:
            return True
        for y, z in points_by_x[x]:
            if not (used_y >> (y - 1)) & 1 and not (used_z >> (z - 1)) & 1:
                used_y |= 1 << (y - 1)
                used_z |= 1 << (z - 1)
                chosen[x] = (x, y, z)
                if dfs(x + 1):
                    return True
                used_y ^= 1 << (y - 1)
                used_z ^= 1 << (z - 1)
        return False
    
    if dfs(1):
        print("YES")
        for x in range(1, k + 1):
            print(*chosen[x])
    else:
        print("NO")

if __name__ == "__main__":
    solve()