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
    adj_L = defaultdict(list)  # adjacency list for L (Alpha)
    adj_R = defaultdict(list)   # adjacency list for R (Beta)
    
    for i in range(m):
        u = int(data[idx]) - 1  # 0-indexed
        idx += 1
        v = int(data[idx]) - 1  # 0-indexed
        idx += 1
        edges.append((u, v))
        adj_L[u].append((v, i))
        adj_R[v].append((u, i))
    
    # Determine maximum degree Δ
    delta = 0
    for u in adj_L:
        delta = max(delta, len(adj_L[u]))
    for v in adj_R:
        delta = max(delta, len(adj_R[v]))
    
    # Edge coloring: we'll use a greedy approach with available colors per node
    result = [0] * m
    # For each node, maintain a min-heap of available colors
    color_heap_L = {}
    color_heap_R = {}
    # For tracking which colors are used by neighbors
    used_colors_L = defaultdict(set)
    used_colors_R = defaultdict(set)
    
    # Initialize heaps for each node
    for u in adj_L:
        color_heap_L[u] = list(range(1, delta + 1))
        heapq.heapify(color_heap_L[u])
    for v in adj_R:
        color_heap_R[v] = list(range(1, delta + 1))
        heapq.heapify(color_heap_R[v])
    
    # Process edges in arbitrary order (we can do better but this works)
    for u in adj_L:
        for v, i in adj_L[u]:
            # Get a color not used by u or v
            c = None
            temp_colors = []
            while color_heap_L[u]:
                col = heapq.heappop(color_heap_L[u])
                if col not in used_colors_L[u] and col not in used_colors_R[v]:
                    c = col
                    break
                temp_colors.append(col)
            # Push back the popped colors
            for col in temp_colors:
                heapq.heappush(color_heap_L[u], col)
            
            if c is None:
                # Try to find a color from v's heap
                temp_colors_v = []
                while color_heap_R[v]:
                    col = heapq.heappop(color_heap_R[v])
                    if col not in used_colors_L[u] and col not in used_colors_R[v]:
                        c = col
                        break
                    temp_colors_v.append(col)
                for col in temp_colors_v:
                    heapq.heappush(color_heap_R[v], col)
            
            if c is None:
                # This shouldn't happen due to Δ bound
                raise Exception("Could not assign color")
                
            result[i] = c
            used_colors_L[u].add(c)
            used_colors_R[v].add(c)
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()