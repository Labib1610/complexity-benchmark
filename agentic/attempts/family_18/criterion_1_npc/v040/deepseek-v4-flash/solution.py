import sys
from itertools import permutations

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
    
    # If no edges, any permutation works
    if m == 0:
        print("YES")
        print(" ".join(str(i+1) for i in range(n)))
        return
    
    # Try all permutations
    for perm in permutations(range(n)):
        pos = [0]*n
        for i, p in enumerate(perm):
            pos[p] = i+1  # bay number
        total = 0
        for u, v in edges:
            total += abs(pos[u] - pos[v])
            if total > B:
                break
        if total <= B:
            print("YES")
            print(" ".join(str(pos[i]) for i in range(n)))
            return
    
    print("NO")

if __name__ == "__main__":
    solve()