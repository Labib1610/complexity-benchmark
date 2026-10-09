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
    
    # Topological sort with level tracking
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
    
    # Check if all nodes are processed (no cycles)
    if len(topo_order) != n:
        print("NO")
        return
    
    # Check if levels exceed deadline
    max_level = max(level[1:])
    if max_level > T:
        print("NO")
        return
    
    # Assign jobs to hours respecting capacity
    hour = [0] * (n + 1)
    count_per_hour = [0] * (T + 1)
    
    # Group jobs by their level
    jobs_by_level = defaultdict(list)
    for job in range(1, n + 1):
        jobs_by_level[level[job]].append(job)
    
    # Assign jobs level by level
    for t in range(1, T + 1):
        if t in jobs_by_level:
            jobs = jobs_by_level[t]
            for job in jobs:
                if count_per_hour[t] < M:
                    hour[job] = t
                    count_per_hour[t] += 1
                else:
                    # Try to shift to later hours within deadline
                    shifted = False
                    for later in range(t + 1, T + 1):
                        if count_per_hour[later] < M:
                            hour[job] = later
                            count_per_hour[later] += 1
                            shifted = True
                            break
                    if not shifted:
                        print("NO")
                        return
    
    # Verify all jobs are assigned
    for i in range(1, n + 1):
        if hour[i] == 0:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, hour[1:])))

if __name__ == "__main__":
    main()