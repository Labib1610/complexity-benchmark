import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    adj_mask = [0] * n
    for _ in range(m):
        u = int(data[idx]) - 1; idx += 1
        v = int(data[idx]) - 1; idx += 1
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
    
    colors = [0] * n
    colors_mask = [0, 0, 0, 0]
    assigned_mask = 0
    
    def forward_check(v, c):
        neighbors = adj_mask[v]
        unassigned = neighbors & ~assigned_mask
        u = unassigned
        while u:
            bit = u & -u
            u_idx = bit.bit_length() - 1
            blocked = 0
            for c2 in [1, 2, 3]:
                if (adj_mask[u_idx] & colors_mask[c2]) != 0:
                    blocked += 1
                elif c2 == c:
                    blocked += 1
            if blocked == 3:
                return False
            u ^= bit
        return True
    
    def backtrack(v):
        nonlocal assigned_mask
        if v == n:
            return True
        for c in [1, 2, 3]:
            if (adj_mask[v] & colors_mask[c]) == 0:
                colors[v] = c
                colors_mask[c] |= (1 << v)
                assigned_mask |= (1 << v)
                if forward_check(v, c) and backtrack(v + 1):
                    return True
                assigned_mask ^= (1 << v)
                colors_mask[c] ^= (1 << v)
                colors[v] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, colors)))
    else:
        print("NO")

solve()