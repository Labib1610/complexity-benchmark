import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    demands = []
    for i in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        demands.append((s, t, d))

    edges = []
    adj = [[] for _ in range(n)]
    for j in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))
        adj[u].append(j)

    # Flatten demands into individual path requests
    requests = []
    for c_id, (s, t, d) in enumerate(demands):
        for _ in range(d):
            requests.append((s, t, c_id))

    # Remaining capacities
    rem_cap = [cap for _, _, cap in edges]

    # Pre-check individual reachability
    def can_reach(s, t):
        visited = [False] * n
        queue = deque([s])
        visited[s] = True
        while queue:
            curr = queue.popleft()
            if curr == t:
                return True
            for edge_idx in adj[curr]:
                if rem_cap[edge_idx] > 0:
                    v = edges[edge_idx][1]
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)
        return False

    # Check if any commodity is initially disconnected
    for s, t, d in demands:
        if d > 0 and not can_reach(s, t):
            print("NO")
            return

    # Sort requests: longest shortest-path first
    def get_dist(s, t):
        dist = [-1] * n
        dist[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            if u == t:
                return dist[t]
            for e in adj[u]:
                if rem_cap[e] > 0:
                    v = edges[e][1]
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
        return float('inf')

    requests.sort(key=lambda r: get_dist(r[0], r[1]), reverse=True)

    # Flow matrix: flow[c_id][edge_idx]
    flow = [[0] * m for _ in range(k)]

    # Backtracking to find paths
    def find_all_paths(s, t):
        paths = []
        # BFS with parent pointers to find shortest path
        parent = [-1] * n
        parent_edge = [-1] * n
        visited = [False] * n
        q = deque([s])
        visited[s] = True
        
        while q:
            u = q.popleft()
            if u == t:
                break
            for e_idx in adj[u]:
                if rem_cap[e_idx] > 0:
                    v = edges[e_idx][1]
                    if not visited[v]:
                        visited[v] = True
                        parent[v] = u
                        parent_edge[v] = e_idx
                        q.append(v)

        if visited[t]:
            curr = t
            p = []
            while curr != s:
                e_idx = parent_edge[curr]
                p.append(e_idx)
                curr = parent[curr]
            p.reverse()
            paths.append(p)

        # Also find other alternative paths using limited DFS if needed
        def dfs_paths(u, target, current_path, visited_nodes, limit=5):
            if len(paths) >= limit:
                return
            if u == target:
                if current_path not in paths:
                    paths.append(list(current_path))
                return
            for e_idx in adj[u]:
                if rem_cap[e_idx] > 0:
                    v = edges[e_idx][1]
                    if not visited_nodes[v]:
                        visited_nodes[v] = True
                        current_path.append(e_idx)
                        dfs_paths(v, target, current_path, visited_nodes, limit)
                        current_path.pop()
                        visited_nodes[v] = False

        vis = [False] * n
        vis[s] = True
        dfs_paths(s, t, [], vis, limit=6)
        return paths

    def dfs(idx):
        if idx == len(requests):
            return True

        s, t, c_id = requests[idx]
        candidate_paths = find_all_paths(s, t)
        if not candidate_paths:
            return False

        for path in candidate_paths:
            # Check feasibility
            feasible = True
            for e_idx in path:
                if rem_cap[e_idx] <= 0:
                    feasible = False
                    break
            if not feasible:
                continue

            # Apply
            for e_idx in path:
                rem_cap[e_idx] -= 1
                flow[c_id][e_idx] += 1

            if dfs(idx + 1):
                return True

            # Revert
            for e_idx in path:
                rem_cap[e_idx] += 1
                flow[c_id][e_idx] -= 1

        return False

    if dfs(0):
        print("YES")
        for i in range(k):
            print(*(flow[i]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()