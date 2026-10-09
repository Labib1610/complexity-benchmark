import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # x -> list of (y, z)
    by_x = [[] for _ in range(k + 1)]
    # z -> list of (x, y)
    by_z = [[] for _ in range(k + 1)]
    
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        by_x[x].append((y, z))
        by_z[z].append((x, y))
    
    # Since each catalyst x is permanently bound to a unique solvent y,
    # selecting all k catalysts automatically selects all k solvents.
    # The problem reduces to: for each catalyst x, choose a temperature z
    # such that all chosen temperatures are distinct (a perfect matching
    # in the bipartite graph between catalysts and temperatures).
    
    # Hopcroft-Karp for bipartite matching (catalysts on left, temperatures on right)
    pair_x = [0] * (k + 1)
    pair_z = [0] * (k + 1)
    INF = 10 ** 9
    dist = [0] * (k + 1)
    
    from collections import deque
    
    def bfs():
        dq = deque()
        for x in range(1, k + 1):
            if pair_x[x] == 0:
                dist[x] = 0
                dq.append(x)
            else:
                dist[x] = INF
        dist[0] = INF
        while dq:
            x = dq.popleft()
            if dist[x] < dist[0]:
                for y, z in by_x[x]:
                    if pair_z[z] == 0:
                        dist[0] = dist[x] + 1
                    elif dist[pair_z[z]] == INF:
                        dist[pair_z[z]] = dist[x] + 1
                        dq.append(pair_z[z])
        return dist[0] != INF
    
    def dfs(x):
        for y, z in by_x[x]:
            if pair_z[z] == 0 or (dist[pair_z[z]] == dist[x] + 1 and dfs(pair_z[z])):
                pair_x[x] = z
                pair_z[z] = x
                return True
        dist[x] = INF
        return False
    
    matching = 0
    while bfs():
        for x in range(1, k + 1):
            if pair_x[x] == 0:
                if dfs(x):
                    matching += 1
    
    if matching == k:
        out = ["YES"]
        for x in range(1, k + 1):
            z = pair_x[x]
            # find y for this x, z
            y = None
            for yy, zz in by_x[x]:
                if zz == z:
                    y = yy
                    break
            out.append(f"{x} {y} {z}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

solve()