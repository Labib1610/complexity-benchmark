import sys
from collections import defaultdict

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # Map: (x, y) -> list of z values
    reactions = defaultdict(list)
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        reactions[(x, y)].append(z)
    
    # Build bipartite graph: left = catalysts (x), right = solvents (y)
    # Edge exists if (x, y) has at least one reaction
    adj = [[] for _ in range(k + 1)]
    for (x, y), zlist in reactions.items():
        adj[x].append(y)
    
    # Hopcroft-Karp for maximum matching
    pair_u = [0] * (k + 1)
    pair_v = [0] * (k + 1)
    dist = [0] * (k + 1)
    
    from collections import deque
    
    def bfs():
        queue = deque()
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        dist[0] = float('inf')
        while queue:
            u = queue.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if pair_v[v] == 0:
                        dist[0] = dist[u] + 1
                    elif dist[pair_v[v]] == float('inf'):
                        dist[pair_v[v]] = dist[u] + 1
                        queue.append(pair_v[v])
        return dist[0] != float('inf')
    
    def dfs(u):
        for v in adj[u]:
            if pair_v[v] == 0 or (dist[pair_v[v]] == dist[u] + 1 and dfs(pair_v[v])):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = float('inf')
        return False
    
    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching != k:
        print("NO")
        return
    
    # Now we have a perfect matching between x and y
    # Need to assign z values such that all z are distinct
    # Build assignment problem: k reactions, k z values
    # reaction i (for catalyst i) uses solvent pair_u[i], and can use any z in reactions[(i, pair_u[i])]
    
    # Build bipartite graph: left = reactions (1..k), right = z values (1..k)
    adj2 = [[] for _ in range(k + 1)]
    for x in range(1, k + 1):
        y = pair_u[x]
        for z in reactions[(x, y)]:
            adj2[x].append(z)
    
    pair_u2 = [0] * (k + 1)
    pair_v2 = [0] * (k + 1)
    dist2 = [0] * (k + 1)
    
    def bfs2():
        queue = deque()
        for u in range(1, k + 1):
            if pair_u2[u] == 0:
                dist2[u] = 0
                queue.append(u)
            else:
                dist2[u] = float('inf')
        dist2[0] = float('inf')
        while queue:
            u = queue.popleft()
            if dist2[u] < dist2[0]:
                for v in adj2[u]:
                    if pair_v2[v] == 0:
                        dist2[0] = dist2[u] + 1
                    elif dist2[pair_v2[v]] == float('inf'):
                        dist2[pair_v2[v]] = dist2[u] + 1
                        queue.append(pair_v2[v])
        return dist2[0] != float('inf')
    
    def dfs2(u):
        for v in adj2[u]:
            if pair_v2[v] == 0 or (dist2[pair_v2[v]] == dist2[u] + 1 and dfs2(pair_v2[v])):
                pair_u2[u] = v
                pair_v2[v] = u
                return True
        dist2[u] = float('inf')
        return False
    
    matching2 = 0
    while bfs2():
        for u in range(1, k + 1):
            if pair_u2[u] == 0:
                if dfs2(u):
                    matching2 += 1
    
    if matching2 != k:
        print("NO")
        return
    
    print("YES")
    for x in range(1, k + 1):
        y = pair_u[x]
        z = pair_u2[x]
        print(f"{x} {y} {z}")

if __name__ == "__main__":
    solve()