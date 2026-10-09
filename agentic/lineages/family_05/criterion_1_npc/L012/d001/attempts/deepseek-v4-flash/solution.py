import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    points = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        points.append((x-1, y-1, z-1))  # 0-indexed

    # Group points by x for faster lookup
    by_x = [[] for _ in range(k)]
    for idx, (x, y, z) in enumerate(points):
        by_x[x].append((y, z, idx))

    used_y = 0
    used_z = 0
    chosen = []

    # Precompute for each x, the list of (y,z) pairs
    # We'll do DFS over x values 0..k-1
    # At each step, pick a point with this x not using used y or z

    sys.setrecursionlimit(10000)

    def dfs(x):
        nonlocal used_y, used_z
        if x == k:
            return True
        for y, z, idx in by_x[x]:
            if not (used_y & (1 << y)) and not (used_z & (1 << z)):
                used_y |= (1 << y)
                used_z |= (1 << z)
                chosen.append(points[idx])
                if dfs(x+1):
                    return True
                chosen.pop()
                used_y &= ~(1 << y)
                used_z &= ~(1 << z)
        return False

    if dfs(0):
        print("YES")
        for x, y, z in chosen:
            print(x+1, y+1, z+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()