from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    k = int(data[idx])
    idx += 1
    d = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    # Build graph
    graph = defaultdict(list)
    indegree = [0] * (n + 1)
    
    for _ in range(m):
        a = int(data[idx])
        idx += 1
        b = int(data[idx])
        idx += 1
        graph[a].append(b)
        indegree[b] += 1
    
    # Topological sort with level assignment
    queue = deque()
    level = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            level[i] = 1
    
    topo_order = []
    
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            level[neighbor] = max(level[neighbor], level[node] + 1)
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if all nodes were processed (no cycles)
    if len(topo_order) != n:
        print("NO")
        return
    
    # Check if levels exceed deadline
    max_level = max(level[1:])
    if max_level > d:
        print("NO")
        return
    
    # For each level, check if we can assign tasks to stations without exceeding k
    # Group tasks by level
    level_tasks = defaultdict(list)
    for task in range(1, n + 1):
        level_tasks[level[task]].append(task)
    
    # Check each level
    for lvl in range(1, max_level + 1):
        if len(level_tasks[lvl]) > k:
            print("NO")
            return
    
    # If all checks pass, output the levels
    print("YES")
    result = []
    for i in range(1, n + 1):
        result.append(str(level[i]))
    print(' '.join(result))

if __name__ == "__main__":
    main()