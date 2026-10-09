import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    constraints = []
    for _ in range(m):
        v = [int(next(it)) for _ in range(3)]
        constraints.append(v)
    
    # Try all 2^n configurations
    for mask in range(1 << n):
        ok = True
        for c in constraints:
            satisfied = False
            for x in c:
                idx = abs(x) - 1
                desired = 1 if x > 0 else 0
                actual = (mask >> idx) & 1
                if actual == desired:
                    satisfied = True
                    break
            if not satisfied:
                ok = False
                break
        if ok:
            print("YES")
            print(' '.join(str((mask >> i) & 1) for i in range(n)))
            return
    
    print("NO")

if __name__ == "__main__":
    solve()