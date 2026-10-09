import sys
from itertools import combinations

def find_bad_triplet(n, edges):
    # Build adjacency list
    adj = [set() for _ in range(n + 1)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # For each triplet, check if it forms a triangle (i.e., all three edges exist)
    # A triangle is the minimal bad configuration: no matter how you 2-color it,
    # at least one edge will be monochromatic.
    for a, b, c in combinations(range(1, n + 1), 3):
        if b in adj[a] and c in adj[a] and c in adj[b]:
            return (a, b, c)
    
    # The problem guarantees a solution exists, so we should never reach here.
    return None

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        edges.append((u, v))
        index += 2
    
    triplet = find_bad_triplet(n, edges)
    print(triplet[0], triplet[1], triplet[2])

if __name__ == "__main__":
    main()