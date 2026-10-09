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
    
    # Build graph
    graph = defaultdict(list)
    indegree = [0] * (n + 1)
    
    for _ in range(m):
        a = int(data[idx])
        b = int(data[idx+1])
        idx += 2
        graph[a].append(b)
        indegree[b] += 1
    
    # Topological sort with cycle detection
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
    
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(order) != n:
        print("NO")
        return
    
    # Assign cycles
    cycle = [0] * (n + 1)
    processor_count = [0] * (T + 1)
    
    # For each node in topological order, assign the earliest possible cycle
    for node in order:
        # Find the earliest cycle where all dependencies are satisfied and capacity allows
        earliest = 1
        for dep in graph:
            if node in graph[dep]:
                earliest = max(earliest, cycle[dep] + 1)
        
        # Try to place in the earliest available cycle
        placed = False
        for c in range(earliest, T + 1):
            if processor_count[c] < M:
                cycle[node] = c
                processor_count[c] += 1
                placed = True
                break
        
        if not placed:
            print("NO")
            return
    
    # Check if all processors are assigned
    for i in range(1, n + 1):
        if cycle[i] == 0:
            print("NO")
            return
    
    print("YES")
    print(' '.join(str(cycle[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()