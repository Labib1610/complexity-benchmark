import sys

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
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
    
    # Greedy placement: place nodes in order 1..n at positions 1..n
    # This minimizes total distance for edges connecting nodes with close indices
    pos = list(range(n + 1))  # pos[i] = i
    
    # Calculate total stretch
    total = 0
    for u, v in edges:
        total += abs(pos[u] - pos[v])
    
    if total <= B:
        print("YES")
        print(' '.join(map(str, pos[1:])))
        return
    
    # Try reverse placement
    pos_rev = [0] + list(range(n, 0, -1))
    total = 0
    for u, v in edges:
        total += abs(pos_rev[u] - pos_rev[v])
    
    if total <= B:
        print("YES")
        print(' '.join(map(str, pos_rev[1:])))
        return
    
    # Try other simple permutations
    # Alternating: 1, n, 2, n-1, ...
    pos_alt = [0] * (n + 1)
    left, right = 1, n
    for i in range(1, n + 1):
        if i % 2 == 1:
            pos_alt[i] = left
            left += 1
        else:
            pos_alt[i] = right
            right -= 1
    
    total = 0
    for u, v in edges:
        total += abs(pos_alt[u] - pos_alt[v])
    
    if total <= B:
        print("YES")
        print(' '.join(map(str, pos_alt[1:])))
        return
    
    # Try reverse alternating
    pos_alt2 = [0] * (n + 1)
    left, right = 1, n
    for i in range(1, n + 1):
        if i % 2 == 0:
            pos_alt2[i] = left
            left += 1
        else:
            pos_alt2[i] = right
            right -= 1
    
    total = 0
    for u, v in edges:
        total += abs(pos_alt2[u] - pos_alt2[v])
    
    if total <= B:
        print("YES")
        print(' '.join(map(str, pos_alt2[1:])))
        return
    
    print("NO")

if __name__ == "__main__":
    solve()