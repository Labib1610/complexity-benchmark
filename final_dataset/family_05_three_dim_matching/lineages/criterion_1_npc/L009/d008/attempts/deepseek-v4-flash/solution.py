import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    paths = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        paths.append((x-1, y-1, z-1))  # 0-index for easier bitmasking

    # Group by x
    by_x = [[] for _ in range(k)]
    for x, y, z in paths:
        by_x[x].append((y, z))

    # We'll use bitmasks for used y and z
    full_mask = (1 << k) - 1
    chosen = []

    def dfs(idx, used_y, used_z):
        if idx == k:
            return True
        x = idx  # we will assign x in order 0..k-1
        for y, z in by_x[x]:
            if not (used_y >> y) & 1 and not (used_z >> z) & 1:
                chosen.append((x+1, y+1, z+1))
                if dfs(idx+1, used_y | (1 << y), used_z | (1 << z)):
                    return True
                chosen.pop()
        return False

    if dfs(0, 0, 0):
        print("YES")
        for x, y, z in chosen:
            print(x, y, z)
    else:
        print("NO")

if __name__ == "__main__":
    solve()