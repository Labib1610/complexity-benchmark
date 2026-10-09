import sys
from itertools import combinations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list for prohibited pairs
    prohibited = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        prohibited[u].add(v)
        prohibited[v].add(u)
        idx += 2

    # Check all combinations of 3 materials in lexicographical order
    for a, b, c in combinations(range(1, n + 1), 3):
        # Check if all three pairs are prohibited
        if (b in prohibited[a] and 
            c in prohibited[a] and 
            c in prohibited[b]):
            print(a, b, c)
            return

if __name__ == "__main__":
    main()