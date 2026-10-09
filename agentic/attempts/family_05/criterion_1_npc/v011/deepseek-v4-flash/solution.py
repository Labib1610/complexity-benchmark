import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    triples = []
    for _ in range(t):
        m, p, s = map(int, input().split())
        triples.append((m-1, p-1, s-1))
    
    # Precompute for each membrane, list of triples
    by_m = [[] for _ in range(k)]
    for idx, (m, p, s) in enumerate(triples):
        by_m[m].append(idx)
    
    used_p = 0
    used_s = 0
    chosen = []
    
    # Backtracking
    def dfs(mask_m):
        if mask_m == (1 << k) - 1:
            return True
        # find first unused membrane
        m = 0
        while (mask_m >> m) & 1:
            m += 1
        for idx in by_m[m]:
            mm, p, s = triples[idx]
            if (used_p >> p) & 1:
                continue
            if (used_s >> s) & 1:
                continue
            # choose
            chosen.append(idx)
            used_p |= (1 << p)
            used_s |= (1 << s)
            if dfs(mask_m | (1 << mm)):
                return True
            # backtrack
            chosen.pop()
            used_p &= ~(1 << p)
            used_s &= ~(1 << s)
        return False
    
    if dfs(0):
        print("YES")
        for idx in chosen:
            m, p, s = triples[idx]
            print(m+1, p+1, s+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()