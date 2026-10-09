import sys
from collections import defaultdict
import heapq

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read
    data = input().split()
    
    nL = int(data[0])
    nR = int(data[1])
    m = int(data[2])
    
    tests = []
    deg_L = [0] * (nL + 1)
    deg_R = [0] * (nR + 1)
    
    for i in range(m):
        u = int(data[3 + 2*i])
        v = int(data[3 + 2*i + 1])
        tests.append((u, v))
        deg_L[u] += 1
        deg_R[v] += 1
    
    delta = max(max(deg_L), max(deg_R))
    
    # For each device, maintain a min-heap of available colors
    heap_L = [[] for _ in range(nL + 1)]
    heap_R = [[] for _ in range(nR + 1)]
    res = []
    
    # We'll process edges in a specific order to ensure we can always color them
    # But since we know that the chromatic index equals the maximum degree,
    # we can use a greedy approach with heaps tracking used colors.
    
    # To implement the edge coloring efficiently, we can simulate the proof of König's theorem:
    # The idea is to maintain for each vertex the set of colors used on its edges,
    # and assign the smallest available color.
    
    # However, a simpler way is to just greedily assign the smallest color not used 
    # by either endpoint, which works because the graph is bipartite.
    
    # Let's track for each vertex the set of colors currently used.
    # But to make it efficient, we can use a global pool of available colors per node,
    # or just assign greedily using a heap to find the next available color quickly.
    
    # Actually, let's think differently:
    # We can build a graph and then perform a BFS-based edge coloring.
    # But there's an even easier way: since the graph is bipartite, 
    # we can sort the edges and assign colors greedily.
    
    # Here's a simple greedy method:
    # For each edge, pick the smallest color not yet used by either endpoint.
    # To do this efficiently, for each vertex we keep track of the colors used.
    # And also maintain a min-heap of available colors for assignment.
    
    # Initialize available color heaps for each vertex as [1,2,...,delta]
    # But that's inefficient. Instead, we track used colors and find the mex (minimum excludant).
    
    # Better approach:
    # For each vertex, maintain a boolean array or a set of used colors.
    # Since delta is bounded reasonably, we can do this.
    # Or even better, use a heap to track the minimum available color.
    
    # Let's do this properly:
    # For each vertex, maintain a min-heap of *used* colors.
    # Then, to get the next available color, we look for the smallest positive integer not in the heap.
    # This is called finding the "mex" (minimum excludant).
    
    # To find mex efficiently:
    # Keep a min-heap of used colors, and track the mex incrementally.
    # When assigning a new color, take the current mex.
    # When releasing a color (if needed), update accordingly.
    
    # But in our case, once assigned, colors stay assigned.
    # So we just need to assign each edge a color not used by its endpoints.
    
    # Efficient way:
    # For each vertex, keep a min-heap of *used* colors.
    # Also keep a variable for the current mex.
    # But again, since we don't release colors, we can simplify.
    
    # Let's proceed with a greedy assignment:
    # For each edge, assign the smallest color >= 1 that is not used by u or v.
    
    # To do this efficiently:
    used_L = [set() for _ in range(nL + 1)]
    used_R = [set() for _ in range(nR + 1)]
    
    # We can also maintain for each vertex a min-heap of *available* colors.
    # Initially, all vertices have access to colors 1 through delta.
    # As we assign colors, we remove them from availability.
    
    avail_L = [list(range(delta, 0, -1)) for _ in range(nL + 1)]  # reverse order for heap
    avail_R = [list(range(delta, 0, -1)) for _ in range(nR + 1)]
    
    def get_available_color(u, v):
        # Find the smallest color that is available for both u and v
        # We can intersect their available colors and pick the minimum
        # But that's slow. Instead, we can pop from heaps until we find a common one.
        # Even simpler: just pick the first available from u, check if available for v.
        # If not, try next. Since lists are sorted descending, we pop from end.
        # This is still not optimal but should work.
        
        # Let's instead do: for each vertex, keep a min-heap of used colors.
        # Then, to assign a new color, find the smallest positive integer not in either heap.
        # That's the mex.
        # To compute mex efficiently:
        # Use a min-heap H_u and H_v.
        # Merge them conceptually and find the first missing positive integer.
        # This is doable by merging and scanning.
        # But let's avoid that complexity.
        
        # Simpler: just use sets and scan.
        cu = used_L[u]
        cv = used_R[v]
        c = 1
        while c in cu or c in cv:
            c += 1
        return c
        
    
    # Actually, let's re-think.
    # The most straightforward way:
    # For each vertex, maintain a set of used colors.
    # For each edge, find the minimum color not in either set.
    # Assign it, and add to both sets.
    
    result = []
    for u, v in tests:
        cu = used_L[u]
        cv = used_R[v]
        c = 1
        while c in cu or c in cv:
            c += 1
        result.append(c)
        cu.add(c)
        cv.add(c)
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()