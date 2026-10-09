import sys
from collections import defaultdict, deque

def main():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    
    # agent -> set of sectors
    agent_sectors = defaultdict(set)
    agent_vehicle = {}
    
    for _ in range(t):
        x, y, z = map(int, input().split())
        agent_sectors[x].add(z)
        agent_vehicle[x] = y  # all entries for same agent have same vehicle
    
    # Build bipartite graph: left = agents (1..k), right = sectors (1..k)
    # We'll use Hopcroft-Karp for efficiency
    
    adj = [[] for _ in range(k + 1)]
    for agent in range(1, k + 1):
        for sector in agent_sectors[agent]:
            adj[agent].append(sector)
    
    # match_sector[sector] = agent matched to it, 0 if none
    match_sector = [0] * (k + 1)
    dist = [0] * (k + 1)
    
    def bfs():
        q = deque()
        for u in range(1, k + 1):
            if match_sector[u] == 0:  # Actually we need match for agents, not sectors
                pass
        # We'll use match_agent[agent] = sector
        # Let's redo with match_agent
        return
    
    # Let's implement standard Hopcroft-Karp with match_agent and match_sector
    match_agent = [0] * (k + 1)  # match_agent[agent] = sector
    match_sector = [0] * (k + 1)  # match_sector[sector] = agent
    
    INF = 10**9
    
    def bfs():
        q = deque()
        for u in range(1, k + 1):
            if match_agent[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while q:
            u = q.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if dist[match_sector[v]] == INF:
                        dist[match_sector[v]] = dist[u] + 1
                        q.append(match_sector[v])
        return dist[0] != INF
    
    def dfs(u):
        if u != 0:
            for v in adj[u]:
                if dist[match_sector[v]] == dist[u] + 1 and dfs(match_sector[v]):
                    match_sector[v] = u
                    match_agent[u] = v
                    return True
            dist[u] = INF
            return False
        return True
    
    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if match_agent[u] == 0 and dfs(u):
                matching += 1
    
    if matching != k:
        print("NO")
        return
    
    print("YES")
    for agent in range(1, k + 1):
        sector = match_agent[agent]
        vehicle = agent_vehicle[agent]
        print(agent, vehicle, sector)

if __name__ == "__main__":
    main()