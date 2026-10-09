import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # allowed[x] = list of (y,z)
    allowed = [[] for _ in range(k+1)]
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        allowed[x].append((y-1, z-1))  # 0-index
    
    # Sort by number of options for better pruning
    order = list(range(1, k+1))
    order.sort(key=lambda x: len(allowed[x]))
    
    usedY = 0
    usedZ = 0
    assignment = [None] * (k+1)  # assignment[x] = (y,z)
    
    # Precompute for each x a list of (y,z) as bitmask-friendly
    # We'll just use lists.
    
    def dfs(idx):
        nonlocal usedY, usedZ
        if idx == k:
            return True
        x = order[idx]
        for y, z in allowed[x]:
            if (usedY >> y) & 1:
                continue
            if (usedZ >> z) & 1:
                continue
            # prune: remaining specialists must be <= remaining machines and times
            rem = k - idx - 1
            if rem > k - bin(usedY).count("1") - 1:
                continue
            if rem > k - bin(usedZ).count("1") - 1:
                continue
            usedY |= (1 << y)
            usedZ |= (1 << z)
            assignment[x] = (y+1, z+1)
            if dfs(idx+1):
                return True
            usedY ^= (1 << y)
            usedZ ^= (1 << z)
            assignment[x] = None
        return False
    
    if dfs(0):
        print("YES")
        for x in range(1, k+1):
            y, z = assignment[x]
            print(x, y, z)
    else:
        print("NO")

if __name__ == "__main__":
    solve()