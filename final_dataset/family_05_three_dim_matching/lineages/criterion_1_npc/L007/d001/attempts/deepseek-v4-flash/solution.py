import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    adj = [[] for _ in range(k)]
    for _ in range(t):
        c = int(next(it)) - 1
        n = int(next(it)) - 1
        i = int(next(it)) - 1
        adj[c].append((n, i))
    
    # Remove duplicates just in case (though problem says no duplicates)
    for c in range(k):
        adj[c] = list(set(adj[c]))
    
    full_mask = (1 << k) - 1
    memo = {}
    
    def dfs(chassis_mask, nav_mask, sensor_mask):
        if chassis_mask == full_mask:
            return True
        key = (chassis_mask, nav_mask, sensor_mask)
        if key in memo:
            return False
        
        # find best chassis
        best_c = -1
        best_count = k + 1
        for c in range(k):
            if not (chassis_mask >> c) & 1:
                cnt = 0
                for (n, i) in adj[c]:
                    if not (nav_mask >> n) & 1 and not (sensor_mask >> i) & 1:
                        cnt += 1
                if cnt < best_count:
                    best_count = cnt
                    best_c = c
                    if cnt == 0:
                        break
        if best_count == 0:
            memo[key] = True
            return False
        
        # try each pair for best_c
        for (n, i) in adj[best_c]:
            if (nav_mask >> n) & 1 or (sensor_mask >> i) & 1:
                continue
            chosen.append((best_c + 1, n + 1, i + 1))
            if dfs(chassis_mask | (1 << best_c), nav_mask | (1 << n), sensor_mask | (1 << i)):
                return True
            chosen.pop()
        
        memo[key] = True
        return False
    
    chosen = []
    if dfs(0, 0, 0):
        print("YES")
        for c, n, i in chosen:
            print(c, n, i)
    else:
        print("NO")

if __name__ == "__main__":
    solve()