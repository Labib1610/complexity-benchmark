import sys
from itertools import combinations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    adj = [set() for _ in range(n + 1)]
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Find all triangles (3-cliques) in the graph
    # A triangle is a set of three nodes where each pair is connected
    min_trace = float('inf')
    result = None
    
    # For each combination of 3 nodes, check if they form a triangle
    for combo in combinations(range(1, n + 1), 3):
        a, b, c = sorted(combo)
        if b in adj[a] and c in adj[a] and c in adj[b]:
            # It's a triangle
            trace = a * (10**8) + b * (10**4) + c
            if trace < min_trace:
                min_trace = trace
                result = (a, b, c)
    
    print(result[0], result[1], result[2])

if __name__ == "__main__":
    main()