import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    vectors = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        vectors.append((x-1, y-1, z-1))  # 0-index for bitmasking

    # Group vectors by x for faster lookup
    by_x = [[] for _ in range(k)]
    for idx, (x, y, z) in enumerate(vectors):
        by_x[x].append((y, z, idx))

    used_y = 0
    used_z = 0
    chosen = []

    # Backtracking
    def dfs(x):
        if x == k:
            return True
        for y, z, idx in by_x[x]:
            if (used_y >> y) & 1 or (used_z >> z) & 1:
                continue
            used_y |= (1 << y)
            used_z |= (1 << z)
            chosen.append(vectors[idx])
            if dfs(x + 1):
                return True
            chosen.pop()
            used_y ^= (1 << y)
            used_z ^= (1 << z)
        return False

    if dfs(0):
        print("YES")
        for x, y, z in chosen:
            print(x+1, y+1, z+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()