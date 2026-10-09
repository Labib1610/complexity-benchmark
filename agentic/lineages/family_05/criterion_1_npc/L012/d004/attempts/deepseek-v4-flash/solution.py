import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    points = []
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        points.append((x, y, z))
    
    # Sort points for better pruning
    points.sort()
    
    used_x = [False] * (k + 1)
    used_y = [False] * (k + 1)
    used_z = [False] * (k + 1)
    chosen = []
    
    def dfs(idx, count):
        if count == k:
            return True
        if idx == t:
            return False
        if t - idx < k - count:
            return False
        
        x, y, z = points[idx]
        
        # Try skipping
        if dfs(idx + 1, count):
            return True
        
        # Try taking if possible
        if not used_x[x] and not used_y[y] and not used_z[z]:
            used_x[x] = True
            used_y[y] = True
            used_z[z] = True
            chosen.append((x, y, z))
            if dfs(idx + 1, count + 1):
                return True
            chosen.pop()
            used_x[x] = False
            used_y[y] = False
            used_z[z] = False
        
        return False
    
    if dfs(0, 0):
        print("YES")
        for p in chosen:
            print(p[0], p[1], p[2])
    else:
        print("NO")

if __name__ == "__main__":
    solve()