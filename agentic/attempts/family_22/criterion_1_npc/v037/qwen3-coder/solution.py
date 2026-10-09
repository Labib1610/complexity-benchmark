from collections import deque, defaultdict
import sys

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
    
    # Build graph and in-degree
    graph = defaultdict(list)
    indegree = [0] * (n + 1)
    
    for _ in range(m):
        a = int(data[idx])
        idx += 1
        b = int(data[idx])
        idx += 1
        graph[a].append(b)
        indegree[b] += 1
    
    # Kahn's algorithm with level tracking
    queue = deque()
    # Find all nodes with in-degree 0
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)
    
    levels = [[]]  # levels[0] is dummy, levels start from 1
    current_level = 1
    count = 0
    result_slots = [0] * (n+1)
    
    while queue:
        next_queue = deque()
        current_tasks = []
        
        # Process all nodes at the current level
        while queue:
            node = queue.popleft()
            current_tasks.append(node)
            
        # Check if we exceed the number of stations
        if len(current_tasks) > k:
            print("NO")
            return
            
        # Assign slots: we can place up to k tasks per slot
        # If more than k tasks, we need multiple slots
        task_idx = 0
        slot_offset = 0
        while task_idx < len(current_tasks):
            num_tasks_in_slot = min(k, len(current_tasks) - task_idx)
            for i in range(num_tasks_in_slot):
                node = current_tasks[task_idx + i]
                result_slots[node] = current_level + slot_offset
                # Add neighbors to next level
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        next_queue.append(neighbor)
            task_idx += num_tasks_in_slot
            if task_idx < len(current_tasks):
                slot_offset += 1
        
        # Move to the next level
        current_level += slot_offset
        if current_level > d:
            print("NO")
            return
        queue = next_queue
    
    # Check if all nodes were processed
    if any(indegree[i] > 0 for i in range(1, n+1)):
        print("NO")
        return
        
    print("YES")
    print(' '.join(map(str, result_slots[1:])))

if __name__ == "__main__":
    main()