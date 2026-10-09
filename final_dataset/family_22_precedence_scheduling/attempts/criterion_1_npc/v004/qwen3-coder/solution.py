from collections import deque, defaultdict
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1
    T = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    # Build graph
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    for _ in range(m):
        a = int(data[idx])
        idx += 1
        b = int(data[idx])
        idx += 1
        graph[a].append(b)
        in_degree[b] += 1
    
    # Topological sort with priority to minimize slot usage
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    # slots[i] = number of tasks scheduled in slot i
    slots = [0] * (T + 1)
    task_slot = [0] * (n + 1)
    
    # For each task, we need to know the earliest slot it can start
    earliest_start = [1] * (n + 1)
    
    # Process tasks in topological order
    topo_order = []
    temp_queue = deque(queue)
    while temp_queue:
        u = temp_queue.popleft()
        topo_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                temp_queue.append(v)
    
    if len(topo_order) != n:
        print("NO")
        return
    
    # Now assign slots
    for u in topo_order:
        # Find the earliest slot where we can place task u
        slot = earliest_start[u]
        while slot <= T and slots[slot] >= M:
            slot += 1
        if slot > T:
            print("NO")
            return
        slots[slot] += 1
        task_slot[u] = slot
        # Update earliest start time for neighbors
        for v in graph[u]:
            earliest_start[v] = max(earliest_start[v], slot + 1)
    
    print("YES")
    print(' '.join(map(str, task_slot[1:])))

if __name__ == "__main__":
    main()