import sys
from collections import defaultdict
import heapq

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n_A = int(data[0])
    n_B = int(data[1])
    m = int(data[2])
    
    operations = []
    deg_A = [0] * (n_A + 1)
    deg_B = [0] * (n_B + 1)
    
    idx = 3
    for i in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        operations.append((u, v))
        deg_A[u] += 1
        deg_B[v] += 1
        idx += 2
    
    T = max(max(deg_A), max(deg_B)) if m > 0 else 0
    
    # For each machine, maintain a min-heap of available cycles
    heap_A = [[] for _ in range(n_A + 1)]
    heap_B = [[] for _ in range(n_B + 1)]
    
    # Initialize heaps with cycles 1 to T
    for u in range(1, n_A + 1):
        for c in range(1, T + 1):
            heapq.heappush(heap_A[u], c)
    
    for v in range(1, n_B + 1):
        for c in range(1, T + 1):
            heapq.heappush(heap_B[v], c)
    
    result = []
    
    for u, v in operations:
        # Get the smallest available cycle for both u and v
        # We need to find a cycle that's available for both
        # Peek at the tops of both heaps to find the first common cycle
        # This requires merging or checking, so we do it step by step
        
        # To make it efficient, we can just pop from both and push back unused ones
        # But a better way is to always assign the max of the current minima to avoid conflict
        # Actually, since we know a solution exists, we can use a greedy approach:
        # Always assign the earliest cycle that is available for both machines
        
        # Let's use a simpler method:
        # Keep track of next available cycle for each machine
        # But since we have to ensure both ends are free, we'll simulate assignment
        
        # A correct and efficient way:
        # Use a priority queue approach where we assign cycles greedily ensuring no conflicts
        
        # However, given the constraints and that a solution always exists,
        # we can model this as edge coloring in a bipartite graph, which is always possible with degree Δ
        
        # Efficient simulation:
        # For each operation, pick the earliest cycle not used by either endpoint yet in current assignment
        
        # Let's implement a direct simulation:
        
        # For each node, keep a set of used cycles
        used_A = [set() for _ in range(n_A + 1)]
        used_B = [set() for _ in range(n_B + 1)]
        
        result = []
        for u, v in operations:
            c = 1
            while c in used_A[u] or c in used_B[v]:
                c += 1
            used_A[u].add(c)
            used_B[v].add(c)
            result.append(c)
        break # Only run once
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()