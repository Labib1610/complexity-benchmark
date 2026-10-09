from collections import defaultdict, deque

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
    
    # Build graph for topological sort
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        graph[u].append(v)
        in_degree[v] += 1
    
    # Topological sort
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
    
    # Check if all nodes are included (no cycle)
    if len(topo_order) != n:
        print("NO")
        return
    
    # Assign days
    day_assignment = [0] * (n + 1)
    day_count = [0] * (T + 1)
    
    # Try to assign each container to the earliest possible day
    for container in topo_order:
        assigned = False
        for d in range(1, T + 1):
            # Check if we can place this container on day d
            # We need to ensure that all predecessors are assigned to days < d
            valid = True
            for pred in graph:
                if container in graph[pred]:
                    if day_assignment[pred] >= d:
                        valid = False
                        break
            if valid and day_count[d] < M:
                day_assignment[container] = d
                day_count[d] += 1
                assigned = True
                break
        if not assigned:
            print("NO")
            return
    
    # Check the additional constraint: for any subset of days S, containers(S) <= |S| * M
    # This is equivalent to checking that for every prefix of days, the number of containers
    # assigned to days 1..t is <= t*M
    prefix_count = [0] * (T + 1)
    for i in range(1, n + 1):
        prefix_count[day_assignment[i]] += 1
    
    cum_sum = 0
    for t in range(1, T + 1):
        cum_sum += prefix_count[t]
        if cum_sum > t * M:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, day_assignment[1:])))

if __name__ == "__main__":
    main()