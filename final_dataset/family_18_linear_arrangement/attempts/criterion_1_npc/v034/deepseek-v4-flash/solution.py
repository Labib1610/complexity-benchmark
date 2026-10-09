import sys
from itertools import permutations

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    K = int(data[2])
    edges = []
    idx = 3
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        idx += 2
        edges.append((u, v))
    
    for perm in permutations(range(n)):
        pos = [0] * n
        for i, p in enumerate(perm):
            pos[p] = i
        total = 0
        for u, v in edges:
            total += abs(pos[u] - pos[v])
            if total > K:
                break
        if total <= K:
            print("YES")
            print(" ".join(str(p+1) for p in perm))
            return
    print("NO")

if __name__ == "__main__":
    main()