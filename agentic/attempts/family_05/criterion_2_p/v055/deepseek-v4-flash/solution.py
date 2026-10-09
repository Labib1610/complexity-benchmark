import sys
from collections import deque

def main():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    k = int(next(it))
    t = int(next(it))

    # Since each source is tied to a specific waveplate, we can just use source index
    # and later map back to waveplate.
    source_waveplate = [0] * (k + 1)
    adj = [[] for _ in range(k + 1)]

    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        source_waveplate[x] = y
        adj[x].append(z)

    # Hopcroft-Karp for maximum bipartite matching
    match_sensor = [0] * (k + 1)  # sensor -> source
    match_source = [0] * (k + 1)  # source -> sensor
    dist = [0] * (k + 1)

    def bfs():
        q = deque()
        for u in range(1, k + 1):
            if match_source[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = float('inf')
        dist[0] = float('inf')
        while q:
            u = q.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if dist[match_sensor[v]] == float('inf'):
                        dist[match_sensor[v]] = dist[u] + 1
                        q.append(match_sensor[v])
        return dist[0] != float('inf')

    def dfs(u):
        if u != 0:
            for v in adj[u]:
                if dist[match_sensor[v]] == dist[u] + 1 and dfs(match_sensor[v]):
                    match_sensor[v] = u
                    match_source[u] = v
                    return True
            dist[u] = float('inf')
            return False
        return True

    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if match_source[u] == 0 and dfs(u):
                matching += 1

    if matching != k:
        print("NO")
    else:
        print("YES")
        for x in range(1, k + 1):
            z = match_source[x]
            y = source_waveplate[x]
            print(x, y, z)

if __name__ == "__main__":
    main()