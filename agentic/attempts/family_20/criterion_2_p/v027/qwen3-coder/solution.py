import sys
from collections import defaultdict
import heapq

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    nL, nR, m = map(int, sys.stdin.readline().split())
    
    # If no transmissions, we can just output YES and nothing else
    if m == 0:
        print("YES")
        return
    
    # Store edges as a list
    edges = []
    # Degree count for each node
    deg_L = [0] * (nL + 1)
    deg_R = [0] * (nR + 1)
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        deg_L[u] += 1
        deg_R[v] += 1
    
    # Find K - the maximum degree
    K = 0
    for i in range(1, nL + 1):
        K = max(K, deg_L[i])
    for i in range(1, nR + 1):
        K = max(K, deg_R[i])
    
    # For each node, maintain a min-heap of available colors
    # We'll use a greedy approach: assign the smallest available color
    heap_L = [[] for _ in range(nL + 1)]
    heap_R = [[] for _ in range(nR + 1)]
    
    # Initialize heaps with all colors 1 to K for each node
    for i in range(1, nL + 1):
        for c in range(1, K + 1):
            heapq.heappush(heap_L[i], c)
            
    for i in range(1, nR + 1):
        for c in range(1, K + 1):
            heapq.heappush(heap_R[i], c)
    
    # To track which colors are currently used by each node
    used_L = [set() for _ in range(nL + 1)]
    used_R = [set() for _ in range(nR + 1)]
    
    result = []
    
    for u, v in edges:
        # Find the smallest color that is not used by both u and v
        # This is done by popping from heaps until we find such a color
        
        # We need to find a color that is available for both u and v
        # Let's take the top of both heaps and synchronize
        
        # A simpler way: since we're assigning greedily, we can keep track 
        # of used colors and pick the first available common one
        
        # But let's think differently: we can simulate this by keeping track
        # of used colors per node and picking a new one each time
        
        # Actually, there's a better way: 
        # Since we know that max degree is K, and a valid coloring exists,
        # we can use a greedy algorithm where for each edge (u,v) we pick
        # the smallest color not yet used by u and not yet used by v
        
        # Get the set of colors already used by u and v
        cu = used_L[u]
        cv = used_R[v]
        
        # Try colors from 1 to K
        color = 1
        while color in cu or color in cv:
            color += 1
            
        result.append(color)
        used_L[u].add(color)
        used_R[v].add(color)
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()