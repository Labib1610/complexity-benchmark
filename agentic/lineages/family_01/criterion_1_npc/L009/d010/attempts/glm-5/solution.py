import sys

def solve():
    data = sys.stdin.read().split()
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
    
    # Precompute valid pairs: valid[a][b] is True if pair (a,b) is stable
    # H(a,b) = 2ab/(a+b) must NOT be an integer
    valid = [[False] * 4 for _ in range(4)]
    for a in range(1, 4):
        for b in range(1, 4):
            num = 2 * a * b
            den = a + b
            if num % den != 0:
                valid[a][b] = True
    
    # Backtracking with pruning
    c = [0] * n
    
    def backtrack(i):
        if i == n:
            return True
        
        for val in range(1, 4):
            ok = True
            for j in adj[i]:
                if j < i:
                    if not valid[c[j]][val]:
                        ok = False
                        break
            if ok:
                c[i] = val
                if backtrack(i + 1):
                    return True
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, c)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()