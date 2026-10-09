import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    configs = [[] for _ in range(k + 1)]
    for _ in range(t):
        x, y, z = map(int, input().split())
        configs[x].append((y, z))
    
    # Sort configs for each specialist to try smaller options first
    for i in range(1, k + 1):
        configs[i].sort()
    
    used_mach = [False] * (k + 1)
    used_shift = [False] * (k + 1)
    ans = [None] * (k + 1)
    
    def dfs(spec):
        if spec > k:
            return True
        for y, z in configs[spec]:
            if not used_mach[y] and not used_shift[z]:
                used_mach[y] = True
                used_shift[z] = True
                ans[spec] = (spec, y, z)
                if dfs(spec + 1):
                    return True
                used_mach[y] = False
                used_shift[z] = False
        return False
    
    if dfs(1):
        print("YES")
        for i in range(1, k + 1):
            print(*ans[i])
    else:
        print("NO")

if __name__ == "__main__":
    solve()