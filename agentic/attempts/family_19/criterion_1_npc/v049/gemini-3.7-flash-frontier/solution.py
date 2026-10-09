import sys
import heapq
import time
import random

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    k = int(next(iterator))
    
    contracts = []
    total_demand = 0
    for _ in range(k):
        s = int(next(iterator))
        t = int(next(iterator))
        d = int(next(iterator))
        contracts.append((s, t, d))
        total_demand += d
        
    edges = []
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        cap = int(next(iterator))
        edges.append((u, v, cap))
        adj[u].append((v, i, cap))
    
    # Special fast case: k = 1 (Standard Maximum Flow with Dinic)
    if k == 1:
        s, t, d = contracts[0]
        if d == 0:
            print("YES")
            print(" ".join("0" for _ in range(m)))
            return
        
        # Dinic's Algorithm
        # Edge structure: [to, cap, flow, rev_idx, orig_edge_idx]
        graph = [[] for _ in range(n + 1)]
        for i, (u, v, cap) in enumerate(edges):
            fwd = [v, cap, 0, len(graph[v]), i]
            bwd = [u, 0, 0, len(graph[u]), -1]
            graph[u].append(fwd)
            graph[v].append(bwd)
            
        def bfs(level):
            for i in range(n + 1):
                level[i] = -1
            level[s] = 0
            queue = [s]
            head = 0
            while head < len(queue):
                curr = queue[head]
                head += 1
                for edge in graph[curr]:
                    nxt, cap, flow, _, _ = edge
                    if cap - flow > 0 and level[nxt] == -1:
                        level[nxt] = level[curr] + 1
                        queue.append(nxt)
            return level[t] != -1

        def dfs(curr, pushed, level, ptr):
            if pushed == 0 or curr == t:
                return pushed
            for idx in range(ptr[curr], len(graph[curr])):
                ptr[curr] = idx
                edge = graph[curr][idx]
                nxt, cap, flow, rev_idx, _ = edge
                if level[curr] + 1 != level[nxt] or cap - flow <= 0:
                    continue
                tr = dfs(nxt, min(pushed, cap - flow), level, ptr)
                if tr == 0:
                    continue
                edge[2] += tr
                graph[nxt][rev_idx][2] -= tr
                return tr
            return 0

        max_flow = 0
        level = [-1] * (n + 1)
        while bfs(level):
            ptr = [0] * (n + 1)
            while True:
                pushed = dfs(s, d - max_flow, level, ptr)
                if pushed == 0:
                    break
                max_flow += pushed
                if max_flow >= d:
                    break
            if max_flow >= d:
                break
                
        if max_flow < d:
            print("NO")
        else:
            ans = [0] * m
            for u in range(1, n + 1):
                for edge in graph[u]:
                    orig_idx = edge[4]
                    if orig_idx != -1:
                        ans[orig_idx] = edge[2]
            print("YES")
            print(" ".join(map(str, ans)))
        return

    # For k > 1, use PathFinder (Negotiated Congestion Routing)
    # Flatten each demand into individual unit pulses
    pulses = []
    for comm_idx, (s, t, d) in enumerate(contracts):
        for _ in range(d):
            pulses.append((comm_idx, s, t))
            
    num_pulses = len(pulses)
    if num_pulses == 0:
        print("YES")
        for _ in range(k):
            print(" ".join("0" for _ in range(m)))
        return

    # Check trivial connectivity for each contract
    for comm_idx, (s, t, d) in enumerate(contracts):
        if d > 0:
            visited = [False] * (n + 1)
            q = [s]
            visited[s] = True
            h = 0
            while h < len(q):
                curr = q[h]
                h += 1
                for nxt, _, _ in adj[curr]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)
            if not visited[t]:
                print("NO")
                return

    paths = [[] for _ in range(num_pulses)]
    edge_usage = [0] * m
    edge_history = [1.0] * m
    caps = [edges[i][2] for i in range(m)]

    start_time = time.time()
    multiplier = 1.0
    
    pulse_indices = list(range(num_pulses))
    
    max_iters = 300
    solved = False

    for iteration in range(max_iters):
        if time.time() - start_time > 4.5:
            break
            
        random.shuffle(pulse_indices)
        
        for p_idx in pulse_indices:
            comm_idx, s, t = pulses[p_idx]
            
            # Remove old path
            if paths[p_idx]:
                for e_idx in paths[p_idx]:
                    edge_usage[e_idx] -= 1
                paths[p_idx] = []
                
            # Dijkstra to find least cost path
            dist = [float('inf')] * (n + 1)
            parent_edge = [-1] * (n + 1)
            parent_node = [-1] * (n + 1)
            dist[s] = 0.0
            pq = [(0.0, s)]
            
            while pq:
                d_cur, u = heapq.heappop(pq)
                if d_cur > dist[u]:
                    continue
                if u == t:
                    break
                for v, e_idx, cap in adj[u]:
                    u_val = edge_usage[e_idx]
                    cost_e = edge_history[e_idx] * (1.0 + multiplier * max(0, u_val + 1 - cap))
                    if dist[u] + cost_e < dist[v]:
                        dist[v] = dist[u] + cost_e
                        parent_edge[v] = e_idx
                        parent_node[v] = u
                        heapq.heappush(pq, (dist[v], v))
                        
            if dist[t] == float('inf'):
                break
                
            # Reconstruct path
            curr = t
            new_path = []
            while curr != s:
                e_idx = parent_edge[curr]
                new_path.append(e_idx)
                curr = parent_node[curr]
            new_path.reverse()
            
            paths[p_idx] = new_path
            for e_idx in new_path:
                edge_usage[e_idx] += 1

        # Check if all capacities are satisfied
        overused = False
        for i in range(m):
            if edge_usage[i] > caps[i]:
                overused = True
                edge_history[i] += 0.8 * (edge_usage[i] - caps[i])
                
        if not overused:
            solved = True
            break
            
        multiplier += 0.8

    if not solved:
        print("NO")
        return

    print("YES")
    flow = [[0] * m for _ in range(k)]
    for p_idx in range(num_pulses):
        comm_idx = pulses[p_idx][0]
        for e_idx in paths[p_idx]:
            flow[comm_idx][e_idx] += 1
            
    for comm_idx in range(k):
        print(" ".join(map(str, flow[comm_idx])))

if __name__ == '__main__':
    solve()