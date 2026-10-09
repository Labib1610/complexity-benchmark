import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [0] * n
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    full = (1 << n) - 1
    memo = {}
    
    def max_clique(R, P, X):
        if P == 0 and X == 0:
            return bin(R).count('1')
        key = (R, P, X)
        if key in memo:
            return memo[key]
        best = 0
        pivot = P | X
        pivot_bit = pivot & (-pivot)
        candidates = P & ~pivot_bit
        c = candidates
        while c:
            v_bit = c & (-c)
            v = v_bit.bit_length() - 1
            new_R = R | v_bit
            new_P = P & adj[v]
            new_X = X & adj[v]
            res = max_clique(new_R, new_P, new_X)
            if res > best:
                best = res
            P ^= v_bit
            X |= v_bit
            c ^= v_bit
        memo[key] = best
        return best
    
    if max_clique(0, full, 0) > 3:
        print("NO")
        return
    
    color = [0] * n
    order = sorted(range(n), key=lambda x: bin(adj[x]).count('1'), reverse=True)
    
    def backtrack(pos):
        if pos == n:
            return True
        v = order[pos]
        used = 0
        av = adj[v]
        while av:
            b = av & (-av)
            u = b.bit_length() - 1
            if color[u]:
                used |= 1 << color[u]
            av ^= b
        for c in range(1, 5):
            if not (used & (1 << c)):
                color[v] = c
                if backtrack(pos + 1):
                    return True
                color[v] = 0
        return False
    
    if not backtrack(0):
        print("NO")
        return
    
    print("YES")
    print(' '.join(str(color[i]) for i in range(n)))

solve()