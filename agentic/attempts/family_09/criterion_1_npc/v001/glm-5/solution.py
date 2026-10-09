import sys
sys.setrecursionlimit(100000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    # Generate maximal independent sets
    all_vertices = (1 << (n + 1)) - 1
    for i in range(1, n + 1):
        all_vertices |= 1 << i
    
    max_sets = []
    
    def bronk(R, P, X):
        if P == 0 and X == 0:
            max_sets.append(R)
            return
        # Choose pivot u from P | X with max degree in P
        union = P | X
        # Find vertex with max |P & neighbors|
        pivot = -1
        max_cnt = -1
        bit = 1
        for v in range(1, n + 1):
            if union & (1 << v):
                cnt = bin(P & adj[v]).count('1')
                if cnt > max_cnt:
                    max_cnt = cnt
                    pivot = v
            bit <<= 1
        
        # Candidates: P - neighbors(pivot)
        candidates = P & ~adj[pivot]
        while candidates:
            # Pick lowest bit
            v = (candidates & -candidates).bit_length() - 1
            v_bit = 1 << v
            bronk(R | v_bit, P & adj[v], X & adj[v])
            P &= ~v_bit
            candidates &= ~v_bit
            X |= v_bit
    
    R = 0
    P = 0
    for i in range(1, n + 1):
        P |= 1 << i
    X = 0
    
    bronk(R, P, X)
    
    for ms in max_sets:
        if bin(ms).count('1') >= k:
            cnt = 0
            res = []
            for v in range(1, n + 1):
                if ms & (1 << v):
                    res.append(str(v))
                    cnt += 1
                    if cnt == k:
                        break
            print("YES")
            print(' '.join(res))
            return
    
    print("NO")

if __name__ == "__main__":
    solve()