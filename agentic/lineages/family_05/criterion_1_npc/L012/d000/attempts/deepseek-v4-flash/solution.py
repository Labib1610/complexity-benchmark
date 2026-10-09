import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    candidates = [[] for _ in range(k)]
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        candidates[x].append((1 << y, 1 << z, y + 1, z + 1))
    
    # If any depth has no candidates, impossible
    for i in range(k):
        if not candidates[i]:
            print("NO")
            return
    
    # Sort depths by number of candidates (fewest first)
    order = sorted(range(k), key=lambda i: len(candidates[i]))
    
    chosen = [None] * k
    
    def dfs(idx, usedY, usedZ):
        if idx == k:
            return True
        
        remaining = k - idx
        
        # Quick prune: not enough distinct y or z left
        if bin(usedY).count("1") < remaining or bin(usedZ).count("1") < remaining:
            return False
        
        # Prune: any remaining depth has no available candidate
        for i in range(idx, k):
            x = order[i]
            ok = False
            for y_bit, z_bit, _, _ in candidates[x]:
                if not (usedY & y_bit) and not (usedZ & z_bit):
                    ok = True
                    break
            if not ok:
                return False
        
        x = order[idx]
        for y_bit, z_bit, y_val, z_val in candidates[x]:
            if not (usedY & y_bit) and not (usedZ & z_bit):
                chosen[x] = (y_val, z_val)
                if dfs(idx + 1, usedY | y_bit, usedZ | z_bit):
                    return True
                chosen[x] = None
        return False
    
    if dfs(0, 0, 0):
        print("YES")
        for x in range(k):
            y_val, z_val = chosen[x]
            print(f"{x+1} {y_val} {z_val}")
    else:
        print("NO")

if __name__ == "__main__":
    solve()