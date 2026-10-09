import sys
from itertools import permutations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    B = int(data[idx])
    idx += 1
    
    edges = []
    for _ in range(m):
        u = int(data[idx]) - 1
        idx += 1
        v = int(data[idx]) - 1
        idx += 1
        edges.append((u, v))
    
    # Try all permutations
    for perm in permutations(range(n)):
        total = 0
        pos = [0] * n
        for i in range(n):
            pos[perm[i]] = i
        
        for u, v in edges:
            total += abs(pos[u] - pos[v])
        
        if total <= B:
            print("YES")
            print(' '.join(str(x+1) for x in perm))
            return
    
    print("NO")

if __name__ == "__main__":
    main()