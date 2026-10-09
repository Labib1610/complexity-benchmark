import sys
from collections import deque, defaultdict

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    T = []
    for _ in range(t):
        T.append(int(input_data[idx])); idx += 1
    
    pairs = []
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        pairs.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    T_set = set(T)
    T_list = list(T)
    
    # Build adjacency for all pairs
    adj_all = defaultdict(list)
    for i, (u, v, w) in enumerate(pairs):
        adj_all[u].append((v, i))
        adj_all[v].append((u, i))
    
    # For each pair, compute reachability in G \ {that pair}
    # reach[i] = set of nodes reachable from u_i (and v_i) in G \ pair_i
    reach = [None] * m
    for i, (u, v, w) in enumerate(pairs):
        visited = set()
        visited.add(u)
        visited.add(v)
        queue = deque([u, v])
        while queue:
            x = queue.popleft()
            for (y, j) in adj_all[x]:
                if j != i and y not in visited:
                    visited.add(y)
                    queue.append(y)
        reach[i] = visited
    
    # For each pair, compute which subsets of T it covers
    # cover[i] = bitmask of subsets A (non-empty proper subset of T) that pair i covers
    full_mask = (1 << t) - 1
    num_subsets = (1 << t) - 2  # exclude 0 and full_mask
    
    # Map subset mask to subset index (1..num_subsets)
    def subset_to_idx(mask):
        return mask - 1  # mask 1 -> idx 0, mask 2 -> idx 1, etc.
    
    cover = [0] * m
    for i in range(m):
        r = reach[i]
        T_in_r = 0
        for j, elem in enumerate(T_list):
            if elem in r:
                T_in_r |= (1 << j)
        # Pair covers subset A if (T_in_r & A) != 0 and (T_in_r & ~A & full_mask) != 0
        # i.e., T_in_r intersects both A and T\A
        # For all A from 1 to full_mask-1:
        for A in range(1, full_mask):
            if (T_in_r & A) and (T_in_r & (~A & full_mask)):
                cover[i] |= (1 << (A - 1))
    
    # Build flow network
    # Nodes: 0 = source, 1..m = pair nodes, m+1..m+num_subsets = subset nodes, m+num_subsets+1 = sink
    source = 0
    sink = m + num_subsets + 1
    num_nodes = sink + 1
    
    INF = float('inf')
    
    # Edges: source -> pair (capacity w), pair -> subset (if covers, INF), subset -> sink (INF)
    graph = [[] for _ in range(num_nodes)]
    
    def add_edge(u, v, cap):
        graph[u].append([v, cap, len(graph[v])])
        graph[v].append([u, 0, len(graph[u]) - 1])
    
    for i, (u, v, w) in enumerate(pairs):
        add_edge(source, 1 + i, w)
        c = cover[i]
        while c:
            low = c & (-c)
            A_idx = low.bit_length() - 1  # subset index
            add_edge(1 + i, 1 + m + A_idx, INF)
            c ^= low
    
    for j in range(num_subsets):
        add_edge(1 + m + j, sink, INF)
    
    # Dinic's algorithm
    def bfs():
        level = [-1] * num_nodes
        level[source] = 0
        queue = deque([source])
        while queue:
            x = queue.popleft()
            for edge in graph[x]:
                v, cap, _ = edge
                if cap > 0 and level[v] < 0:
                    level[v] = level[x] + 1
                    queue.append(v)
        return level if level[sink] >= 0 else None
    
    def dfs(x, level, iter_arr, f):
        if x == sink:
            return f
        while iter_arr[x] < len(graph[x]):
            edge = graph[x][iter_arr[x]]
            v, cap, rev = edge
            if cap > 0 and level[v] == level[x] + 1:
                d = dfs(v, level, iter_arr, min(f, cap))
                if d > 0:
                    edge[1] -= d
                    graph[v][rev][1] += d
                    return d
            iter_arr[x] += 1
        return 0
    
    max_flow = 0
    while True:
        level = bfs()
        if level is None:
            break
        iter_arr = [0] * num_nodes
        while True:
            f = dfs(source, level, iter_arr, INF)
            if f == 0:
                break
            max_flow += f
    
    print(max_flow)

solve()