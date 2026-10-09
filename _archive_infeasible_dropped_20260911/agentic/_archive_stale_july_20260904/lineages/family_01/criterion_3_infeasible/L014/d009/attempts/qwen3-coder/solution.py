import sys
from itertools import combinations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list for prohibited pairs
    adj = [set() for _ in range(n + 1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        adj[u].add(v)
        adj[v].add(u)
        index += 2

    # Iterate through all combinations of 3 materials in lexicographical order
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            for c in range(b + 1, n + 1):
                # Check if all three pairs are prohibited (i.e., form a triangle in the complement graph)
                if b in adj[a] and c in adj[a] and c in adj[b]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()