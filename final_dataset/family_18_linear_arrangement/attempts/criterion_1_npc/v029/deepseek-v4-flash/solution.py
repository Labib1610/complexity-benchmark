import sys
from itertools import permutations

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n, m, B = map(int, data[:3])
    edges = []
    idx = 3
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        idx += 2
        edges.append((u, v))
    
    # Try all permutations
    for perm in permutations(range(n)):
        pos = [0] * n
        for i, p in enumerate(perm):
            pos[p] = i + 1  # bay positions 1..n
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
    main()