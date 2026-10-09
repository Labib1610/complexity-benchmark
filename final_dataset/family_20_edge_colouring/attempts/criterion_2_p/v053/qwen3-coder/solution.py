import sys
from collections import defaultdict
import heapq

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    nL = int(data[idx])
    idx += 1
    nR = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    operations = []
    for i in range(m):
        u = int(data[idx]) - 1  # Convert to 0-based indexing
        idx += 1
        v = int(data[idx]) - 1
        idx += 1
        operations.append((u, v))
    
    # Determine Delta: maximum number of operations involving any single feed
    warp_count = [0] * nL
    weft_count = [0] * nR
    for u, v in operations:
        warp_count[u] += 1
        weft_count[v] += 1
    Delta = max(max(warp_count), max(weft_count)) if m > 0 else 1
    
    # Create adjacency list for conflicts: for each operation, which operations conflict with it
    # Two operations conflict if they share a warp or weft feed
    adj = [[] for _ in range(m)]
    warp_op_list = [[] for _ in range(nL)]
    weft_op_list = [[] for _ in range(nR)]
    
    for i in range(m):
        u, v = operations[i]
        warp_op_list[u].append(i)
        weft_op_list[v].append(i)
    
    # For each operation, build its conflicting operations
    for op_list in warp_op_list:
        for i in op_list:
            for j in op_list:
                if i != j:
                    adj[i].append(j)
    for op_list in weft_op_list:
        for i in op_list:
            for j in op_list:
                if i != j:
                    adj[i].append(j)
                    
    # Now perform graph coloring using greedy algorithm with priority queue (DSatur heuristic)
    # But since Delta is bounded and we know a valid coloring exists with at most Delta colors,
    # we can use a simpler approach: assign lowest available color not used by neighbors
    
    # Result array
    result = [-1] * m
    # For each node, track which colors are forbidden
    forbidden = [set() for _ in range(m)]
    
    # Process nodes in some order; here we process in order but could optimize
    for i in range(m):
        # Find the smallest color >=1 not in forbidden[i]
        color = 1
        while color in forbidden[i]:
            color += 1
        result[i] = color
        # Propagate this color to neighbors
        for neighbor in adj[i]:
            forbidden[neighbor].add(color)
            
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()