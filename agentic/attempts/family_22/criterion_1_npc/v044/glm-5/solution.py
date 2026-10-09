import sys

# Set recursion limit for deep DFS (though n is likely small enough)
sys.setrecursionlimit(100000)

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    iterator = iter(data)
    n = int(next(iterator))
    M = int(next(iterator))
    T = int(next(iterator))
    m = int(next(iterator))
    
    adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    
    for _ in range(m):
        a = int(next(iterator))
        b = int(next(iterator))
        adj[a].append(b)
        in_degree[b] += 1
        
    # Initialize time for each operation
    # We will compute this in topological order
    t = [1] * (n + 1)
    
    # Queue for topological sort (0 in-degree nodes)
    q = []
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)
            
    processed_count = 0
    head = 0
    
    while head < len(q):
        u = q[head]
        head += 1
        processed_count += 1
        
        for v in adj[u]:
            # v must happen strictly after u.
            # Since all operations take time 1, strict inequality t[v] > t[u] translates to t[v] >= t[u] + 1
            if t[v] < t[u] + 1:
                t[v] = t[u] + 1
            
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
                
    # If not all nodes processed, there is a cycle
    if processed_count != n:
        print("NO")
        return
    
    # Check if any operation is scheduled beyond the deadline T
    # Since deadlines are strict, t[i] must be <= T
    feasible = True
    for i in range(1, n + 1):
        if t[i] > T:
            feasible = False
            break
            
    if not feasible:
        print("NO")
        return
    
    # Get the distribution of operations across time intervals
    # slots[k] will store the number of operations scheduled at time k
    slots = [0] * (T + 1)
    for i in range(1, n + 1):
        slots[t[i]] += 1
        
    # Check if the number of operations in any time slot exceeds the number of bays M
    # We allow operations in the same time slot to run in parallel up to M
    for k in range(1, T + 1):
        if slots[k] > M:
            print("NO")
            return
            
    # All checks passed - produce output
    print("YES")
    output_tokens = [str(t[i]) for i in range(1, n + 1)]
    print(" ".join(output_tokens))

if __name__ == "__main__":
    solve()