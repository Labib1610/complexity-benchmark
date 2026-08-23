import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list and edge set for O(1) lookup
    adj = defaultdict(set)
    edges = set()
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        adj[u].add(v)
        adj[v].add(u)
        edges.add((min(u,v), max(u,v)))
    
    # Convert adjacency list to sorted lists for consistent iteration
    adj_list = {k: sorted(list(v)) for k, v in adj.items()}
    
    # Iterate through all possible triplets (i, j, k) with i < j < k
    for i in range(1, n+1):
        if i not in adj_list:
            continue
        for idx_j in range(len(adj_list[i])):
            j = adj_list[i][idx_j]
            if j <= i:
                continue
            for idx_k in range(idx_j+1, len(adj_list[i])):
                k = adj_list[i][idx_k]
                if k <= j:
                    continue
                # Check if j and k are connected
                if (j, k) in edges:
                    print(i, j, k)
                    return

if __name__ == "__main__":
    main()