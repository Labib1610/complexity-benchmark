import sys
import heapq
import time

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    contracts = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        contracts.append((s, t, d))

    edges = []
    adj = [[] for _ in range(n)]
    cap = []
    for j in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        edges.append((u, v))
        cap.append(c)
        adj[u].append((v, j))

    # Expand contracts into individual unit demands
    demands = []
    for c_idx, (s, t, d) in enumerate(contracts):
        for _ in range(d):
            demands.append((c_idx, s, t))

    num_demands = len(demands)

    if num_demands == 0:
        print("YES")
        for _ in range(k):
            print(*( [0] * m ))
        return

    # Check trivial connectivity for each contract
    for s, t, d in contracts:
        if d > 0:
            # BFS reachability
            visited = [False] * n
            q = [s]
            visited[s] = True
            found = False
            for curr in q:
                if curr == t:
                    found = True
                    break
                for v, _ in adj[curr]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
            if not found:
                print("NO")
                return

    # PathFinder / Negotiated Congestion Algorithm
    start_time = time.time()
    time_limit = 4.5

    h = [0.0] * m
    use = [0] * m
    paths = [[] for _ in range(num_demands)]

    def dijkstra(s, t, pres_fac):
        dist = [float('inf')] * n
        parent_node = [-1] * n
        parent_edge = [-1] * n
        dist[s] = 0
        pq = [(0, s)]

        while pq:
            d_curr, u = heapq.heappop(pq)
            if d_curr > dist[u]:
                continue
            if u == t:
                break
            for v, e_idx in adj[u]:
                # Cost function
                c_edge = (1.0 + h[e_idx]) * (1.0 + max(0, use[e_idx] + 1 - cap[e_idx]) * pres_fac)
                if dist[u] + c_edge < dist[v]:
                    dist[v] = dist[u] + c_edge
                    parent_node[v] = u
                    parent_edge[v] = e_idx
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

    pres_fac = 0.5
    solved = False

    # Initial routing
    for i in range(num_demands):
        c_idx, s, t = demands[i]
        path = dijkstra(s, t, 0.0)
        if path is None:
            print("NO")
            return
        paths[i] = path
        for e_idx in path:
            use[e_idx] += 1

    # Check if initially feasible
    if all(use[e] <= cap[e] for e in range(m)):
        solved = True

    iteration = 0
    while not solved and time.time() - start_time < time_limit:
        iteration += 1
        # Rip-up and reroute each demand
        for i in range(num_demands):
            c_idx, s, t = demands[i]
            # Rip up
            for e_idx in paths[i]:
                use[e_idx] -= 1

            # Reroute
            new_path = dijkstra(s, t, pres_fac)
            if new_path is None:
                # Restore old path
                for e_idx in paths[i]:
                    use[e_idx] += 1
                continue

            paths[i] = new_path
            for e_idx in paths[i]:
                use[e_idx] += 1

        # Check feasibility
        feasible = True
        for e in range(m):
            if use[e] > cap[e]:
                feasible = False
                h[e] += (use[e] - cap[e]) * 0.5

        if feasible:
            solved = True
            break

        pres_fac *= 1.1

    if not solved:
        print("NO")
        return

    # Build answer
    ans = [[0] * m for _ in range(k)]
    for i in range(num_demands):
        c_idx, s, t = demands[i]
        for e_idx in paths[i]:
            ans[c_idx][e_idx] += 1

    print("YES")
    for row in ans:
        print(*(row))

if __name__ == '__main__':
    solve()