import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    k = int(next(it))
    t = int(next(it))
    
    routes_by_source = [[] for _ in range(k)]
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        routes_by_source[x].append((y, z))
    
    # Sort routes for deterministic behavior
    for i in range(k):
        routes_by_source[i].sort()
    
    full_mask = (1 << k) - 1
    chosen = []
    
    def dfs(src_mask, trans_mask, dest_mask, count):
        if count == k:
            return True
        # Find first unused source
        for s in range(k):
            if not (src_mask >> s) & 1:
                break
        else:
            return False
        
        for y, z in routes_by_source[s]:
            if (trans_mask >> y) & 1:
                continue
            if (dest_mask >> z) & 1:
                continue
            chosen.append((s, y, z))
            if dfs(src_mask | (1 << s), trans_mask | (1 << y), dest_mask | (1 << z), count + 1):
                return True
            chosen.pop()
        return False
    
    if dfs(0, 0, 0, 0):
        print("YES")
        for x, y, z in chosen:
            print(x + 1, y + 1, z + 1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()