import sys
from itertools import permutations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    B = int(data[2])
    
    edges = []
    for i in range(m):
        u = int(data[3 + 2*i]) - 1  # Convert to 0-based
        v = int(data[4 + 2*i]) - 1
        edges.append((u, v))
    
    # If n is small enough, try all permutations
    if n <= 8:
        for perm in permutations(range(n)):
            total = 0
            pos = [0] * n
            for i in range(n):
                pos[perm[i]] = i
            for u, v in edges:
                total += abs(pos[u] - pos[v])
            if total <= B:
                print("YES")
                print(' '.join(str(x + 1) for x in perm))
                return
        print("NO")
        return
    
    # For larger n, use a heuristic: place nodes in order of highest degree first
    # This is a greedy approach
    deg = [0] * n
    adj = [[] for _ in range(n)]
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Sort nodes by degree descending
    nodes = list(range(n))
    nodes.sort(key=lambda x: deg[x], reverse=True)
    
    # Try to place them in order, minimizing stretch
    pos = [-1] * n
    placed = [False] * n
    pos[nodes[0]] = 0
    placed[nodes[0]] = True
    
    # For each subsequent node, place it in the position that minimizes total stretch
    for i in range(1, n):
        u = nodes[i]
        best_pos = -1
        best_cost = float('inf')
        # Try all available positions
        for p in range(n):
            if pos[p] != -1:
                continue
            # Calculate cost if we place u at position p
            cost = 0
            for v in adj[u]:
                if placed[v]:
                    cost += abs(p - pos[v])
            if cost < best_cost:
                best_cost = cost
                best_pos = p
        pos[u] = best_pos
        placed[u] = True
    
    # Now compute total stretch
    total = 0
    for u, v in edges:
        total += abs(pos[u] - pos[v])
    
    if total <= B:
        # Create result permutation
        result = [0] * n
        for i in range(n):
            result[pos[i]] = i + 1
        print("YES")
        print(' '.join(map(str, result)))
        return
    
    # If greedy fails, try a few random permutations
    import random
    for _ in range(1000):
        perm = list(range(n))
        random.shuffle(perm)
        pos = [0] * n
        for i in range(n):
            pos[perm[i]] = i
        total = 0
        for u, v in edges:
            total += abs(pos[u] - pos[v])
        if total <= B:
            print("YES")
            print(' '.join(str(x + 1) for x in perm))
            return
    
    print("NO")

if __name__ == "__main__":
    main()