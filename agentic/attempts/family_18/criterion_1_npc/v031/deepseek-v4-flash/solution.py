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
    
    # For small n, brute force all permutations
    if n <= 9:
        best_perm = None
        for perm in permutations(range(n)):
            pos = [0] * n
            for idx, val in enumerate(perm):
                pos[val] = idx + 1  # 1-based positions
            total = 0
            for u, v in edges:
                total += abs(pos[u] - pos[v])
                if total > B:
                    break
            if total <= B:
                best_perm = perm
                break
        if best_perm is None:
            print("NO")
        else:
            pos = [0] * n
            for idx, val in enumerate(best_perm):
                pos[val] = idx + 1
            print("YES")
            print(" ".join(map(str, pos)))
        return
    
    # For larger n, use a greedy heuristic: place vertices with high degree near center
    # Simple heuristic: sort by degree descending, place them alternating from center outward
    deg = [0] * n
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    
    order = sorted(range(n), key=lambda x: -deg[x])
    pos = [0] * n
    left = n // 2
    right = left + 1
    # place high degree in center
    for i, v in enumerate(order):
        if i % 2 == 0:
            if left >= 1:
                pos[v] = left
                left -= 1
            else:
                pos[v] = right
                right += 1
        else:
            if right <= n:
                pos[v] = right
                right += 1
            else:
                pos[v] = left
                left -= 1
    
    total = 0
    for u, v in edges:
        total += abs(pos[u] - pos[v])
    if total <= B:
        print("YES")
        print(" ".join(map(str, pos)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()