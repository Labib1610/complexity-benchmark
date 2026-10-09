import sys
from collections import defaultdict
import heapq

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n_L = int(data[idx])
    idx += 1
    n_R = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    edges = []
    degree_L = [0] * (n_L + 1)
    degree_R = [0] * (n_R + 1)
    
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        edges.append((u, v))
        degree_L[u] += 1
        degree_R[v] += 1
    
    K = max(max(degree_L), max(degree_R))
    
    # For each switch, maintain a min-heap of available cycles
    cycles_L = [list(range(1, K+1)) for _ in range(n_L + 1)]
    cycles_R = [list(range(1, K+1)) for _ in range(n_R + 1)]
    import heapq
    for i in range(n_L + 1):
        heapq.heapify(cycles_L[i])
    for i in range(n_R + 1):
        heapq.heapify(cycles_R[i])
    
    result = []
    
    # To make sure we can always assign, we process edges in a specific order,
    # but actually, since the problem guarantees a solution exists with K cycles,
    # we can just assign greedily: for each edge (u,v), pick a cycle not used yet
    # by u and not used yet by v.
    
    # We'll use a greedy approach:
    # For each edge (u,v), find a cycle number that's still available for both u and v.
    # Since max degree is K, and we have K cycles, it's always possible.
    
    used_L = [set() for _ in range(n_L + 1)]
    used_R = [set() for _ in range(n_R + 1)]
    
    for u, v in edges:
        # Find a cycle from 1 to K not in used_L[u] and not in used_R[v]
        cyc = 1
        while cyc in used_L[u] or cyc in used_R[v]:
            cyc += 1
        result.append(str(cyc))
        used_L[u].add(cyc)
        used_R[v].add(cyc)
    
    print("YES")
    print(' '.join(result))

if __name__ == "__main__":
    main()