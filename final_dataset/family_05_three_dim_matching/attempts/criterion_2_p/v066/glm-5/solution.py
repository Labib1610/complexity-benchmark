import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    idx = 2
    # crew -> list of (route, proposal_index)
    crew_routes = [[] for _ in range(k + 1)]
    for i in range(t):
        x = int(data[idx]); y = int(data[idx+1]); z = int(data[idx+2])
        idx += 3
        crew_routes[x].append((z, i, x, y))
    
    # Hopcroft-Karp style matching: crews to routes
    # crew u can match route v if there's a proposal (u, *, v)
    # Since each crew has fixed airframe, we just need to output the proposal.
    
    pair_crew = [-1] * (k + 1)  # route -> crew
    pair_route = [-1] * (k + 1) # crew -> route
    INF = float('inf')
    dist = [0] * (k + 1)
    
    from collections import deque
    
    def bfs():
        dq = deque()
        found = False
        for u in range(1, k + 1):
            if pair_route[u] == -1:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        # dummy node 0
        dist[0] = INF
        while dq:
            u = dq.popleft()
            if dist[u] < dist[0]:
                for v, _pi, _x, _y in crew_routes[u]:
                    pu = pair_crew[v]
                    if pu == -1:
                        dist[0] = dist[u] + 1
                        found = True
                    elif dist[pu] == INF:
                        dist[pu] = dist[u] + 1
                        dq.append(pu)
        return found
    
    def dfs(u):
        for v, pi, x, y in crew_routes[u]:
            pu = pair_crew[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pair_crew[v] = u
                pair_route[u] = v
                crew_routes[u]  # no-op
                # store proposal info
                proposal_info[u] = (x, y, v)
                return True
        dist[u] = INF
        return False
    
    proposal_info = [None] * (k + 1)
    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pair_route[u] == -1:
                if dfs(u):
                    matching += 1
    if matching == k:
        out = ["YES"]
        for u in range(1, k + 1):
            x, y, z = proposal_info[u]
            out.append(f"{x} {y} {z}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

solve()