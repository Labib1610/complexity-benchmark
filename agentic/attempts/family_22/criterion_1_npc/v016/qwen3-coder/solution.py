from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    M = int(data[1])
    T = int(data[2])
    m = int(data[3])
    
    edges = []
    indegree = [0] * (n + 1)
    adj = defaultdict(list)
    
    idx = 4
    for _ in range(m):
        a = int(data[idx])
        b = int(data[idx + 1])
        idx += 2
        edges.append((a, b))
        adj[a].append(b)
        indegree[b] += 1
    
    # Topological sort with priority to minimize cycle assignment
    from heapq import heappush, heappop
    
    # We'll use a min-heap to always process the earliest available operations first
    heap = []
    dist = [0] * (n + 1)  # dist[i] will store the cycle assigned to operation i
    
    # Find all nodes with indegree 0
    for i in range(1, n + 1):
        if indegree[i] == 0:
            heappush(heap, (1, i))  # (cycle, operation)
    
    # For each cycle from 1 to T, we can schedule up to M operations
    cycle_op_count = [0] * (T + 1)
    scheduled = [0] * (n + 1)
    
    while heap and any(c < T or (c == T and cycle_op_count[c] < M) for c in range(1, T+1)):
        # Collect all operations that can be scheduled in current cycle
        temp_heap = []
        scheduled_in_cycle = 0
        
        # Try to schedule as many operations as possible in each cycle
        for t in range(1, T+1):
            if not heap:
                break
            temp_ops = []
            count_this_cycle = 0
            
            # Get all operations that can start at time t
            while heap and count_this_cycle < M:
                cycle, op = heappop(heap)
                if cycle > t:
                    temp_ops.append((cycle, op))
                    break
                else:
                    # Assign this operation to cycle t
                    dist[op] = t
                    scheduled[op] = t
                    count_this_cycle += 1
                    
                    # Add its neighbors
                    for neighbor in adj[op]:
                        indegree[neighbor] -= 1
                        if indegree[neighbor] == 0:
                            heappush(heap, (t + 1, neighbor))
            
            # Push back unprocessed operations
            for item in temp_ops:
                heappush(heap, item)
                
            # If we've reached the limit for this cycle, move on
            if count_this_cycle == M:
                continue
                
        if not any(scheduled[op] == 0 for op in range(1, n+1)):
            break
    
    # Check if all operations were scheduled
    if any(scheduled[i] == 0 for i in range(1, n+1)):
        print("NO")
        return
    
    # Validate the solution
    for a, b in edges:
        if dist[a] >= dist[b]:
            print("NO")
            return
            
    # Check that no more than M operations per cycle
    cycle_count = [0] * (T + 1)
    for i in range(1, n+1):
        cycle_count[dist[i]] += 1
    if any(count > M for count in cycle_count):
        print("NO")
        return
        
    print("YES")
    print(' '.join(str(dist[i]) for i in range(1, n+1)))

if __name__ == "__main__":
    main()