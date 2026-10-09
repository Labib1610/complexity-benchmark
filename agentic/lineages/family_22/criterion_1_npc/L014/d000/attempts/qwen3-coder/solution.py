from collections import defaultdict, deque

def main():
    n, M, T, m = map(int, input().split())
    
    # Build graph
    graph = defaultdict(list)
    indegree = [0] * (n + 1)
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    
    # Topological sort with level assignment
    queue = deque()
    level = [0] * (n + 1)
    
    # Find all nodes with indegree 0
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            level[i] = 1
    
    # Process nodes in topological order
    while queue:
        node = queue.popleft()
        current_level = level[node]
        
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            level[neighbor] = max(level[neighbor], current_level + 1)
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if all nodes were processed (no cycles)
    for i in range(1, n + 1):
        if indegree[i] != 0:
            print("NO")
            return
    
    # Check if we can fit within T minutes
    max_level = max(level[1:])
    if max_level > T:
        print("NO")
        return
    
    # Count jobs per level
    count_per_level = [0] * (T + 1)
    for i in range(1, n + 1):
        count_per_level[level[i]] += 1
    
    # Check if any level exceeds M servers
    valid = True
    for i in range(1, T + 1):
        if count_per_level[i] > M:
            valid = False
            break
    
    if not valid:
        print("NO")
        return
    
    # Output result
    print("YES")
    print(*level[1:])

if __name__ == "__main__":
    main()