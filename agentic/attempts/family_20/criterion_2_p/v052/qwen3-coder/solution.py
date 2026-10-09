import sys
from collections import defaultdict
import heapq

def main():
    import sys
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
    degree = [0] * (n_L + n_R + 1)
    
    for i in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        edges.append((u, v))
        degree[u] += 1
        degree[v + n_L] += 1  # Offset acceptor nodes
    
    delta = max(degree) if degree else 0
    
    # Build adjacency list for conflict graph: each node (donor or acceptor) has a list of connected bonds
    adj_bond = [[] for _ in range(n_L + n_R + 1)]
    for i in range(m):
        u, v = edges[i]
        adj_bond[u].append(i)
        adj_bond[v + n_L].append(i)
    
    # Color assignment: we'll use first-fit with a priority queue to minimize colors used
    result = [0] * m
    color_used = [0] * (delta + 1)  # Tracks which colors are used by neighbors
    
    for i in range(1, n_L + n_R + 1):
        if not adj_bond[i]:
            continue
        # Reset color tracking for current node's incident bonds
        for c in range(1, delta + 1):
            color_used[c] = False
        # Mark colors used by already colored neighbors
        for bond_idx in adj_bond[i]:
            if result[bond_idx] != 0:
                color_used[result[bond_idx]] = True
        # Assign the smallest available color to uncolored neighbors
        ptr = 1
        for bond_idx in adj_bond[i]:
            if result[bond_idx] == 0:
                while color_used[ptr]:
                    ptr += 1
                result[bond_idx] = ptr
                color_used[ptr] = True
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()