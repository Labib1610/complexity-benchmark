import sys
from collections import defaultdict, deque

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    k = int(input_data[idx]); idx += 1
    
    commodities = []
    for i in range(k):
        s = int(input_data[idx]); idx += 1
        t = int(input_data[idx]); idx += 1
        d = int(input_data[idx]); idx += 1
        commodities.append((s, t, d))
    
    edges = []
    adj = defaultdict(list)
    for j in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        cap = int(input_data[idx]); idx += 1
        edges.append((u, v, cap))
        adj[u].append((v, j))
    
    # Find all simple paths for each commodity
    def find_paths(s, t, max_paths=100):
        paths = []
        stack = [(s, [s], [], set([s]))]
        while stack and len(paths) < max_paths:
            node, path_nodes, path_edges, visited = stack.pop()
            if node == t:
                if path_edges:
                    paths.append(path_edges)
                continue
            for (v, j) in adj[node]:
                if v not in visited:
                    new_visited = visited | {v}
                    stack.append((v, path_nodes + [v], path_edges + [j], new_visited))
        return paths
    
    # Get paths for each commodity
    all_paths = []
    for (s, t, d) in commodities:
        paths = find_paths(s, t)
        all_paths.append(paths)
    
    # Greedy: try to assign flow to paths
    remaining_cap = [edges[j][2] for j in range(m)]
    flow = [[0]*m for _ in range(k)]
    
    for i in range(k):
        s, t, d = commodities[i]
        remaining = d
        paths = all_paths[i]
        # Sort paths by length (shorter first)
        paths.sort(key=len)
        for path in paths:
            if remaining == 0:
                break
            # Max flow we can send on this path
            max_on_path = min(remaining_cap[j] for j in path)
            if max_on_path > 0:
                send = min(max_on_path, remaining)
                for j in path:
                    flow[i][j] += send
                    remaining_cap[j] -= send
                remaining -= send
        if remaining > 0:
            print("NO")
            return
    
    print("YES")
    for i in range(k):
        print(' '.join(map(str, flow[i])))

solve()