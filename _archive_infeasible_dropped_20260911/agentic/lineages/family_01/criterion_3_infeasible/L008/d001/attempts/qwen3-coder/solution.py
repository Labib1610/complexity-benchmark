import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list representation of the graph
    adj = defaultdict(set)
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        adj[u].add(v)
        adj[v].add(u)
        index += 2

    # Convert to list for ordered iteration
    nodes = list(range(1, n+1))
    
    # Iterate through all triplets (i, j, k) in lexicographical order
    for i in nodes:
        for j in nodes:
            if j <= i:
                continue
            if j not in adj[i]:
                continue
            for k in nodes:
                if k <= j:
                    continue
                if k not in adj[i]:
                    continue
                if k not in adj[j]:
                    continue
                # Found a triangle: i-j, i-k, j-k
                print(i, j, k)
                return

if __name__ == "__main__":
    main()