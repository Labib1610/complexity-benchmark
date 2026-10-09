import sys
from itertools import permutations

def solve():
    input = sys.stdin.readline
    n, m, B = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u-1, v-1))
    
    # Try brute force if n small
    if n <= 8:
        for perm in permutations(range(n)):
            pos = [0]*n
            for slot, sat in enumerate(perm):
                pos[sat] = slot
            total = 0
            ok = True
            for u,v in edges:
                total += abs(pos[u] - pos[v])
                if total > B:
                    ok = False
                    break
            if ok:
                print("YES")
                print(" ".join(str(p+1) for p in perm))
                return
        print("NO")
        return
    
    # Fallback: try ID order
    pos = list(range(n))
    total = 0
    for u,v in edges:
        total += abs(pos[u] - pos[v])
    if total <= B:
        print("YES")
        print(" ".join(str(p+1) for p in pos))
        return
    
    # Try reverse
    pos = list(range(n-1, -1, -1))
    total = 0
    for u,v in edges:
        total += abs(pos[u] - pos[v])
    if total <= B:
        print("YES")
        print(" ".join(str(p+1) for p in pos))
        return
    
    print("NO")

if __name__ == "__main__":
    solve()