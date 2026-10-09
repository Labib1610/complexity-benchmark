import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    paths = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        paths.append((x, y, z))
    
    # Group by x
    by_x = [[] for _ in range(k+1)]
    for x, y, z in paths:
        by_x[x].append((y, z))
    
    used_y = [False] * (k+1)
    used_z = [False] * (k+1)
    chosen = []
    
    def dfs(x):
        if x > k:
            return True
        for y, z in by_x[x]:
            if not used_y[y] and not used_z[z]:
                used_y[y] = True
                used_z[z] = True
                chosen.append((x, y, z))
                if dfs(x+1):
                    return True
                chosen.pop()
                used_y[y] = False
                used_z[z] = False
        return False
    
    if dfs(1):
        print("YES")
        for x, y, z in chosen:
            print(x, y, z)
    else:
        print("NO")

if __name__ == "__main__":
    solve()