import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Precompute valid pairs (sa, sb) such that M(a->b) != M(b->a)
    # M(a->b) = (17*sa^3 + 27*sb^2) mod 64
    valid_pairs = [[False] * 3 for _ in range(3)]
    for sa in range(1, 4):
        for sb in range(1, 4):
            m_ab = (17 * (sa ** 3) + 27 * (sb ** 2)) % 64
            m_ba = (17 * (sb ** 3) + 27 * (sa ** 2)) % 64
            if m_ab != m_ba:
                valid_pairs[sa-1][sb-1] = True
    
    # Backtracking with pruning
    assignment = [0] * n
    
    def backtrack(i):
        if i == n:
            return True
        
        # Determine valid choices for oscillator i
        # We need to check constraints with all previously assigned neighbors
        for s in range(1, 4):
            valid = True
            for neighbor in adj[i]:
                if neighbor < i:  # neighbor already assigned
                    if not valid_pairs[s-1][assignment[neighbor]-1]:
                        valid = False
                        break
            if valid:
                assignment[i] = s
                if backtrack(i + 1):
                    return True
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, assignment)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()