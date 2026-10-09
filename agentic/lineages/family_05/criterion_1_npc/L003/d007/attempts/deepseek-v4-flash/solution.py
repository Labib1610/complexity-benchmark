import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    modules = [[] for _ in range(k + 1)]
    for _ in range(t):
        x, y, z = map(int, input().split())
        modules[x].append((y, z))
    
    used_y = [False] * (k + 1)
    used_z = [False] * (k + 1)
    chosen = [None] * (k + 1)  # chosen[x] = (y, z)
    
    def dfs(x):
        if x > k:
            return True
        for y, z in modules[x]:
            if not used_y[y] and not used_z[z]:
                used_y[y] = True
                used_z[z] = True
                chosen[x] = (y, z)
                if dfs(x + 1):
                    return True
                used_y[y] = False
                used_z[z] = False
        return False
    
    if dfs(1):
        print("YES")
        for x in range(1, k + 1):
            y, z = chosen[x]
            print(x, y, z)
    else:
        print("NO")

if __name__ == "__main__":
    solve()