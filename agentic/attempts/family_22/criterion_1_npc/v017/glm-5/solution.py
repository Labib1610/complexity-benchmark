import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    M = int(input_data[1])
    T = int(input_data[2])
    m = int(input_data[3])
    
    adj = [[] for _ in range(n)]
    in_degree = [0] * n
    
    idx = 4
    for _ in range(m):
        a = int(input_data[idx]) - 1
        b = int(input_data[idx + 1]) - 1
        adj[a].append(b)
        in_degree[b] += 1
        idx += 2
        
    queue = []
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
            
    cycle_assignment = [0] * n
    current_cycle = 1
    operations_done = 0
    
    while queue:
        if current_cycle > T:
            print("NO")
            return
            
        # We can schedule at most M operations in the current cycle
        # To minimize the maximum cycle, we greedily assign as many as possible
        # to the current cycle.
        next_queue = []
        count = 0
        
        for u in queue:
            if count < M:
                cycle_assignment[u] = current_cycle
                count += 1
                for v in adj[u]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        next_queue.append(v)
                operations_done += 1
            else:
                # Exceeds capacity for this cycle, defer to the next cycle
                next_queue.append(u)
                
        queue = next_queue
        current_cycle += 1
        
    if operations_done != n:
        print("NO")
        return
        
    # Check if any operation was assigned a cycle > T
    for c in cycle_assignment:
        if c > T:
            print("NO")
            return
            
    print("YES")
    print(" ".join(map(str, cycle_assignment)))

if __name__ == '__main__':
    solve()