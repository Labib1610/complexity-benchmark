import sys
import time
import random
import heapq
from collections import defaultdict, deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    k = int(next(iterator))
    
    orders = []
    for i in range(k):
        s = int(next(iterator)) - 1
        t = int(next(iterator)) - 1
        d = int(next(iterator))
        orders.append((s, t, d))
        
    edges = []
    adj = [[] for _ in range(n)]
    for j in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        cap = int(next(iterator))
        edges.append((u, v, cap))
        adj[u].append((v, j))

    # Decompose orders into single-unit commodities
    # unit_id -> (order_id, s, t)
    units = []
    for i, (s, t, d) in enumerate(orders):
        for _ in range(d):
            units.append((i, s, t))
            
    num_units = len(units)
    
    # If no units to route, trivial YES
    if num_units == 0:
        print("YES")
        for _ in range(k):
            print(*(0 for _ in range(m)))
        return

    # Check trivial connectivity for each unit
    for i, s, t in units:
        # BFS to see if t reachable from s
        visited = [False] * n
        q = deque([s])
        visited[s] = True
        while q:
            curr = q.popleft()
            for nxt, _ in adj[curr]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
        if not visited[t]:
            print("NO")
            return

    # Backtracking / Rip-up and Reroute
    # For small num_units, we can use an exact DFS with heuristics,
    # or randomized rip-up and reroute.
    
    start_time = time.time()
    time_limit = 4.5  # seconds
    
    # Let's first try exact DFS (branch and bound) if num_units <= 40
    # DFS state: route units one by one
    def find_all_simple_paths(s, t, max_paths=100):
        # find some shortest / alternative paths
        paths = []
        q = deque([(s, [])])
        visited_in_path = [False] * n
        visited_in_path[s] = True
        
        # Simple BFS / DFS to find paths
        def dfs_paths(u, current_path):
            if len(paths) >= max_paths:
                return
            if u == t:
                paths.append(list(current_path))
                return
            for v, e_idx in adj[u]:
                if not visited_in_path[v]:
                    visited_in_path[v] = True
                    current_path.append(e_idx)
                    dfs_paths(v, current_path)
                    current_path.pop()
                    visited_in_path[v] = False

        dfs_paths(s, [])
        return paths

    # Pre-find paths for each distinct (s, t) pair
    pair_paths = {}
    for _, s, t in units:
        if (s, t) not in pair_paths:
            pair_paths[(s, t)] = find_all_simple_paths(s, t, max_paths=200)
            if not pair_paths[(s, t)]:
                print("NO")
                return

    # Check if total capacity on edges is enough
    # If sum of all demands > sum of all caps, maybe NO, but capacity is shared
    
    # Try exact DFS first
    edge_usage = [0] * m
    caps = [e[2] for e in edges]
    solution_paths = [None] * num_units
    
    # Sort units by fewest paths first (MRV heuristic)
    unit_order = sorted(range(num_units), key=lambda u_idx: len(pair_paths[(units[u_idx][1], units[u_idx][2])]))

    # Sort paths for each unit by length
    for p_list in pair_paths.values():
        p_list.sort(key=lambda p: len(p))

    found = [False]

    def solve_dfs(idx):
        if time.time() - start_time > 1.5:
            return False
        if idx == num_units:
            found[0] = True
            return True
        
        u_idx = unit_order[idx]
        s, t = units[u_idx][1], units[u_idx][2]
        paths = pair_paths[(s, t)]
        
        for path in paths:
            # Check if path fits
            possible = True
            for e in path:
                if edge_usage[e] + 1 > caps[e]:
                    possible = False
                    break
            if possible:
                for e in path:
                    edge_usage[e] += 1
                solution_paths[u_idx] = path
                if solve_dfs(idx + 1):
                    return True
                for e in path:
                    edge_usage[e] -= 1
                    
        return False

    if solve_dfs(0):
        # Format output
        ans = [[0] * m for _ in range(k)]
        for u_idx, path in enumerate(solution_paths):
            ord_id = units[u_idx][0]
            for e in path:
                ans[ord_id][e] += 1
        print("YES")
        for row in ans:
            print(*(row))
        return

    # If DFS didn't finish or failed, use Rip-Up and Reroute (Min-Conflicts / Simulated Annealing)
    # Assign initial paths using shortest path with current edge costs
    edge_usage = [0] * m
    unit_paths = [None] * num_units
    
    def dijkstra(s, t, weights):
        dist = [float('inf')] * n
        parent_edge = [-1] * n
        parent_node = [-1] * n
        dist[s] = 0
        pq = [(0, s)]
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            if u == t:
                break
            for v, e_idx in adj[u]:
                w = weights[e_idx]
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent_edge[v] = e_idx
                    parent_node[v] = u
                    heapq.heappush(pq, (dist[v], v))
                    
        if dist[t] == float('inf'):
            return None
        
        path = []
        curr = t
        while curr != s:
            path.append(parent_edge[curr])
            curr = parent_node[curr]
        path.reverse()
        return path

    # Initial routing
    base_weights = [1.0] * m
    for u_idx in range(num_units):
        s, t = units[u_idx][1], units[u_idx][2]
        w = [base_weights[e] * (1.0 + 5.0 * (edge_usage[e] / max(1, caps[e]))**2) for e in range(m)]
        path = dijkstra(s, t, w)
        if path is None:
            print("NO")
            return
        unit_paths[u_idx] = path
        for e in path:
            edge_usage[e] += 1

    # Rip-up and Reroute loop
    history_penalty = [0.0] * m
    iter_count = 0
    max_iters = 50000

    while time.time() - start_time < time_limit and iter_count < max_iters:
        iter_count += 1
        
        # Check violations
        violations = [e for e in range(m) if edge_usage[e] > caps[e]]
        if not violations:
            # Feasible solution found!
            ans = [[0] * m for _ in range(k)]
            for u_idx, path in enumerate(unit_paths):
                ord_id = units[u_idx][0]
                for e in path:
                    ans[ord_id][e] += 1
            print("YES")
            for row in ans:
                print(*(row))
            return
        
        # Update history penalties on congested edges
        for e in violations:
            history_penalty[e] += 1.0 + (edge_usage[e] - caps[e]) * 0.5
            
        # Pick conflicting units to reroute
        conflicted_units = []
        for u_idx in range(num_units):
            for e in unit_paths[u_idx]:
                if edge_usage[e] > caps[e]:
                    conflicted_units.append(u_idx)
                    break
                    
        random.shuffle(conflicted_units)
        # Reroute a subset of conflicted units
        reroute_count = min(len(conflicted_units), max(1, len(conflicted_units) // 2))
        
        for u_idx in conflicted_units[:reroute_count]:
            # Rip-up
            for e in unit_paths[u_idx]:
                edge_usage[e] -= 1
                
            s, t = units[u_idx][1], units[u_idx][2]
            # Compute dynamic weights
            w = [1.0 + history_penalty[e] + 10.0 * max(0, edge_usage[e] + 1 - caps[e])**2 + random.uniform(0, 0.1) for e in range(m)]
            new_path = dijkstra(s, t, w)
            if new_path is None:
                new_path = unit_paths[u_idx] # revert
            unit_paths[u_idx] = new_path
            for e in new_path:
                edge_usage[e] += 1

    # If still not solved
    violations = [e for e in range(m) if edge_usage[e] > caps[e]]
    if not violations:
        ans = [[0] * m for _ in range(k)]
        for u_idx, path in enumerate(unit_paths):
            ord_id = units[u_idx][0]
            for e in path:
                ans[ord_id][e] += 1
        print("YES")
        for row in ans:
            print(*(row))
    else:
        print("NO")

if __name__ == '__main__':
    solve()