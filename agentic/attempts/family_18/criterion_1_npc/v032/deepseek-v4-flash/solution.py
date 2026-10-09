import sys
import itertools

def main():
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
    
    # Try all permutations of slot assignments
    for perm in itertools.permutations(range(1, n+1)):
        # perm[i] = slot of module i
        total = 0
        for u, v in edges:
            total += abs(perm[u] - perm[v])
            if total > B:
                break
        if total <= B:
            print("YES")
            print(" ".join(map(str, perm)))
            return
    print("NO")

if __name__ == "__main__":
    main()