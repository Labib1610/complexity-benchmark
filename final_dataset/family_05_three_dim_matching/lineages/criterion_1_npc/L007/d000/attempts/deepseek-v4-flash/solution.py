import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # For each enzyme, store list of (s, p)
    adj = [[] for _ in range(k)]
    for _ in range(t):
        e = int(next(it)) - 1
        s = int(next(it)) - 1
        p = int(next(it)) - 1
        adj[e].append((s, p))
    
    # Sort maybe to help pruning? Not necessary.
    
    used_s = 0
    used_p = 0
    chosen = [None] * k
    
    # Precompute full mask
    full_mask = (1 << k) - 1
    
    # Recursive function
    def dfs(e_idx, used_s, used_p):
        if e_idx == k:
            return True
        for s, p in adj[e_idx]:
            if (used_s >> s) & 1:
                continue
            if (used_p >> p) & 1:
                continue
            chosen[e_idx] = (e_idx + 1, s + 1, p + 1)
            if dfs(e_idx + 1, used_s | (1 << s), used_p | (1 << p)):
                return True
        return False
    
    if dfs(0, 0, 0):
        out = ["YES"]
        for e, s, p in chosen:
            out.append(f"{e} {s} {p}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()