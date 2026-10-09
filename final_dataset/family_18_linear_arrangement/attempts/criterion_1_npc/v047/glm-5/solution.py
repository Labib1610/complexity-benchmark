import sys
from collections import defaultdict

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    adj = defaultdict(list)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    # Sort modules by degree (descending) for greedy placement
    modules = list(range(1, n + 1))
    modules.sort(key=lambda x: -len(adj[x]))
    
    # Greedy: place high-degree modules in center slots
    slots = list(range(1, n + 1))
    center_slots = sorted(slots, key=lambda x: abs(x - (n + 1) / 2))
    
    assignment = [0] * (n + 1)
    used = [False] * (n + 1)
    
    for i, mod in enumerate(modules):
        slot = center_slots[i]
        assignment[mod] = slot
        used[slot] = True
    
    # Calculate total cable length
    total = 0
    for u in range(1, n + 1):
        for v in adj[u]:
            if v > u:
                total += abs(assignment[u] - assignment[v])
    
    if total <= B:
        print("YES")
        print(' '.join(map(str, assignment[1:])))
        return
    
    # Try reverse order (low-degree in center)
    modules_rev = list(range(1, n + 1))
    modules_rev.sort(key=lambda x: len(adj[x]))
    
    assignment2 = [0] * (n + 1)
    for i, mod in enumerate(modules_rev):
        slot = center_slots[i]
        assignment2[mod] = slot
    
    total2 = 0
    for u in range(1, n + 1):
        for v in adj[u]:
            if v > u:
                total2 += abs(assignment2[u] - assignment2[v])
    
    if total2 <= B:
        print("YES")
        print(' '.join(map(str, assignment2[1:])))
        return
    
    # Try identity permutation
    assignment3 = list(range(n + 1))
    total3 = 0
    for u in range(1, n + 1):
        for v in adj[u]:
            if v > u:
                total3 += abs(assignment3[u] - assignment3[v])
    
    if total3 <= B:
        print("YES")
        print(' '.join(map(str, assignment3[1:])))
        return
    
    # Try reverse permutation
    assignment4 = [0] + list(range(n, 0, -1))
    total4 = 0
    for u in range(1, n + 1):
        for v in adj[u]:
            if v > u:
                total4 += abs(assignment4[u] - assignment4[v])
    
    if total4 <= B:
        print("YES")
        print(' '.join(map(str, assignment4[1:])))
        return
    
    # Try more permutations for small n
    if n <= 8:
        from itertools import permutations
        for perm in permutations(range(1, n + 1)):
            total_p = 0
            for u in range(1, n + 1):
                for v in adj[u]:
                    if v > u:
                        total_p += abs(perm[u-1] - perm[v-1])
            if total_p <= B:
                print("YES")
                print(' '.join(map(str, perm)))
                return
    
    print("NO")

if __name__ == "__main__":
    solve()