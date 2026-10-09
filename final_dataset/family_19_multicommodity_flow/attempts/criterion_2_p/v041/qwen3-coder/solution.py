from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    one = int(data[idx])
    idx += 1
    
    s = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    d = int(data[idx])
    idx += 1
    
    edges = []
    graph = defaultdict(list)
    capacity = []
    
    for i in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        cap = int(data[idx])
        idx += 1
        edges.append((u, v, cap))
        graph[u].append((v, len(capacity)))
        capacity.append(cap)
        graph[v].append((u, len(capacity)))
        capacity.append(0)  # reverse edge with 0 capacity initially

    # Add super source and super sink
    super_s = 0
    super_t = n + 1

    # Connect super source to s with capacity d
    graph[super_s].append((s, len(capacity)))
    capacity.append(d)
    graph[s].append((super_s, len(capacity)))
    capacity.append(0)

    # Connect t to super sink with capacity d
    graph[t].append((super_t, len(capacity)))
    capacity.append(d)
    graph[super_t].append((t, len(capacity)))
    capacity.append(0)

    def bfs():
        parent = [-1] * (n + 2)
        visited = [False] * (n + 2)
        queue = deque([super_s])
        visited[super_s] = True

        while queue:
            u = queue.popleft()
            for v, i in graph[u]:
                if not visited[v] and capacity[i] > 0:
                    visited[v] = True
                    parent[v] = (u, i)
                    if v == super_t:
                        return parent
                    queue.append(v)
        return None

    max_flow = 0
    flow = [0] * len(capacity)

    while True:
        parent = bfs()
        if not parent:
            break

        # Find minimum capacity along the path
        path_flow = float('inf')
        s_node = super_t
        while s_node != super_s:
            u, i = parent[s_node]
            path_flow = min(path_flow, capacity[i])
            s_node = u

        # Update capacities and flows
        v_node = super_t
        while v_node != super_s:
            u, i = parent[v_node]
            capacity[i] -= path_flow
            capacity[i ^ 1] += path_flow
            flow[i] += path_flow
            flow[i ^ 1] -= path_flow
            v_node = u

        max_flow += path_flow

    if max_flow < d:
        print("NO")
        return

    print("YES")
    result = []
    for i in range(0, len(flow), 2):
        result.append(str(flow[i]))
    print(' '.join(result[:m]))

solve()