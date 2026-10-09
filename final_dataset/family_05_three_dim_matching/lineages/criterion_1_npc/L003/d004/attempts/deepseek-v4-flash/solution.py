import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    triples = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        triples.append((x-1, y-1, z-1))  # 0-index

    # Group by foundation
    by_foundation = [[] for _ in range(k)]
    for x, y, z in triples:
        by_foundation[x].append((y, z))

    # We'll try to assign each foundation a unique (shaft, capital)
    used_shaft = 0
    used_cap = 0
    assignment = [None] * k

    # Memoization: (foundation_index, used_shaft_mask, used_cap_mask) -> bool
    memo = {}

    def dfs(i, used_shaft, used_cap):
        if i == k:
            return True
        key = (i, used_shaft, used_cap)
        if key in memo:
            return memo[key]
        for y, z in by_foundation[i]:
            if not (used_shaft & (1 << y)) and not (used_cap & (1 << z)):
                assignment[i] = (i, y, z)
                if dfs(i+1, used_shaft | (1 << y), used_cap | (1 << z)):
                    memo[key] = True
                    return True
        memo[key] = False
        return False

    if dfs(0, 0, 0):
        print("YES")
        for x, y, z in assignment:
            print(x+1, y+1, z+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()