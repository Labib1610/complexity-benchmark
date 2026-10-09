import sys
from itertools import combinations

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    forbidden = set()
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        forbidden.add((min(u, v), max(u, v)))
    
    # Try all subsets of size k
    for combo in combinations(range(1, n + 1), k):
        valid = True
        for i in range(k):
            for j in range(i + 1, k):
                a, b = combo[i], combo[j]
                if (min(a, b), max(a, b)) in forbidden:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            print("YES")
            print(' '.join(map(str, combo)))
            return
    
    print("NO")

if __name__ == "__main__":
    solve()