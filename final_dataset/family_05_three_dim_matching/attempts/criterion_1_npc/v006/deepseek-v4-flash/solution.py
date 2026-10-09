import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    allowed = [[] for _ in range(k)]  # allowed[z] = list of (x, y)
    for _ in range(t):
        x, y, z = map(int, input().split())
        allowed[z-1].append((x-1, y-1))
    
    # Sort each list to have deterministic order
    for z in range(k):
        allowed[z].sort()
    
    # Backtracking
    used_x = 0
    used_y = 0
    schedule = [None] * k  # schedule[z] = (x, y)
    
    # Precompute possible pairs for each z
    # We'll try to assign time blocks in order
    def dfs(z):
        nonlocal used_x, used_y
        if z == k:
            return True
        for x, y in allowed[z]:
            if not (used_x >> x) & 1 and not (used_y >> y) & 1:
                used_x |= (1 << x)
                used_y |= (1 << y)
                schedule[z] = (x, y)
                if dfs(z+1):
                    return True
                used_x ^= (1 << x)
                used_y ^= (1 << y)
        return False
    
    if dfs(0):
        print("YES")
        for z in range(k):
            x, y = schedule[z]
            print(x+1, y+1, z+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()