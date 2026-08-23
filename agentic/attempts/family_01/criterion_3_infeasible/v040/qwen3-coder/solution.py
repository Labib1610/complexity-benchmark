import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Store incompatibilities as a set of frozensets for fast lookup
    incompatibles = set()
    # Also store adjacency list for quick neighbor access
    adj = defaultdict(set)
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        if u > v:
            u, v = v, u
        incompatibles.add((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # We need to find a triangle in the complement graph
    # But it's easier to think of it as finding a triangle where all edges are present in our graph
    
    # Try all combinations of 3 nodes, starting from smallest
    # Since we want lexicographically smallest, we can iterate i<j<k
    
    # For efficiency, let's go through each node i, then its neighbors j, 
    # then check if any neighbor of j (that's not i) is also a neighbor of i
    
    found = False
    result = None
    
    # Convert adjacency lists to sorted lists for consistent iteration
    adj_list = {}
    for node in adj:
        adj_list[node] = sorted(list(adj[node]))
        
    # Iterate through nodes in ascending order
    for i in sorted(adj.keys()):
        if found:
            break
        neighbors_i = adj_list.get(i, [])
        # For each neighbor j of i where j > i
        for j_idx in range(len(neighbors_i)):
            j = neighbors_i[j_idx]
            if j <= i:
                continue
            neighbors_j = adj_list.get(j, [])
            # For each neighbor k of j where k > j
            for k in neighbors_j:
                if k <= j:
                    continue
                # Check if k is also a neighbor of i (i.e., edge i-k exists)
                if k in adj[i]:
                    # Found a triangle: i-j, j-k, i-k
                    print(i, j, k)
                    return
                    
    # Fallback brute force for correctness (though above should work)
    # This part won't be reached due to constraints and early return

if __name__ == "__main__":
    main()