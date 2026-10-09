import sys
from collections import defaultdict, deque

def main():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    
    # Map from data source to its fixed encryption module
    source_to_module = {}
    # Adjacency list: source -> list of channels
    adj = [[] for _ in range(k + 1)]
    
    for _ in range(t):
        x, y, z = map(int, input().split())
        source_to_module[x] = y
        adj[x].append(z)
    
    # We need to match each source to a distinct channel
    match_channel = [0] * (k + 1)  # channel -> source
    match_source = [0] * (k + 1)   # source -> channel
    
    def bfs():
        queue = deque()
        for u in range(1, k + 1):
            if match_source[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        dist[0] = float('inf')
        found = False
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if dist[match_channel[v]] == float('inf'):
                    dist[match_channel[v]] = dist[u] + 1
                    if match_channel[v] != 0:
                        queue.append(match_channel[v])
                    else:
                        found = True
        return found
    
    def dfs(u):
        for v in adj[u]:
            if dist[match_channel[v]] == dist[u] + 1:
                if match_channel[v] == 0 or dfs(match_channel[v]):
                    match_channel[v] = u
                    match_source[u] = v
                    return True
        dist[u] = float('inf')
        return False
    
    dist = [0] * (k + 1)
    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if match_source[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching == k:
        print("YES")
        for src in range(1, k + 1):
            ch = match_source[src]
            mod = source_to_module[src]
            print(src, mod, ch)
    else:
        print("NO")

if __name__ == "__main__":
    main()