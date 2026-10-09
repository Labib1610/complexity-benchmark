from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    M = int(data[idx+1])
    T = int(data[idx+2])
    m = int(data[idx+3])
    idx += 4
    
    # Build graph and in-degree count
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    for _ in range(m):
        a = int(data[idx])
        b = int(data[idx+1])
        graph[a].append(b)
        in_degree[b] += 1
        idx += 2
    
    # Topological sort with Kahn's algorithm
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    topo_order = []
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If topo_order doesn't include all nodes, there's a cycle
    if len(topo_order) != n:
        print("NO")
        return
    
    # Assign time slots
    # time_slots[t] = number of operations scheduled at time t
    time_slots = [0] * (T + 1)  # 1-indexed
    assignment = [0] * (n + 1)   # assignment[i] = time slot for operation i
    
    # For each operation in topological order, assign the earliest possible time slot
    for op in topo_order:
        # Earliest time is max(1, max of predecessors' times + 1)
        earliest = 1
        for pred in graph:
            if op in graph[pred]:
                earliest = max(earliest, assignment[pred] + 1)
        
        # Find the first time slot from 'earliest' to T where we can fit this operation
        placed = False
        for t in range(earliest, T + 1):
            if time_slots[t] < M:
                assignment[op] = t
                time_slots[t] += 1
                placed = True
                break
        
        if not placed:
            print("NO")
            return
    
    # If we reached here, a valid schedule exists
    print("YES")
    print(' '.join(str(assignment[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()