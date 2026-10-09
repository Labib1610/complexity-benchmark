import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    triples = []
    idx = 2
    # store for each processor: list of (sensor, transmitter)
    options = [[] for _ in range(k)]
    for _ in range(t):
        x = int(data[idx]) - 1
        y = int(data[idx+1]) - 1
        z = int(data[idx+2]) - 1
        idx += 3
        options[x].append((y, z))
    
    full_mask = (1 << k) - 1
    memo = {}
    chosen = []
    
    def dfs(pmask, smask, tmask):
        if pmask == full_mask:
            return True
        key = (pmask, smask, tmask)
        if key in memo:
            return False  # already failed
        # pick processor with fewest options
        best = -1
        best_len = 10**9
        for i in range(k):
            if not (pmask >> i) & 1:
                cnt = 0
                for y, z in options[i]:
                    if not (smask >> y) & 1 and not (tmask >> z) & 1:
                        cnt += 1
                if cnt < best_len:
                    best_len = cnt
                    best = i
                    if cnt == 0:
                        break
        if best_len == 0:
            memo[key] = True
            return False
        # try options
        for y, z in options[best]:
            if not (smask >> y) & 1 and not (tmask >> z) & 1:
                chosen.append((best, y, z))
                if dfs(pmask | (1 << best), smask | (1 << y), tmask | (1 << z)):
                    return True
                chosen.pop()
        memo[key] = True
        return False
    
    if dfs(0, 0, 0):
        print("YES")
        for x, y, z in chosen:
            print(x+1, y+1, z+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()