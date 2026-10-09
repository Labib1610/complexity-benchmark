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
    
    # Topological sort with level tracking
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
    
    levels = [0] * (n + 1)  # level corresponds to stage
    nodes_in_level = defaultdict(list)
    current_level = 1
    
    while queue:
        next_queue = deque()
        processed_count = 0
        
        # Process all nodes with indegree 0 in current level
        while queue:
            node = queue.popleft()
            levels[node] = current_level
            nodes_in_level[current_level].append(node)
            processed_count += 1
            
            # Check if we exceed stage capacity
            if processed_count > M:
                print("NO")
                return
            
            # Update neighbors
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    next_queue.append(neighbor)
        
        # Move to next level
        queue = next_queue
        current_level += 1
        
        # Check if we exceed number of stages
        if current_level > T + 1:
            print("NO")
            return
    
    # Check if all nodes were processed (no cycles)
    for i in range(1, n + 1):
        if levels[i] == 0:
            print("NO")
            return
    
    # Output result
    print("YES")
    result = []
    for i in range(1, n + 1):
        result.append(str(levels[i]))
    print(" ".join(result))

if __name__ == "__main__":
    main()