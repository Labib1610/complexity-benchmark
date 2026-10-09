import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    k = int(next(it))
    t = int(next(it))
    
    triples = []
    for _ in range(t):
        m = int(next(it)) - 1
        p = int(next(it)) - 1
        s = int(next(it)) - 1
        triples.append((m, p, s))
    
    # Group triples by membrane for faster search
    by_m = [[] for _ in range(k)]
    for idx, (m, p, s) in enumerate(triples):
        by_m[m].append(idx)
    
    used_p = 0
    used_s = 0
    chosen = []
    
    # Precompute masks for each triple
    p_mask = [1 << p for _, p, _ in triples]
    s_mask = [1 << s for _, _, s in triples]
    
    full_mask = (1 << k) - 1
    
    # Backtracking
    def dfs(m_idx):
        nonlocal used_p, used_s
        if m_idx == k:
            return used_p == full_mask and used_s == full_mask
        
        # Try triples with this membrane
        for idx in by_m[m_idx]:
            m, p, s = triples[idx]
            if (used_p >> p) & 1:
                continue
            if (used_s >> s) & 1:
                continue
            # choose
            used_p |= (1 << p)
            used_s |= (1 << s)
            chosen.append((m + 1, p + 1, s + 1))
            if dfs(m_idx + 1):
                return True
            # backtrack
            chosen.pop()
            used_p &= ~(1 << p)
            used_s &= ~(1 << s)
        return False
    
    if dfs(0):
        print("YES")
        for m, p, s in chosen:
            print(m, p, s)
    else:
        print("NO")

if __name__ == "__main__":
    solve()